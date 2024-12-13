(function () {
    /**
     * Create a banner and mount it to the DOM as the first element inside the `body`.
     *
     * @param innerHTML {string} The HTML content you want the banner to contain.
     */
    function displayBanner(innerHTML = "") {
        const sphinxRTDSidebarEl = document.querySelector('.wy-side-nav-search');
        const zIndexOfSphinxRTDSidebar = sphinxRTDSidebarEl !== null ? parseInt(window.getComputedStyle(sphinxRTDSidebarEl).zIndex) : 0;

        const divEl = document.createElement("div");
        divEl.style.backgroundColor = "red";
        divEl.style.textAlign = "center";
        divEl.style.zIndex = `${zIndexOfSphinxRTDSidebar + 1}`;
        divEl.style.position = "relative";
        divEl.innerHTML = innerHTML;
        document.body.insertBefore(divEl, document.body.firstChild);

        // Now that we've mounted the banner to the DOM, get its height in pixels and give the sidebar's search area
        // that same number of pixels of top margin; that way, the banner won't cover that element. Also, do the same
        // thing whenever the browser's width changes, since the banner's height could change in that situation, too.
        sphinxRTDSidebarEl.style.marginTop = window.getComputedStyle(divEl).height;
        addEventListener("resize", () => {
            sphinxRTDSidebarEl.style.marginTop = window.getComputedStyle(divEl).height;
        });
    }

    // Register a callback function to run when the web page has fully loaded.
    window.addEventListener("load", (event) => {
        displayBanner('<strong>This website is in early development.</strong> You can access our production documentation <a href="https://microbiomedata.org/documentation/" style="color: black;">here</a>.');
    });
})();