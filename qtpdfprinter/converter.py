"""Used to convert an .html file or raw HTML to a PDF"""

from contextlib import contextmanager
from PySide.QtCore import QApplication, QEventLoop, QTimer, QUrl
from PySide.QtWebKit import QWebView
from PySide.QtGui import QPrinter


def convert_html_to_pdf(source, destination, page_size=QPrinter.Letter,
        print_format=QPrinter.PdfFormat, app=None):
    """Converts an .html file at the source to a .pdf at the destination

    Any external files linked in the source file must be paths relative to
    the location of the source file itself.  If building the html file
    dynamically, the rel_path function can be used to create proper
    relative paths using the .html location as the source location.

    The conversion is done using th ability of a QPrinter to print
    a QWebView to a PDF.  This means we must have some Qt bindings, either
    PySide (default) or PyQt4 (5 support incoming?), but then are only
    limited by what the QWebView can display.

    While the intent is so print to a PDF, the format parameter is exposed
    so that this can be used to print directly to a printer or (if >=Qt4.2)
    PostScript format.

    If this is being used in a larger QApplication, we should only have one
    instance of QApplication, so pass the existing instance to the `app`
    parameter.
    """
    if app is None:
        app = QApplication()  # Shouldn't need sys.argv

    view = QWebView()

    # We want to ensure the page was fully loaded before printing, so
    # we wait for the loadFinished event to fire.
    with wait_for_signal(view.loadFinished):
        view.load(QUrl.fromLocalFile(source))

    # With the QWebView loaded, we now print to the destination PDF
    printer = QPrinter()
    printer.setPageSize(page_size)
    printer.setOutputFormat(print_format)
    printer.setOutputFileName(destination)
    view.print_(printer)

    # Exit the application
    app.exit()


@contextmanager
def wait_for_signal(signal, timeout=10000):
    """Waits the given signal to be emitted, or breaks after a timeout

    This context manager wraps a method of using a nested event loop to
    wait for a signal, but additionally adds a timeout in case the signal
    was prematurely emitted (in which case we will never catch it) or if
    there is some kind of error and the signal is never emitted.

    This context manager used here is inspired by code from a blob by John
    Reaver, of which an archive can be found here:

    https://web.archive.org/web/20160126155634/http://jdreaver.com/
    posts/2014-07-03-waiting-for-signals-pyside-pyqt.html
    """
    loop = QEventLoop()

    # When the signal is caught, the loop will break
    signal.connect(loop.quit)

    # The content in the context manager will now be executed
    # The timeout doesn't start until this block is finished, so make sure
    # there is no blocking calls in the with block.
    yield

    is timeout is None:  # Not False as possible 0ms timeout would be False
        QTimer.singleShot(timeout, loop.quit)
    loop.exec_()


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
