(() => {
  const portraitUrl = 'https://avatars.githubusercontent.com/u/77919295?v=4';
  const isRussian = document.documentElement.lang === 'ru';
  const portraitAlt = isRussian ? 'Портрет Михаила Разакова' : 'Portrait of Mikhail Razakov';

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
    [/С сентября 2026 открыт к работе(?: с неполной занятостью)?/giu, 'Открыт к работе'],
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

  const setText = (selector, text) => {
    const element = document.querySelector(selector);
    if (element) element.textContent = text;
  };

  const setProof = (index, title, body) => {
    const item = document.querySelectorAll('.proof-item')[index];
    if (!item) return;
    const heading = item.querySelector('strong');
    const description = item.querySelector('span');
    if (heading) heading.textContent = title;
    if (description) description.textContent = body;
  };

  const setCareer = (index, title, body) => {
    const item = document.querySelectorAll('.career-item')[index];
    if (!item) return;
    const heading = item.querySelector('strong');
    const description = item.querySelector('span');
    if (heading) heading.textContent = title;
    if (description) description.textContent = body;
  };

  const applyCompilerProfile = () => {
    setText('.brand-copy span', 'компиляторы · .NET-платформы · backend');
    setText('.hero .eyebrow', 'Архитектура языковых платформ · runtime / SSA · надёжные backend-системы');
    setText('.hero-role', 'Инженер по компиляторам и .NET-платформам');
    setText('.hero-summary', 'Проектирую платформенные системы с явными контрактами, инвариантами и проверяемым поведением. Создал UniversalToolchain/Wist2 — модульный .NET SDK для композиции языков и сред исполнения; разрабатываю SSA с семантикой вызовов, интерпретатор/CIL и PlanFuzz. Практически работал с .NET backend-сервисами: платежами, подписками, ролями, устройствами, миграциями, восстановлением после сбоев и проверяемыми релизами.');
    setText('.identity-card strong', 'Архитектура языковых платформ, .NET runtime и надёжных backend-систем');
    setText('.identity-card span', 'контракты · инварианты · fail-closed · SSA · interpreter/CIL · recovery');

    setProof(0, 'Архитектура платформы', 'Независимые пакеты, типизированные артефакты, графы возможностей и конфликтов, детерминированные маршруты и lock-идентичность.');
    setProof(1, '.NET и эксплуатация', 'ASP.NET Core, PostgreSQL/SQLite, платежные состояния, идемпотентность, миграции, backup/restore, Docker, nginx и systemd.');
    setProof(2, 'Компиляторная глубина', 'Callable-first SSA, CFG и доминирование, interpreter/CIL parity, LLVM, анализ программ и x86-64 codegen.');

    setCareer(0, 'UniversalToolchain', 'Архитектура модульной .NET-платформы: контракты, маршруты, manifests/locks и lifecycle ownership.');
    setCareer(1, '.NET backend', 'Платежи, подписки, роли, устройства, webhooks, состояние данных, recovery и проверяемые релизы.');
    setCareer(2, 'Compiler runtime', 'Callable-first SSA, оптимизации, интерпретатор/CIL и типизированные делегаты.');
    setCareer(3, 'LLVM / systems', 'C++23, оптимизационный проход, анализ программ и генерация x86-64.');

    const headings = document.querySelectorAll('.section-heading');
    if (headings[0]) {
      const h2 = headings[0].querySelector('h2');
      const intro = headings[0].querySelector('.section-intro');
      if (h2) h2.textContent = 'Архитектура платформ, компиляторы и надёжные backend-системы.';
      if (intro) intro.textContent = 'Основная работа — UniversalToolchain/Wist2; production-опыт дополняют .NET-сервисы с платежами, состоянием, восстановлением и ответственностью за релиз.';
    }
    if (headings[2]) {
      const h2 = headings[2].querySelector('h2');
      if (h2) h2.textContent = 'Платформенная архитектура, .NET backend и compiler engineering.';
    }

    const stack = document.querySelectorAll('.stack-line');
    if (stack[3]) {
      const heading = stack[3].querySelector('strong');
      const body = stack[3].querySelector('p');
      if (heading) heading.textContent = 'Runtime и backend';
      if (body) body.textContent = 'Интерпретатор/CIL, типизированные делегаты, ASP.NET Core, REST/OpenAPI, PostgreSQL/SQLite, payments/webhooks, lifecycle, recovery и fail-closed политики';
    }

    setText('.print-cv .pcv-header h2', 'Инженер по компиляторам и .NET-платформам');
    setText('.print-cv .pcv-summary', 'Проектирую платформенные системы с явными контрактами и инвариантами: UniversalToolchain/Wist2, callable-first SSA, interpreter/CIL и PlanFuzz; дополнительно — .NET backend с платежами, состоянием, миграциями, recovery и проверяемыми релизами.');
    const printProofs = document.querySelectorAll('.print-cv .pcv-proof');
    const proofValues = [
      ['Архитектура платформы', 'контракты, маршруты, manifests/locks и lifecycle ownership'],
      ['.NET backend и recovery', 'платежи, состояния, миграции, backup/restore и rollback'],
      ['Компиляторная глубина', 'SSA, interpreter/CIL, LLVM, анализ программ и x86-64'],
    ];
    printProofs.forEach((proof, index) => {
      if (!proofValues[index]) return;
      const heading = proof.querySelector('strong');
      const body = proof.querySelector('span');
      if (heading) heading.textContent = proofValues[index][0];
      if (body) body.textContent = proofValues[index][1];
    });
  };

  const applyBackendProfile = () => {
    setText('.hero-role', '.NET Backend Engineer · надёжные системы');
    setText('.identity-card strong', 'Backend с ответственностью за состояние, recovery и безопасные релизы');
    setText('.print-cv .pcv-header h2', '.NET Backend Engineer · надёжные системы');
  };

  const path = window.location.pathname;
  if (path.endsWith('/ru-compiler.html') || path.endsWith('ru-compiler.html')) applyCompilerProfile();
  if (path.endsWith('/ru-backend.html') || path.endsWith('ru-backend.html') || path.endsWith('/ru-platform.html') || path.endsWith('ru-platform.html')) applyBackendProfile();

  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const textNodes = [];
  while (walker.nextNode()) textNodes.push(walker.currentNode);
  textNodes.forEach((node) => {
    const original = node.nodeValue ?? '';
    const cleaned = cleanAvailabilityText(original);
    if (cleaned !== original.trim()) node.nodeValue = cleaned;
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
