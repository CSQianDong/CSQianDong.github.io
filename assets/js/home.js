/* Homepage interactions: scroll reveal, hero rotator, and cursor spotlight. */
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

  function initRotator() {
    var element = document.getElementById("hero-rotator");
    if (!element) return;

    var phrases;
    try {
      phrases = JSON.parse(element.getAttribute("data-phrases"));
    } catch (error) {
      phrases = [];
    }

    if (!phrases || !phrases.length) return;
    element.textContent = phrases[0];

    if (prefersReducedMotion()) return;

    var phraseIndex = 0;
    var characterIndex = phrases[0].length;
    var deleting = true;

    function tick() {
      var phrase = phrases[phraseIndex];
      element.textContent = phrase.substring(0, characterIndex);

      var delay = deleting ? 45 : 95;

      if (deleting && characterIndex === 0) {
        deleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        delay = 350;
      } else if (!deleting && characterIndex === phrase.length) {
        deleting = true;
        delay = 1500;
      } else {
        characterIndex += deleting ? -1 : 1;
      }

      window.setTimeout(tick, delay);
    }

    window.setTimeout(tick, 1500);
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
    initRotator();
    initGlow();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
