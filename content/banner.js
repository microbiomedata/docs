(function () {
    /**
     * Create a banner and mount it to the DOM as the first element inside the `body`.
     *
     * @param innerHTML {string} The HTML content you want the banner to contain.
     * @param backgroundColor {string} The CSS color of the banner's background.
     */
    function displayBanner(innerHTML = "", backgroundColor = "red") {
        const divEl = document.createElement("div");
        divEl.style.backgroundColor = backgroundColor;
        divEl.style.textAlign = "center";
        divEl.innerHTML = innerHTML;
        document.body.insertBefore(divEl, document.body.firstChild);
    }

    displayBanner('<strong>This website is in early development.</strong> You can access our production documentation <a href="https://microbiomedata.org/documentation/" style="color: black;">here</a>.');
})();