import argparse
import qtpdfprinter.templating as templating


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
    parser.add_argument(
        '-l', '--link', type=str,
        help='Path to the external links directory'
    )

    # Parse and return arguments
    return parser.parse_args()


def process_commands():
    """Parses and processes command line options"""
    # Parse and handle each different command
    args = parse_arguments()

    templating.convert_template_to_pdf(
        args.source, args.destination, base_dir=args.link,
    )
