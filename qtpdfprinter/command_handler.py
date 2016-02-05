import argparse
import os
import qtpdfprinter.converter as converter


def parse_arguments():
    """Parses commands line options"""
    # Create main parser and subparsers
    parser = argparse.ArgumentParser(
        description='Command line interface for converting HTML to PDF'
    )

    parser.add_argument(
        'source', type=str,
        help='Path to the source HTML file',
    )

    parser.add_argument(
        'destination', type=str,
        help='Path to the destination PDF file'
    )

    # Parse and return arguments
    return parser.parse_args()


def process_commands():
    """Parses and processes command line options"""
    # Parse and handle each different command
    args = parse_arguments()

    converter.convert_html_to_pdf(args.source, args.destination)
