(() => {
  const githubAvatar = 'https://avatars.githubusercontent.com/u/77919295?v=4&s=575';

  document.querySelectorAll('img.identity-mark, .contact-card img').forEach((image) => {
    if (image.dataset.localPhoto === 'true') return;

    const fallback = image.getAttribute('src');

    image.addEventListener('error', () => {
      if (fallback && image.getAttribute('src') !== fallback) {
        image.setAttribute('src', fallback);
      }
    }, { once: true });

    image.setAttribute('src', githubAvatar);
    image.setAttribute('width', '460');
    image.setAttribute('height', '575');
    image.style.width = '100%';
    image.style.height = 'auto';
    image.style.aspectRatio = '4 / 5';
    image.style.objectFit = 'cover';
    image.style.objectPosition = '50% 32%';
    image.decoding = 'async';
  });

  const menu = document.querySelector('.mobile-menu');
  if (!menu) return;
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => menu.removeAttribute('open')));
  document.addEventListener('click', (event) => {
    if (menu.open && !menu.contains(event.target)) menu.removeAttribute('open');
  });
})();
