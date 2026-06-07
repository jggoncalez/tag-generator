function setStatus(msg, type) {
  const el = document.getElementById('status');
  el.textContent = msg;
  el.className = 'status ' + (type || '');
}

function copiar() {
  if (!lastCodigo) return;

  // Cria textarea invisível, seleciona e copia — sem pedir permissão
  const ta = document.createElement('textarea');
  ta.value = lastCodigo;
  ta.style.cssText = 'position:fixed;opacity:0;pointer-events:none';
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);

  const btn = document.querySelector('.copy-btn');
  btn.textContent = 'COPIADO';
  setTimeout(() => btn.textContent = 'COPIAR', 1500);
}
