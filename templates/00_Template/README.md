## Viewing slides

1. Install [Miniconda](https://conda.io/miniconda.html)
2. Install [RISE](https://github.com/damianavila/RISE)

```
conda install -c damianavila82 rise
```

3. Launch Jupyter and browse to the notebook
```
jupyter notebook
```

4. Navigation from Jupyter:

* Alt-r, "Enter/Exit Live Reveal Slideshow
* Shift-i, Toggle slide
* Shift-u, Toggle subslide
* Shift-f, Toggle fragment

[Usage](https://github.com/damianavila/RISE/blob/master/doc/usage.md)


## Exporting to PDF

Reference: https://damianavila.github.io/RISE/usage.html

1. Generate the slides and serve them using nbconvert. For example:

```
jupyter nbconvert --to slides speech.ipynb --post serve
```

This opens up a webpage in the browser at http://127.0.0.1:8000/speech.slides.html#/

2 - Add ?print-pdf to the query string as http://127.0.0.1:8000/speech.slides.html?print-pdf

Note that you need to remove the # at the end. The page will render the slides vertically.

3 - Save to PDF in Chrome using the print option

* Open the in-browser print dialog (Cmd/Ctrl + P).
* Change the Destination setting to Save as PDF.
* Change the Layout to Landscape.
* Change the Margins to None.
* Enable the Background graphics option.
* Click Save.