#!/usr/bin/env python3
"""
main.py

Baixa apenas um trecho (em áudio) de um vídeo do YouTube, para você guardar
batidas de atabaque e escutar depois sem precisar abrir o vídeo de novo.

Requisitos (instalar uma vez):
    pip install yt-dlp
    ffmpeg precisa estar instalado no sistema:
        - Windows: https://ffmpeg.org/download.html (ou "choco install ffmpeg")
        - Mac:     brew install ffmpeg
        - Linux:   sudo apt install ffmpeg

Uso:
    python main.py <URL> <inicio> <fim> [--nome "nome_da_batida"]

Exemplos de tempo aceitos: 1:23, 01:23, 1:02:15, 83 (segundos)

Exemplo:
    python main.py "https://www.youtube.com/watch?v=XXXXXXXX" 1:15 1:45 --nome "ijexa_intro"
"""

import argparse
import subprocess
import sys
import os


def parse_args():
    p = argparse.ArgumentParser(description="Baixa um trecho de áudio de um vídeo do YouTube.")
    p.add_argument("url", help="Link do vídeo do YouTube")
    p.add_argument("inicio", help="Tempo de início (ex: 1:23 ou 83)")
    p.add_argument("fim", help="Tempo de fim (ex: 1:45 ou 105)")
    p.add_argument("--nome", default=None, help="Nome do arquivo de saída (sem extensão)")
    p.add_argument("--pasta", default="clips_atabaque", help="Pasta onde salvar os clipes")
    return p.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.pasta, exist_ok=True)

    nome = args.nome or "clip"
    saida_template = os.path.join(args.pasta, f"{nome}.%(ext)s")

    # --download-sections faz o yt-dlp baixar (quando possível) só o trecho pedido,
    # em vez do vídeo inteiro.
    secao = f"*{args.inicio}-{args.fim}"

    cmd = [
        "yt-dlp",
        "-x",  # extrair só áudio
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--download-sections", secao,
        "--force-keyframes-at-cuts",
        "-o", saida_template,
        args.url,
    ]

    print("Rodando:", " ".join(cmd))
    resultado = subprocess.run(cmd)

    if resultado.returncode != 0:
        print("\nAlgo deu errado. Verifique se o yt-dlp e o ffmpeg estão instalados"
              " (veja as instruções no topo do script).")
        sys.exit(1)

    print(f"\nPronto! Seu trecho foi salvo em: {args.pasta}/{nome}.mp3")


if __name__ == "__main__":
    main()