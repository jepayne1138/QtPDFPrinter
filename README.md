# QtPDF Printer
Uses PySide / PyQt4 (will add support) for creating PDF's using Jinja2 templating

The package is designed so that Jinja2 should not be a dependency if the library will only be used for creating PDFs from raw HTML files.  However, neither the command line version nor the templating functionality will work or without Jinja2 installed, raising an ImportError.

## Usage
### Module
**Raw HTML file (no templating)**
```python
import qtpdfprinter.converter as converter

converter.convert_html_to_pdf(sourc_path, destination_path)
```

**Jinja2 template**
```python
import qtpdfprinter.templating as templating

templating.convert_template_to_pdf(sourc_path, destination_path, context={})
```


### Command Line
From the command line:

`python html2pdf.py <html_source> <pdf_destination>`

## Dependencies
PySide / PyQt4
Jinja2 (might make optional if only needing raw HTML rendering)
