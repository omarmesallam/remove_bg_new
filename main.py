#!/usr/bin/env python3
"""
CLI tool for removing background from PDF files (e.g., ibn_katheer_dhamrah.pdf).
"""

import argparse
import os
import sys

from remove_bg import CleaningMode, process_pdf


def main():
    parser = argparse.ArgumentParser(
        description="PDF Background Remover - Remove yellowed/shaded backgrounds from scanned PDFs."
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        default="ibn_katheer_dhamrah.pdf",
        help="Path to input PDF file (default: ibn_katheer_dhamrah.pdf)"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Path to output cleaned PDF file (default: <input>_clean.pdf)"
    )

    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["color", "grayscale", "adaptive_bw"],
        default="color",
        help="Cleaning mode: 'color' (default: removes paper background while keeping ALL original text/ink colors), 'grayscale' (crisp gray text), 'adaptive_bw' (monochrome black/white)."
    )

    parser.add_argument(
        "-p", "--pages",
        type=str,
        default="all",
        help="Pages to process, e.g. '1-10', '1,3,5', or 'all' (default: all)"
    )

    parser.add_argument(
        "-d", "--dpi",
        type=int,
        default=150,
        help="Rendering resolution DPI (default: 150)"
    )

    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=None,
        help="Number of parallel worker processes (default: auto-detect CPU cores)"
    )

    parser.add_argument(
        "--bg-kernel",
        type=int,
        default=35,
        help="Kernel size for background surface estimation (default: 35)"
    )

    parser.add_argument(
        "--white-thresh",
        type=int,
        default=215,
        help="White level cutoff threshold 0-255 (default: 215)"
    )

    parser.add_argument(
        "--black-thresh",
        type=int,
        default=40,
        help="Black level cutoff threshold 0-255 (default: 40)"
    )

    parser.add_argument(
        "--no-despeckle",
        action="store_true",
        help="Disable noise despeckling in adaptive_bw mode"
    )

    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="JPEG compression quality 1-100 (default: 85)"
    )

    args = parser.parse_args()

    input_path = args.input
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = args.output
    else:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_clean{ext}"

    mode = CleaningMode(args.mode)

    try:
        process_pdf(
            input_path=input_path,
            output_path=output_path,
            mode=mode,
            dpi=args.dpi,
            pages_spec=args.pages,
            workers=args.workers,
            bg_kernel_size=args.bg_kernel,
            white_threshold=args.white_thresh,
            black_threshold=args.black_thresh,
            despeckle=not args.no_despeckle,
            jpeg_quality=args.quality
        )
    except Exception as e:
        print(f"Error processing PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
