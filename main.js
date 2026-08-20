const header = document.querySelector("[data-header]");
const menuToggle = document.querySelector("[data-menu-toggle]");
const mobileMenu = document.querySelector("[data-mobile-menu]");
const heroVideo = document.querySelector("[data-hero-video]");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const caseImage = document.querySelector("[data-case-image]");
const bottomCtaImage = document.querySelector("[data-bottom-cta-image]");

document.documentElement.classList.add("motion-ready");

caseImage?.addEventListener("error", () => {
  caseImage.classList.add("is-missing");
});

if (caseImage?.complete && !caseImage.naturalWidth) {
  caseImage.classList.add("is-missing");
}

bottomCtaImage?.addEventListener("error", () => {
  bottomCtaImage.classList.add("is-missing");
  bottomCtaImage.parentElement?.classList.remove("has-image");
});

const syncBottomCtaImage = () => {
  if (!bottomCtaImage) return;
  const hasImage = bottomCtaImage.complete && bottomCtaImage.naturalWidth > 0;
  bottomCtaImage.classList.toggle("is-missing", bottomCtaImage.complete && !hasImage);
  bottomCtaImage.parentElement?.classList.toggle("has-image", hasImage);
};

bottomCtaImage?.addEventListener("load", syncBottomCtaImage);

if (bottomCtaImage?.complete) {
  syncBottomCtaImage();
}

const syncHeader = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 20);
};

const closeMenu = () => {
  if (!menuToggle || !mobileMenu) return;
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "打开导航菜单");
  mobileMenu.hidden = true;
};

menuToggle?.addEventListener("click", () => {
  const willOpen = menuToggle.getAttribute("aria-expanded") !== "true";
  menuToggle.setAttribute("aria-expanded", String(willOpen));
  menuToggle.setAttribute("aria-label", willOpen ? "关闭导航菜单" : "打开导航菜单");
  mobileMenu.hidden = !willOpen;
});

mobileMenu?.addEventListener("click", (event) => {
  if (event.target.closest("a")) closeMenu();
});

window.addEventListener("scroll", syncHeader, { passive: true });
window.addEventListener("resize", () => {
  if (window.innerWidth > 900) closeMenu();
});

syncHeader();

if (heroVideo) {
  const syncVideoSourceMode = () => {
    heroVideo.classList.toggle("uses-solid-background", heroVideo.currentSrc.endsWith(".mp4"));
  };

  const syncVideoPlayback = () => {
    if (reducedMotion.matches) {
      heroVideo.pause();
      return;
    }

    if (document.visibilityState === "visible") {
      heroVideo.play().catch(() => {});
    } else {
      heroVideo.pause();
    }
  };

  const videoObserver = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting && !reducedMotion.matches && document.visibilityState === "visible") {
        heroVideo.play().catch(() => {});
      } else {
        heroVideo.pause();
      }
    },
    { threshold: 0.08 },
  );

  videoObserver.observe(heroVideo);
  heroVideo.addEventListener("loadedmetadata", syncVideoSourceMode);
  reducedMotion.addEventListener("change", syncVideoPlayback);
  document.addEventListener("visibilitychange", syncVideoPlayback);
  syncVideoSourceMode();
  syncVideoPlayback();
}

const motionGroups = [
  [".hero__copy > *", ".agent-pill"],
  [".key-metrics", ".metric-card"],
  [".management-problems", ".management-problems h2, .problem-card"],
  [".platform-architecture", ".platform-architecture h2, .architecture-hub, .architecture-layer"],
  [".intelligent-modules", ".intelligent-modules h2, .module-card"],
  [".case-study", ".case-study h2, .case-panel__media, .case-panel__header, .case-metric, .case-timeline"],
  [".whitepapers", ".whitepapers__header, .whitepapers__book, .whitepaper-card"],
  [".bottom-cta", ".bottom-cta__copy, .bottom-cta__visual"],
  [".site-footer", ".site-footer__brand, .site-footer__nav > div"],
];

motionGroups.forEach(([sectionSelector, itemSelector]) => {
  const section = document.querySelector(sectionSelector);
  if (!section) return;

  section.querySelectorAll(itemSelector).forEach((item, index) => {
    item.classList.add("reveal-item");
    item.style.setProperty("--reveal-delay", `${Math.min(index, 6) * 80}ms`);
  });
});

const animateMetric = (element) => {
  if (element.dataset.counted === "true") return;
  const textNode = [...element.childNodes].find((node) => node.nodeType === Node.TEXT_NODE);
  const target = Number.parseFloat(textNode?.textContent.trim() || "");
  if (!textNode || !Number.isFinite(target)) return;

  element.dataset.counted = "true";
  const decimals = target % 1 === 0 ? 0 : 1;
  const start = performance.now();
  const duration = 1100;

  const tick = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    textNode.textContent = (target * eased).toFixed(decimals);
    if (progress < 1) requestAnimationFrame(tick);
  };

  requestAnimationFrame(tick);
};

const revealSection = (section) => {
  section.classList.add("is-revealed");
  section.querySelectorAll(".metric-card__value").forEach(animateMetric);
};

if (reducedMotion.matches || !("IntersectionObserver" in window)) {
  motionGroups.forEach(([sectionSelector]) => {
    const section = document.querySelector(sectionSelector);
    if (section) revealSection(section);
  });
} else {
  const motionObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        revealSection(entry.target);
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -7%" },
  );

  motionGroups.forEach(([sectionSelector]) => {
    const section = document.querySelector(sectionSelector);
    if (section) motionObserver.observe(section);
  });
}
