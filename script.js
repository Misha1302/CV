(() => {
  const githubAvatar = 'https://avatars.githubusercontent.com/u/77919295?v=4&s=460';

  document.querySelectorAll('img.identity-mark, .contact-card img').forEach((image) => {
    const fallback = image.src;
    image.addEventListener('error', () => {
      if (image.src !== fallback) image.src = fallback;
    }, { once: true });
    image.src = githubAvatar;
    image.decoding = 'async';
  });

  const menu = document.querySelector('.mobile-menu');
  if (!menu) return;
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => menu.removeAttribute('open')));
  document.addEventListener('click', (event) => {
    if (menu.open && !menu.contains(event.target)) menu.removeAttribute('open');
  });
})();
