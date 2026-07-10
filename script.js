(() => {
  const portraitUrl = 'https://avatars.githubusercontent.com/u/77919295?v=4';
  const portraitAlt = document.documentElement.lang === 'ru'
    ? 'Портрет Михаила Разакова'
    : 'Portrait of Mikhail Razakov';

  document.querySelectorAll('.identity-mark').forEach((mark) => {
    const image = new Image(460, 460);
    image.alt = portraitAlt;
    image.decoding = 'async';
    image.fetchPriority = 'high';
    image.style.cssText = 'display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;object-position:center;';
    image.addEventListener('load', () => {
      mark.removeAttribute('aria-hidden');
      mark.style.overflow = 'hidden';
      mark.replaceChildren(image);
    }, { once: true });
    image.src = portraitUrl;
  });

  const menu = document.querySelector('.mobile-menu');
  if (!menu) return;
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => menu.removeAttribute('open')));
  document.addEventListener('click', (event) => {
    if (menu.open && !menu.contains(event.target)) menu.removeAttribute('open');
  });
})();
