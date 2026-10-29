/* Progressive enhancements: the complete homepage also works without this file. */
(function () {
  'use strict';
  if (!document.body.classList.contains('homepage')) return;

  // The theme's 400 ms jQuery scrolling ignores sticky-header scroll margins,
  // native fragment focus, and reduced-motion preferences. Use native anchors.
  if (window.jQuery) window.jQuery(function () {
    window.jQuery('.homepage a').off('click.smoothscroll');
  });

  // Fragment links stay in this tab despite the site's external-link base target.
  document.querySelectorAll('a[href^="#"], a[href^="/#"]').forEach(function (link) {
    link.setAttribute('target', '_self');
  });

  var groups = Array.from(document.querySelectorAll('.publication-group'));
  var filters = document.querySelector('.publication-filters');
  if (filters && groups.length) {
    filters.hidden = false;
    filters.addEventListener('click', function (event) {
      var button = event.target.closest('button[data-publication-filter]');
      if (!button) return;
      var topic = button.dataset.publicationFilter;
      filters.querySelectorAll('button').forEach(function (item) {
        item.setAttribute('aria-pressed', item === button ? 'true' : 'false');
      });
      var count = 0;
      groups.forEach(function (group) {
        group.hidden = topic !== 'all' && group.dataset.publicationTopic !== topic;
        if (!group.hidden) count += group.querySelectorAll('.paper-box').length;
      });
      var status = document.getElementById('publication-status');
      if (status) status.textContent = count + ' publications shown.';
    });
  }

  // Keep full abstract text in the document, with a native keyboard disclosure.
  document.querySelectorAll('.paper-box-text li').forEach(function (item) {
    var label = item.querySelector('strong');
    if (!label || label.textContent.trim() !== 'Abstract') return;
    var details = document.createElement('details');
    details.className = 'paper-abstract';
    var summary = document.createElement('summary');
    summary.textContent = 'Abstract';
    var body = document.createElement('div');
    body.className = 'paper-abstract__body';
    label.remove();
    var first = item.firstChild;
    if (first && first.nodeType === 3) first.textContent = first.textContent.replace(/^\s*:\s*/, '');
    while (item.firstChild) body.appendChild(item.firstChild);
    details.appendChild(summary);
    details.appendChild(body);
    var list = item.parentElement;
    list.parentElement.insertBefore(details, list);
    item.remove();
    if (!list.children.length) list.remove();
  });

  // A compact date column preserves the original news wording and links.
  document.querySelectorAll('.home-section--news > ul > li').forEach(function (item) {
    var date = item.querySelector('em');
    if (!date) return;
    var time = document.createElement('time');
    time.dateTime = date.textContent.trim().replace('.', '-');
    time.textContent = date.textContent;
    date.remove();
    if (item.firstChild && item.firstChild.nodeType === 3) {
      item.firstChild.textContent = item.firstChild.textContent.replace(/^\s*:\s*/, '');
    }
    var entry = document.createElement('div');
    while (item.firstChild) entry.appendChild(item.firstChild);
    item.appendChild(time);
    item.appendChild(entry);
    item.classList.add('news-item');
  });

  var nav = document.getElementById('site-nav');
  var menu = document.getElementById('navigation-overflow');
  var menuButton = nav && nav.querySelector('button');
  if (menu && menuButton) {
    function syncMenuState() {
      menuButton.setAttribute('aria-expanded', menu.classList.contains('hidden') ? 'false' : 'true');
    }
    new MutationObserver(syncMenuState).observe(menu, { attributes: true, attributeFilter: ['class'] });
    syncMenuState();
    nav.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !menu.classList.contains('hidden')) {
        menu.classList.add('hidden');
        menuButton.classList.remove('close');
        menuButton.focus();
      }
    });
    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        menu.classList.add('hidden');
        menuButton.classList.remove('close');
      }
    });
  }

  var sections = Array.from(document.querySelectorAll('.home-section'));
  var topLink = document.querySelector('.back-to-top');
  var ticking = false;
  function updatePosition() {
    var current = 'about-me';
    sections.forEach(function (section) {
      var heading = section.querySelector('h1[id]');
      if (heading && heading.getBoundingClientRect().top <= 150) current = heading.id;
    });
    if (nav) nav.querySelectorAll('a').forEach(function (link) {
      var fragment = link.getAttribute('href').split('#')[1];
      if (fragment === current && !link.closest('.masthead__menu-home-item')) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    if (topLink) topLink.hidden = window.scrollY < 650;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(updatePosition); ticking = true; }
  }, { passive: true });
  updatePosition();

  // Print the complete publication list, including disclosed abstracts.
  var openBeforePrint = [];
  window.addEventListener('beforeprint', function () {
    openBeforePrint = Array.from(document.querySelectorAll('.paper-abstract')).map(function (details) {
      var previous = details.open;
      details.open = true;
      return previous;
    });
  });
  window.addEventListener('afterprint', function () {
    document.querySelectorAll('.paper-abstract').forEach(function (details, index) {
      details.open = openBeforePrint[index] || false;
    });
  });
}());
