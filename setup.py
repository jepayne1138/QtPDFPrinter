from setuptools import setup
setup(
    name='QtPDFPrinter',
    packages=['qtpdfprinter'],
    version='1.0a1',
    description='Creates PDFs from HTML or Jinja2 Templates using PySide',
    author='James Payne',
    author_email='jepayne1138@gmail.com',
    url='https://github.com/jepayne1138/QtPDFPrinter',
    license='MIT',
    download_url='https://github.com/jepayne1138/QtPDFPrinter/tarball/1.0a1',
    keywords='html pyside html convert pdf jinja',
    install_requires=['PySide', 'Jinja2'],
    classifiers=[],
)
