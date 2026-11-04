# PDF Background Remover

A high-performance Python tool designed to remove yellowed, shaded, or noisy backgrounds from scanned PDF documents (such as manuscripts and books like `ibn_katheer_dhamrah.pdf`).

## Features

- **Multiple Cleaning Modes**:
  - `color` (Default): Retains ALL original text and ink colors (black text, red headings, stamps, blue ink, marks) while turning non-text paper background to pure `#FFFFFF` white.
  - `grayscale`: Preserves anti-aliased font edges in grayscale while turning background to pure `#FFFFFF` white.
  - `adaptive_bw`: Binarizes text into high-contrast monochrome (black & white) with automatic noise despeckling.
- **Fast Parallel Processing**: Multi-core CPU multiprocessing for processing large PDFs (such as 600+ page books) in seconds/minutes.
- **Page Selection**: Option to process specific page ranges (`-p 1-10`) or the entire document (`-p all`).
- **Resolution & Compression Control**: Configurable DPI and JPEG/PNG quality options.

## Installation

Ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Remove background from `ibn_katheer_dhamrah.pdf` (Default Color Mode)

```bash
python main.py -i ibn_katheer_dhamrah.pdf -o ibn_katheer_dhamrah_clean.pdf
```

### 2. Process first 10 pages for testing

```bash
python main.py -i ibn_katheer_dhamrah.pdf -o test_sample.pdf -p 1-10
```

### 3. Use Adaptive Monochrome (Black & White) Mode

```bash
python main.py -i ibn_katheer_dhamrah.pdf -o ibn_katheer_bw.pdf -m adaptive_bw
```

### 4. Use Color-Preserving Mode

```bash
python main.py -i ibn_katheer_dhamrah.pdf -o ibn_katheer_color.pdf -m color
```

## CLI Arguments

| Argument | Short | Description | Default |
|---|---|---|---|
| `--input` | `-i` | Path to input PDF file | `ibn_katheer_dhamrah.pdf` |
| `--output` | `-o` | Output PDF file path | `<input>_clean.pdf` |
| `--mode` | `-m` | Cleaning mode (`grayscale`, `adaptive_bw`, `color`) | `grayscale` |
| `--pages` | `-p` | Pages to process (e.g. `1-10`, `1,3,5`, `all`) | `all` |
| `--dpi` | `-d` | Rendering DPI resolution | `150` |
| `--workers` | `-w` | Number of parallel processes | Auto-detected CPU cores |
| `--bg-kernel` | | Morphological kernel size for background estimation | `35` |
| `--white-thresh` | | White cutoff threshold (0-255) | `215` |
| `--black-thresh` | | Black cutoff threshold (0-255) | `40` |
| `--quality` | | Output JPEG quality (1-100) | `85` |

## Programmatic API Usage

You can also import and use the library directly in Python:

```python
from remove_bg import process_pdf, CleaningMode

process_pdf(
    input_path="ibn_katheer_dhamrah.pdf",
    output_path="ibn_katheer_dhamrah_clean.pdf",
    mode=CleaningMode.GRAYSCALE,
    dpi=150,
    pages_spec="1-20"
)
```
