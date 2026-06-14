const navLinks = [...document.querySelectorAll('[data-nav]')];
const sections = navLinks
  .map((link) => document.querySelector(link.getAttribute('href')))
  .filter(Boolean);

if (window.matchMedia('(min-width: 1081px)').matches && 'IntersectionObserver' in window && navLinks.length > 0) {
  const observer = new IntersectionObserver((entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) {
      return;
    }

    for (const link of navLinks) {
      link.classList.toggle('is-active', link.getAttribute('href') === `#${visible.target.id}`);
    }
  }, { rootMargin: '-20% 0px -65% 0px', threshold: [0.05, 0.2, 0.5] });

  for (const section of sections) {
    observer.observe(section);
  }
}

const mobileMenu = document.querySelector('.mobile-menu');
if (mobileMenu) {
  for (const link of mobileMenu.querySelectorAll('a[href^="#"]')) {
    link.addEventListener('click', () => mobileMenu.removeAttribute('open'));
  }

  document.addEventListener('click', (event) => {
    if (mobileMenu.open && !mobileMenu.contains(event.target)) {
      mobileMenu.removeAttribute('open');
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      mobileMenu.removeAttribute('open');
    }
  });
}
