## Setting up slides using reveal.js

**This has been tested with reveal.js 3.6.0**

1. Make a copy of the 00_Template folder, e.g. 01_MyModule

2. Download the latest release version of reveal.js from https://github.com/hakimel/reveal.js/releases

3. Unzip and drop the contents into the `reveal.js` folder, e.g `01_MyModule/reveal.js`

4. Replace `index.html` with index.html.template

5. The resulting folder should look like this:

```
01_MyModule\reveal.js> dir /b
    .gitignore
    .travis.yml
    assets
    bower.json
    CONTRIBUTING.md
    css
    demo.html
    Gruntfile.js
    index.html  <-- replaced with index.html.template
    index.html.template
    js
    lib
    LICENSE
    package.json
    plugin
    README.md
    test
```

6. From here, you have two options 1) run the HTML statically, or 2) run as a local web server for more advanced features such as *printing*, external markdown, presenter notes, master - client slide navigation. Refer to the reveal.js link above for more details.

   * Easy option: open index.html from your browser to view the slide deck. Note that printing support will not work here.

   * Web-server option: run `npm install`, followed by `npm start`.

        ```
        01_MyModule\reveal.js> npm install
        01_MyModule\reveal.js> npm start
        ```
        View the slide deck at http://localhost:8000

        To print the slide deck, go to http://localhost:8000/print-pdf from the **Chrome** browser. You can then print using `Ctrl+P`.