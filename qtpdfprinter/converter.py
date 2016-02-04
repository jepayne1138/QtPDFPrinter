"""Used to convert an .html file or raw HTML to a PDF"""

from PySide.QtCore import QApplication, QEventLoop
from PySide.QtWebKit import QWebView


def rel_path(src, dest):
    """Returns a relative path from the source to the destination file"""
    return os.path.relpath(
        os.path.abspath(dest),
        os.path.abspath(src),
    )

# ==========================================================================
# Everything below here is reference from a previous iteration of this
# module that I am cleaning up and rewriting

def render_template(template_file, **kwargs):
    template = env.get_template(template_file)
    return template.render(**kwargs)


def print_pdf(source, destination):
    app = QApplication(sys.argv)

    web = QWebView()

    loop = QEventLoop()
    web.loadFinished.connect(loop.quit)
    web.load(QUrl.fromLocalFile(source))
    loop.exec_()

    printer = QPrinter()
    printer.setPageSize(QPrinter.Letter)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(destination)
    web.print_(printer)

    app.exit()


def main():
    parser = argparse.ArgumentParser(description='Creates a pdf from an html file')
    parser.add_argument('file', type=str, help='Path to the html file')
    args = parser.parse_args()

    infile = args.file
    outfile = os.path.join(os.getcwd(), os.path.basename(os.path.splitext(infile)[0] + '.pdf'))

    html = render_template(
        os.path.basename(infile),
        # table=table,
    )

    print(__file__)
    print(rel_path(os.environ['TEMP'], __file__))

    # print_pdf(os.path.abspath(infile), outfile)


if __name__ == "__main__":
    main()
