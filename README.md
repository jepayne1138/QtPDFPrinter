# QtPDF Printer
Uses PySide / PyQt4 (will add support) for creating PDF's using Jinja2 templating

## Usage
### Module
**Raw HTML file (no templating)**
```python
import qtpdfprinter

qtpdfprinter.convert_html_to_pdf(sourc_path, destination_path)
```

### Command Line
From the command line:

`python html2pdf.py <html_source> <pdf_destination>`

## Dependencies
PySide / PyQt4
Jinja2 (might make optional if only needing raw HTML rendering)
