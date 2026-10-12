# Ecoá 🥁

Baixa apenas o trecho de áudio que você precisa de um vídeo do YouTube — feito para guardar e relembrar batidas de atabaque sem precisar reabrir o vídeo inteiro.

Chega de ficar procurando "aquele momento do vídeo" toda vez que esquece uma batida. Com o Ecoá você recorta só o pedaço que importa e guarda como MP3 na sua própria biblioteca pessoal de ritmos.

## ✨ Funcionalidades

- Baixa apenas o trecho de áudio especificado (não precisa baixar o vídeo inteiro)
- Exporta direto em MP3
- Organiza os clipes em uma pasta local, com o nome que você escolher
- Simples de usar via linha de comando

## 📋 Requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html)

## 🔧 Instalação

Clone o repositório:

```bash
git clone https://github.com/00MOREIRA00/ecoa.git
cd ecoa
```

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

Instale o ffmpeg:

```bash
# Mac
brew install ffmpeg

# Linux (Debian/Ubuntu)
sudo apt install ffmpeg

# Windows (recomendado - via winget)
winget install ffmpeg
```

> ⚠️ **Atenção (Windows/qualquer SO):** o ffmpeg é um **programa**, não uma biblioteca Python.
> **Não use** `pip install ffmpeg` — esse pacote no PyPI é apenas uma lib Python sem relação com o executável real, e vai te fazer achar que instalou quando na verdade não instalou nada útil. Use sempre `winget`, `brew`, `apt` ou o instalador manual abaixo.

**Depois de instalar, feche e abra o terminal novamente** (o PATH só atualiza em uma janela nova) e confira se funcionou:

```bash
ffmpeg -version
```

Se aparecer a versão, está tudo certo.

### Instalação manual do ffmpeg no Windows (caso o winget não funcione)

1. Baixe em https://www.gyan.dev/ffmpeg/builds/ → clique em **"release essentials"** (arquivo `.zip`)
2. Extraia o conteúdo para `C:\ffmpeg` (confirme que existe `C:\ffmpeg\bin\ffmpeg.exe`)
3. Pesquise **"Variáveis de Ambiente"** no menu Iniciar → **"Editar as variáveis de ambiente do sistema"**
4. Clique em **"Variáveis de Ambiente..."**
5. Em "Variáveis do sistema", selecione `Path` → **Editar** → **Novo**
6. Cole: `C:\ffmpeg\bin`
7. Clique OK em tudo, feche todas as janelas
8. Abra um terminal **novo** e teste `ffmpeg -version`

## ▶️ Como usar

```bash
python main.py <URL> <inicio> <fim> [--nome "nome_da_batida"]
```

**Parâmetros:**

| Parâmetro | Descrição | Exemplo |
|---|---|---|
| `URL` | Link do vídeo do YouTube | `"https://www.youtube.com/watch?v=XXXXX"` |
| `inicio` | Tempo de início do trecho | `1:15` ou `75` (segundos) |
| `fim` | Tempo de fim do trecho | `1:45` ou `105` (segundos) |
| `--nome` | Nome do arquivo de saída (opcional) | `"ijexa_intro"` |
| `--pasta` | Pasta onde salvar os clipes (opcional, padrão: `clips_atabaque`) | `"minhas_batidas"` |

**Exemplo:**

```bash
python main.py "https://www.youtube.com/watch?v=XXXXX" 1:15 1:45 --nome "ijexa_intro"
```

Isso vai gerar `clips_atabaque/ijexa_intro.mp3` com somente o trecho entre 1:15 e 1:45.

## 📂 Organização sugerida

Vá criando sua biblioteca pessoal de batidas com nomes descritivos:

```
clips_atabaque/
├── ijexa_intro.mp3
├── angola_variacao2.mp3
├── barravento_break.mp3
└── aviso_final.mp3
```

## ⚠️ Aviso

Este projeto foi criado para **uso pessoal e estudo**, como apoio à prática instrumental. Baixar conteúdo do YouTube pode contrariar os Termos de Serviço da plataforma — use com responsabilidade e não redistribua o conteúdo baixado.

## 📝 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE).

---

Feito com 🥁 por quem não quer esquecer o toque.