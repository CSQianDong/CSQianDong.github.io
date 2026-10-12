/* Progressive enhancements for the bilingual homepage navigation. */
(function () {
  "use strict";

  function init() {
    var navigation = document.querySelector(".t-nav");
    if (!navigation) return;

    var toggle = navigation.querySelector(".t-menu-toggle");
    var menu = navigation.querySelector("#primary-links");
    var label = toggle && toggle.querySelector(".t-menu-toggle__label");
    var frame = null;
    var activeLink = null;
    var sections = [];

    if (menu) {
      menu.querySelectorAll('a[href^="#"]').forEach(function (link) {
        var target = document.getElementById(link.getAttribute("href").slice(1));
        if (target) sections.push({ link: link, target: target });
      });
    }

    function updateActiveSection() {
      frame = null;
      if (!sections.length) return;

      var marker = navigation.getBoundingClientRect().bottom + 48;
      var current = sections[0].link;
      sections.forEach(function (section) {
        if (section.target.getBoundingClientRect().top <= marker) {
          current = section.link;
        }
      });

      if (current === activeLink) return;
      sections.forEach(function (section) {
        if (section.link === current) {
          section.link.setAttribute("aria-current", "location");
        } else {
          section.link.removeAttribute("aria-current");
        }
      });
      activeLink = current;
    }

    function scheduleUpdate() {
      if (frame === null) frame = window.requestAnimationFrame(updateActiveSection);
    }

    function setMenuOpen(open) {
      navigation.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      var text = toggle.getAttribute(open ? "data-label-close" : "data-label-open");
      if (text) {
        if (label) label.textContent = text;
        toggle.setAttribute("aria-label", text);
      }
      scheduleUpdate();
    }

    if (toggle && menu) {
      navigation.classList.add("is-enhanced");
      setMenuOpen(false);

      toggle.addEventListener("click", function () {
        setMenuOpen(toggle.getAttribute("aria-expanded") !== "true");
      });

      menu.addEventListener("click", function (event) {
        if (event.target.closest("a")) setMenuOpen(false);
      });

      document.addEventListener("click", function (event) {
        if (!navigation.contains(event.target)) setMenuOpen(false);
      });

      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && navigation.classList.contains("is-open")) {
          setMenuOpen(false);
          toggle.focus();
        }
      });
    }

    window.addEventListener("scroll", scheduleUpdate, { passive: true });
    window.addEventListener("resize", function () {
      if (toggle && menu && window.innerWidth > 700) setMenuOpen(false);
      scheduleUpdate();
    });
    window.addEventListener("load", scheduleUpdate);
    window.addEventListener("hashchange", scheduleUpdate);
    document.addEventListener("toggle", scheduleUpdate, true);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(scheduleUpdate);
    }
    scheduleUpdate();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
