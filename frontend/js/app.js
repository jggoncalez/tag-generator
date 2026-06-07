let count = 0;
let lastCodigo = '';

async function gerar() {
  const nome = document.getElementById('nome-input').value.trim();
  if (!nome) {
    setStatus('⚠ Insira o nome do produto.', 'error');
    document.getElementById('nome-input').focus();
    return;
  }

  const btn = document.getElementById('gerar-btn');
  btn.classList.add('loading');
  btn.disabled = true;
  setStatus('');

  try {
    const api = await getApi();
    const res = await api.gerar_etiqueta(nome);

    if (res.sucesso) {
      document.getElementById('result-nome').textContent = res.nome;
      document.getElementById('result-code').textContent = res.codigo;
      document.getElementById('qr-img').src = res.qr_b64;
      lastCodigo = res.codigo;

      document.getElementById('divider').style.display = 'block';
      const resultEl = document.getElementById('result');
      resultEl.classList.remove('visible');
      void resultEl.offsetWidth;
      resultEl.classList.add('visible');

      count++;
      document.getElementById('counter').textContent = count;
      setStatus('✓ Etiqueta salva em Docs/', 'ok');
    } else {
      setStatus('✗ ' + res.erro, 'error');
    }
  } catch (e) {
    setStatus('✗ ' + e.message, 'error');
  } finally {
    btn.classList.remove('loading');
    btn.disabled = false;
  }
}
