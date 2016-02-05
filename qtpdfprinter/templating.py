import os
import tempfile
from jinja2 import Template
import qtpdfprinter.converter as converter


def convert_template_to_pdf(
        source, destination, context=None,
        base_dir=None, **kwargs):
    """Wraps the convert_html_to_pdf function by first processing a template

    The source parameter must point to a Jinja2 template.  The template is
    rendered and saved to a temporary HTML file, then the temporary file is
    printed as a PDF file.

    Exposes a function to the template called link_path() that will create
    the proper paths to external files based on the given base_dir.  As this
    would be built when this function runs, it means that if link_path was
    passed through the context dict, it will be overwritten.
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(source))

    if context is None:
        context = {}

    # Create a temporary file for the output HTML from the template
    # We must have a path for the QWebView.load() method
    try:
        with tempfile.NamedTemporaryFile(
                'r+', suffix='.html', delete=False) as temp_file:
            # Update the context dict with a helper function that will build
            # proper relative path to external resources when rendered
            context['link_path'] = link_path_factory(base_dir, temp_file.name)

            with open(source, 'r') as src_file:
                template = Template(src_file.read())

            temp_file.write(template.render(**context))

        # We need to close the file for the QWebView to open
        converter.convert_html_to_pdf(temp_file.name, destination, **kwargs)
    finally:
        # No matter what, remove the temporary file when done
        os.remove(temp_file.name)


def link_path_factory(base_dir, src_file):
    abs_base_dir = os.path.abspath(base_dir)
    abs_src_dir = os.path.abspath(os.path.dirname(src_file))

    def inner(external_path):
        return os.path.relpath(
            os.path.join(abs_base_dir, external_path),
            abs_src_dir,
        )

    return inner
