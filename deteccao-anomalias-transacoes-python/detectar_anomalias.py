import csv
import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "transacoes.csv"
OUTPUT_FILE = BASE_DIR / "anomalias_detectadas.csv"


def carregar_transacoes(caminho):
    with caminho.open("r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        transacoes = list(leitor)

    for transacao in transacoes:
        transacao["valor"] = float(transacao["valor"])
        transacao["hora"] = int(transacao["hora"])

    return transacoes


def calcular_media(valores):
    return sum(valores) / len(valores)


def calcular_desvio_padrao(valores, media):
    variancia = sum((valor - media) ** 2 for valor in valores) / len(valores)
    return math.sqrt(variancia)


def avaliar_transacao(transacao, media, desvio_padrao):
    motivos = []
    valor = transacao["valor"]
    hora = transacao["hora"]
    pais = transacao["pais"].strip().lower()
    tipo = transacao["tipo"].strip().lower()

    z_score = 0
    if desvio_padrao > 0:
        z_score = (valor - media) / desvio_padrao

    if z_score > 2:
        motivos.append(f"valor muito acima da media (z-score {z_score:.2f})")

    if valor >= 5000:
        motivos.append("valor acima de R$ 5.000")

    if 0 <= hora <= 5:
        motivos.append("transacao em horario incomum")

    if pais != "brasil":
        motivos.append("transacao internacional")

    if tipo == "saque" and valor >= 2000:
        motivos.append("saque de alto valor")

    return motivos, z_score


def detectar_anomalias(transacoes):
    valores = [transacao["valor"] for transacao in transacoes]
    media = calcular_media(valores)
    desvio_padrao = calcular_desvio_padrao(valores, media)
    anomalias = []

    for transacao in transacoes:
        motivos, z_score = avaliar_transacao(transacao, media, desvio_padrao)

        if motivos:
            resultado = transacao.copy()
            resultado["z_score"] = f"{z_score:.2f}"
            resultado["motivos"] = "; ".join(motivos)
            anomalias.append(resultado)

    return anomalias


def salvar_anomalias(anomalias, caminho):
    campos = [
        "id_transacao",
        "cliente_id",
        "valor",
        "tipo",
        "pais",
        "hora",
        "canal",
        "z_score",
        "motivos",
    ]

    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(anomalias)


def main():
    transacoes = carregar_transacoes(INPUT_FILE)
    anomalias = detectar_anomalias(transacoes)
    salvar_anomalias(anomalias, OUTPUT_FILE)

    print(f"Total de transacoes analisadas: {len(transacoes)}")
    print(f"Total de anomalias encontradas: {len(anomalias)}")
    print(f"Arquivo gerado: {OUTPUT_FILE.name}")

    if anomalias:
        print("\nAnomalias encontradas:")
        for anomalia in anomalias:
            print(
                f"- Transacao {anomalia['id_transacao']}: "
                f"R$ {anomalia['valor']:.2f} | {anomalia['motivos']}"
            )


if __name__ == "__main__":
    main()

