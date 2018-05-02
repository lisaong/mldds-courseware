## Setting up reveal.js

Download the latest release version of reveal.js from https://github.com/hakimel/reveal.js/releases

**This has been tested with 3.6.0**

1. Unzip and drop the contents (**except for index.html**) into the `reveal.js` folder, e.g `04_SpeechTimeSeries/reveal.js`

```
04_SpeechTimeSeries\reveal.js>dir /b
    .gitignore
    .travis.yml
    assets
    bower.json
    CONTRIBUTING.md
    css
    demo.html
    Gruntfile.js
    index.html
    js
    lib
    LICENSE
    package.json
    plugin
    README.md
    slides
    test
```

2. Run `npm install`, followed by `npm start`.
```
04_SpeechTimeSeries\reveal.js>npm install
04_SpeechTimeSeries\reveal.js>npm start
```

You can now browse the slide deck at http://localhost:8000

To print the slide deck, go to http://localhost:8000/print-pdf from the Chrome browser. You can then print using `Ctrl+P`.