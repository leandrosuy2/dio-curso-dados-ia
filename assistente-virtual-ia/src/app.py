import argparse
import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
BASE_CONHECIMENTO = BASE_DIR / "data" / "base_conhecimento.json"
PERGUNTAS_TESTE = BASE_DIR / "data" / "perguntas_teste.json"


MENSAGEM_FORA_DA_BASE = (
    "Nao encontrei informacao suficiente na minha base de conhecimento para "
    "responder com seguranca. Posso ajudar com orcamento, reserva de emergencia, "
    "dividas, cartao de credito, Pix e metas financeiras."
)


def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9áàâãéêíóôõúç\s]", " ", texto)
    return set(texto.split())


def carregar_json(caminho):
    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def identificar_tema(pergunta, base):
    tokens = normalizar(pergunta)
    melhor_tema = None
    melhor_pontuacao = 0

    for tema, conteudo in base.items():
        palavras = set(conteudo["palavras_chave"])
        pontuacao = len(tokens.intersection(palavras))

        if pontuacao > melhor_pontuacao:
            melhor_tema = tema
            melhor_pontuacao = pontuacao

    if melhor_tema is None:
        return "fora_da_base", 0

    total_palavras_tema = len(base[melhor_tema]["palavras_chave"])
    confianca = melhor_pontuacao / total_palavras_tema
    return melhor_tema, confianca


def montar_resposta(pergunta, base):
    tema, confianca = identificar_tema(pergunta, base)

    if tema == "fora_da_base":
        return {
            "tema": tema,
            "confianca": 0,
            "resposta": MENSAGEM_FORA_DA_BASE,
        }

    conteudo = base[tema]
    passos = "\n".join(f"{indice}. {passo}" for indice, passo in enumerate(conteudo["passos"], start=1))

    resposta = (
        f"Tema identificado: {tema}\n"
        f"Confianca aproximada: {confianca:.2f}\n\n"
        f"{conteudo['resposta']}\n\n"
        f"Passos sugeridos:\n{passos}\n\n"
        f"Proxima acao sugerida: {conteudo['proxima_acao']}\n\n"
        "Observacao: esta orientacao e educativa e nao substitui atendimento financeiro profissional."
    )

    return {
        "tema": tema,
        "confianca": confianca,
        "resposta": resposta,
    }


def conversar():
    base = carregar_json(BASE_CONHECIMENTO)
    print("Bia Financas Simples")
    print("Digite sua pergunta ou escreva 'sair' para encerrar.\n")

    while True:
        pergunta = input("Voce: ").strip()

        if pergunta.lower() in {"sair", "exit", "quit"}:
            print("Bia: Ate mais. Continue cuidando do seu dinheiro com calma e clareza.")
            break

        resultado = montar_resposta(pergunta, base)
        print(f"\nBia:\n{resultado['resposta']}\n")


def avaliar():
    base = carregar_json(BASE_CONHECIMENTO)
    perguntas = carregar_json(PERGUNTAS_TESTE)
    acertos = 0

    print("Avaliacao do assistente\n")

    for item in perguntas:
        resultado = montar_resposta(item["pergunta"], base)
        tema_obtido = resultado["tema"]
        tema_esperado = item["tema_esperado"]
        correto = tema_obtido == tema_esperado
        acertos += int(correto)

        status = "OK" if correto else "FALHA"
        print(f"[{status}] {item['pergunta']}")
        print(f"  Esperado: {tema_esperado}")
        print(f"  Obtido:   {tema_obtido}\n")

    total = len(perguntas)
    taxa = acertos / total * 100
    print(f"Resultado: {acertos}/{total} respostas classificadas corretamente ({taxa:.1f}%).")


def main():
    parser = argparse.ArgumentParser(description="Bia Financas Simples")
    parser.add_argument("--pergunta", help="Envia uma pergunta unica para o assistente.")
    parser.add_argument("--avaliar", action="store_true", help="Executa perguntas de avaliacao.")
    args = parser.parse_args()

    if args.avaliar:
        avaliar()
        return

    if args.pergunta:
        base = carregar_json(BASE_CONHECIMENTO)
        resultado = montar_resposta(args.pergunta, base)
        print(resultado["resposta"])
        return

    conversar()


if __name__ == "__main__":
    main()

