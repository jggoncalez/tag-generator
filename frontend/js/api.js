function getApi() {
  return new Promise((resolve, reject) => {
    if (window.pywebview && window.pywebview.api) {
      resolve(window.pywebview.api); return;
    }
    let tries = 0;
    const interval = setInterval(() => {
      if (window.pywebview && window.pywebview.api) {
        clearInterval(interval);
        resolve(window.pywebview.api);
      } else if (++tries > 60) {
        clearInterval(interval);
        reject(new Error('API não disponível'));
      }
    }, 100);
  });
}
