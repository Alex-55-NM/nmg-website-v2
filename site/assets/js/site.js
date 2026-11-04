/* Next Mind Group website v2: brief builder on the contact page, menu closing. */
(function () {
  'use strict';

  // Close the mobile menu after choosing a link or pressing Escape.
  var menu = document.querySelector('details.menu');
  if (menu) {
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) menu.removeAttribute('open'); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.open) { menu.removeAttribute('open'); menu.querySelector('summary').focus(); }
    });
  }

  var form = document.getElementById('brief-form');
  if (!form) return;
  var briefBox = document.getElementById('brief');
  var briefText = document.getElementById('brief-text');
  var status = document.getElementById('copy-status');

  // Preselect the service when arriving from a service page (?service=slug).
  var wanted = new URLSearchParams(location.search).get('service');
  if (wanted) {
    var radio = form.querySelector('input[name="service"][value="' + wanted.replace(/[^a-z-]/g, '') + '"]');
    if (radio) radio.checked = true;
  }

  // Words used in the brief and status messages, in the page language.
  var T = {
    en: { title: 'Next Mind Group: project brief', need: 'Need: ', result: 'Result needed:', have: 'What already exists:',
          when: 'When: ', name: 'Name: ', company: 'Company and country: ', none: 'Not stated', on: 'Prepared on ',
          copied: 'Brief copied.', blocked: 'Copying is blocked in this browser. Select the text and copy it.',
          downloaded: 'Brief downloaded.', file: 'next-mind-project-brief.txt' },
    it: { title: 'Next Mind Group: brief di progetto', need: 'Esigenza: ', result: 'Risultato richiesto:', have: 'Cosa esiste già:',
          when: 'Quando: ', name: 'Nome: ', company: 'Azienda e Paese: ', none: 'Non indicato', on: 'Preparato il ',
          copied: 'Brief copiato.', blocked: 'Questo browser blocca la copia. Selezionate il testo e copiatelo.',
          downloaded: 'Brief scaricato.', file: 'next-mind-brief-di-progetto.txt' }
  };
  var t = T[(document.documentElement.lang || 'en').slice(0, 2)] || T.en;

  function show(id, on) { var el = document.getElementById(id); if (el) el.hidden = !on; }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var service = form.querySelector('input[name="service"]:checked');
    var result = form.result.value.trim();
    show('err-service', !service);
    show('err-result', !result);
    if (!service) { form.querySelector('input[name="service"]').focus(); return; }
    if (!result) { form.result.focus(); return; }
    var label = service.parentNode.textContent.trim();
    var lines = [
      t.title,
      '',
      t.need + label,
      '',
      t.result,
      result,
      '',
      t.have,
      form.have.value.trim() || t.none,
      '',
      t.when + (form.when.value || t.none),
      t.name + (form.name.value.trim() || t.none),
      t.company + (form.company.value.trim() || t.none),
      '',
      t.on + new Date().toISOString().slice(0, 10)
    ];
    briefText.textContent = lines.join('\n');
    form.hidden = true;
    briefBox.hidden = false;
    status.textContent = '';
    briefBox.focus();
  });

  document.getElementById('edit-brief').addEventListener('click', function () {
    briefBox.hidden = true; form.hidden = false; form.result.focus();
  });

  document.getElementById('copy-brief').addEventListener('click', function () {
    var text = briefText.textContent;
    var done = function () { status.textContent = t.copied; };
    var fail = function () { status.textContent = t.blocked; };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, fail);
    else fail();
  });

  document.getElementById('download-brief').addEventListener('click', function () {
    var blob = new Blob([briefText.textContent], { type: 'text/plain' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = t.file;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    status.textContent = t.downloaded;
  });
})();
