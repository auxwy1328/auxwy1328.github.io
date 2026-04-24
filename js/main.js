window.addEventListener('DOMContentLoaded', function() {
  // Progress bar & back-to-top
  window.addEventListener('scroll', function() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var p = (window.scrollY / h) * 100;
    var prog = document.getElementById('prog');
    var btt = document.getElementById('btt');
    if (prog) prog.style.width = Math.min(p, 100) + '%';
    if (btt) btt.style.display = window.scrollY > 400 ? 'flex' : 'none';
  });

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function(q) {
    q.addEventListener('click', function() {
      var item = q.parentElement;
      var isOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.faq-item.open').forEach(function(i) {
        i.classList.remove('open');
      });
      if (!isOpen) item.classList.add('open');
    });
  });

  // Mobile menu toggle
  var mobBtn = document.querySelector('.mob-menu');
  var navEl = document.querySelector('.nav');
  if (mobBtn && navEl) {
    mobBtn.addEventListener('click', function() {
      if (navEl.style.display === 'flex') {
        navEl.style.display = 'none';
      } else {
        navEl.style.display = 'flex';
        navEl.style.flexDirection = 'column';
        navEl.style.position = 'absolute';
        navEl.style.top = '60px';
        navEl.style.left = '0';
        navEl.style.right = '0';
        navEl.style.background = 'rgba(9,11,17,.95)';
        navEl.style.padding = '16px';
        navEl.style.borderBottom = '1px solid var(--border)';
      }
    });
  }
});
