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

  const availabilityReplacements = [
    [/С сентября 2026:\s*до 20 часов в неделю/giu, ''],
    [/до 20 часов в неделю с сентября 2026(?: года)?/giu, ''],
    [/С сентября 2026 открыт к работе/giu, 'Открыт к работе'],
    [/From September 2026:\s*up to 20 hours(?:\/week| per week)/giu, ''],
    [/up to 20 hours(?:\/week| per week) from September 2026/giu, ''],
    [/Available from September 2026 for/giu, 'Open to'],
  ];

  const cleanAvailabilityText = (value) => {
    let result = value;
    availabilityReplacements.forEach(([pattern, replacement]) => {
      result = result.replace(pattern, replacement);
    });
    return result
      .replace(/\s+·\s*(?=[.,;:]|$)/gu, '')
      .replace(/(^|[.!?]\s+)·\s+/gu, '$1')
      .replace(/\s{2,}/gu, ' ')
      .replace(/\s+([.,;:])/gu, '$1')
      .trim();
  };

  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const textNodes = [];
  while (walker.nextNode()) textNodes.push(walker.currentNode);

  textNodes.forEach((node) => {
    const cleaned = cleanAvailabilityText(node.nodeValue ?? '');
    if (cleaned !== (node.nodeValue ?? '').trim()) node.nodeValue = cleaned;
  });

  document.querySelectorAll('.hero-context span, .contact-panel p, .print-cv span, .print-cv p').forEach((element) => {
    if (!element.textContent.trim()) element.remove();
  });

  const menu = document.querySelector('.mobile-menu');
  if (!menu) return;
  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => menu.removeAttribute('open')));
  document.addEventListener('click', (event) => {
    if (menu.open && !menu.contains(event.target)) menu.removeAttribute('open');
  });
})();
