/* Homepage interactions: scroll reveal and cursor spotlight. */
(function () {
  "use strict";

  function prefersReducedMotion() {
    return (
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    );
  }

  function initReveal() {
    var elements = document.querySelectorAll(".reveal");
    if (!elements.length) return;

    if (prefersReducedMotion() || !("IntersectionObserver" in window)) {
      elements.forEach(function (element) {
        element.classList.add("is-visible");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    elements.forEach(function (element) {
      observer.observe(element);
    });
  }

  function initGlow() {
    if (
      prefersReducedMotion() ||
      (window.matchMedia && window.matchMedia("(hover: none)").matches)
    ) {
      return;
    }

    var glow = document.createElement("div");
    glow.className = "cursor-glow";
    glow.setAttribute("aria-hidden", "true");
    document.body.appendChild(glow);

    var animationFrame = null;
    var x = 0;
    var y = 0;

    function paint() {
      glow.style.setProperty("--mx", x + "px");
      glow.style.setProperty("--my", y + "px");
      animationFrame = null;
    }

    window.addEventListener(
      "mousemove",
      function (event) {
        x = event.clientX;
        y = event.clientY;
        if (!animationFrame) animationFrame = window.requestAnimationFrame(paint);
      },
      { passive: true }
    );
  }

  function init() {
    initReveal();
    initGlow();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
