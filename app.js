(() => {
  'use strict';
  const P = window.PUZZLO_PRODUCTS;
  const byId = Object.fromEntries(P.map(p => [p.id, p]));
  const $ = s => document.querySelector(s);

  const T = {
    en: {
      skip: 'Skip to content',
      preview: 'Preview store: sample products and placeholder prices. Checkout isn’t connected yet.',
      navShop: 'Shop', navStory: 'Our story', navGifts: 'Gifts', bag: 'Bag',
      tagline: 'Make room for wonder.',
      heroTitle: 'Watch wonder <em>come together.</em>',
      heroLede: 'Illustrated jigsaws of Gulf places and stories, and metal teasers that reward patience. Made for slow evenings and shared tables.',
      heroCta: 'Find your next puzzle',
      videoDesc: 'One hundred interlocking pieces move into place to reveal an illustrated Arabian coastline: a dhow at sunset, wind towers on the shore and palms on the beach.',
      pause: 'Pause video', play: 'Play video',
      shopTitle: 'Find your next <em>puzzle</em>',
      fAll: 'All', fPlaces: 'Places & Stories', fMetal: 'Metal Challenges', fTogether: 'Time Together',
      cat: { places: 'Places & Stories', metal: 'Metal Challenges', together: 'Time Together' },
      showing: n => `Showing ${n} ${n === 1 ? 'product' : 'products'}`,
      storyEyebrow: 'Why we make puzzles',
      storyTitle: 'Small pieces, <em>big quiet.</em>',
      storyP: 'Puzzlo began with a simple wish: to put down the phone and pick up something that rewards attention. Every picture we make starts from a place on the Gulf coast we love, then becomes a hundred, five hundred, a thousand small decisions.',
      p1t: 'Curiosity', p1d: 'A corner of sky, a coral door. You start anywhere and keep looking.',
      p2t: 'Discovery', p2d: 'That small click when a piece fits, or a ring finally slips free.',
      p3t: 'Shared time', p3d: 'One table, a pot of tea, and everyone pointing at the same edge.',
      giftsTitle: 'Give an evening, <em>not just a gift.</em>',
      giftsLede: 'A puzzle is time you hand to someone. Choose by the person, not the piece count.',
      g1k: 'For the one who loves a challenge', g1t: 'Metal Challenges',
      g2k: 'For someone who misses home', g2t: 'Places & Stories',
      g3k: 'For the whole family', g3t: 'Time Together', gLink: 'See the edit',
      footNote: 'Serving the UAE and Saudi Arabia. Prices in SAR. Online checkout isn’t connected yet.',
      bagTitle: 'Your bag', close: 'Close',
      bagEmpty: 'Your bag is empty. Something curious is waiting in the shop.',
      savedTitle: 'Saved for later', items: 'Items', subtotal: 'Subtotal', checkout: 'Checkout',
      checkoutNote: 'Checkout isn’t connected yet, so orders can’t be placed on this site.',
      less: 'Decrease quantity', more: 'Increase quantity',
      addToBag: 'Add to bag', details: 'Details', save: 'Save for later', saved: 'Saved', unsave: 'Remove from saved',
      remove: 'Remove', moveToBag: 'Move to bag', saveForLater: 'Save for later',
      added: n => `Added to bag: ${n}`, savedToast: n => `Saved for later: ${n}`,
      qtyOf: n => `Quantity for ${n}`, each: 'each'
    },
    ar: {
      skip: 'انتقل إلى المحتوى',
      preview: 'متجر تجريبي: منتجات نموذجية وأسعار مؤقتة. الدفع الإلكتروني غير مفعّل بعد.',
      navShop: 'المتجر', navStory: 'قصتنا', navGifts: 'الهدايا', bag: 'الحقيبة',
      tagline: 'أفسِح مكاناً للدهشة.',
      heroTitle: 'شاهد الدهشة <em>تكتمل.</em>',
      heroLede: 'ألغاز صور مرسومة لأماكن وحكايات من الخليج، وألغاز معدنية تكافئ الصبر. لأمسيات هادئة وطاولات مشتركة.',
      heroCta: 'اعثر على لغزك القادم',
      videoDesc: 'مئة قطعة متشابكة تأخذ أماكنها لتكشف ساحلاً عربياً مرسوماً: مركب شراعي عند الغروب، وأبراج هواء على الشاطئ، ونخيل على الرمل.',
      pause: 'إيقاف الفيديو مؤقتاً', play: 'تشغيل الفيديو',
      shopTitle: 'اعثر على <em>لغزك</em> القادم',
      fAll: 'الكل', fPlaces: 'أماكن وحكايات', fMetal: 'تحديات معدنية', fTogether: 'وقت معاً',
      cat: { places: 'أماكن وحكايات', metal: 'تحديات معدنية', together: 'وقت معاً' },
      showing: n => `يُعرض ${n} من المنتجات`,
      storyEyebrow: 'لماذا نصنع الألغاز',
      storyTitle: 'قطع صغيرة، <em>وهدوء كبير.</em>',
      storyP: 'بدأت Puzzlo بأمنية بسيطة: أن نضع الهاتف جانباً ونمسك شيئاً يكافئ الانتباه. كل صورة نرسمها تبدأ من مكان نحبه على ساحل الخليج، ثم تصبح مئة، وخمسمئة، وألف قرار صغير.',
      p1t: 'الفضول', p1d: 'زاوية من السماء، أو باب مرجاني. تبدأ من أي مكان وتواصل النظر.',
      p2t: 'الاكتشاف', p2d: 'تلك النقرة الصغيرة حين تستقر القطعة، أو حين تنفلت الحلقة أخيراً.',
      p3t: 'وقت مشترك', p3d: 'طاولة واحدة، وإبريق شاي، والجميع يشير إلى الحافة نفسها.',
      giftsTitle: 'أهدِ أمسية، <em>لا مجرد هدية.</em>',
      giftsLede: 'اللغز وقتٌ تقدّمه لشخص ما. اختر حسب الشخص، لا حسب عدد القطع.',
      g1k: 'لمن يحب التحدي', g1t: 'تحديات معدنية',
      g2k: 'لمن يشتاق إلى الديار', g2t: 'أماكن وحكايات',
      g3k: 'للعائلة كلها', g3t: 'وقت معاً', gLink: 'تصفّح المجموعة',
      footNote: 'نخدم الإمارات والسعودية. الأسعار بالريال السعودي. الدفع الإلكتروني غير مفعّل بعد.',
      bagTitle: 'حقيبتك', close: 'إغلاق',
      bagEmpty: 'حقيبتك فارغة. شيء مثير للفضول ينتظرك في المتجر.',
      savedTitle: 'محفوظ لوقت لاحق', items: 'القطع', subtotal: 'المجموع', checkout: 'إتمام الطلب',
      checkoutNote: 'الدفع غير مفعّل بعد، لذلك لا يمكن تقديم الطلبات عبر هذا الموقع.',
      less: 'إنقاص الكمية', more: 'زيادة الكمية',
      addToBag: 'أضف إلى الحقيبة', details: 'التفاصيل', save: 'احفظ لوقت لاحق', saved: 'محفوظ', unsave: 'إزالة من المحفوظات',
      remove: 'إزالة', moveToBag: 'انقل إلى الحقيبة', saveForLater: 'احفظ لوقت لاحق',
      added: n => `أُضيف إلى الحقيبة: ${n}`, savedToast: n => `حُفظ لوقت لاحق: ${n}`,
      qtyOf: n => `الكمية: ${n}`, each: 'للقطعة'
    }
  };

  // ---------- state ----------
  const store = {
    get(k, d) { try { const v = localStorage.getItem('puzzlo.' + k); return v ? JSON.parse(v) : d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem('puzzlo.' + k, JSON.stringify(v)); } catch { /* storage unavailable */ } }
  };
  let lang = store.get('lang', (navigator.language || '').toLowerCase().startsWith('ar') ? 'ar' : 'en');
  let filter = 'all';
  let bag = store.get('bag', []).filter(l => byId[l.id] && l.qty > 0);      // [{id, qty}]
  let saved = store.get('saved', []).filter(id => byId[id]);                 // [id]
  const persist = () => { store.set('bag', bag); store.set('saved', saved); };
  const t = k => T[lang][k];
  const name = p => p[lang].name;

  const money = n => {
    const num = new Intl.NumberFormat(lang === 'ar' ? 'ar-SA-u-nu-latn' : 'en-US', { maximumFractionDigits: 2 }).format(n);
    return lang === 'ar' ? `${num} ر.س` : `SAR ${num}`;
  };
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  // ---------- language ----------
  function applyLang() {
    const html = document.documentElement;
    html.lang = lang; html.dir = lang === 'ar' ? 'rtl' : 'ltr';
    document.querySelectorAll('[data-i18n]').forEach(el => { const v = t(el.dataset.i18n); if (typeof v === 'string') el.textContent = v; });
    document.querySelectorAll('[data-i18n-html]').forEach(el => { el.innerHTML = t(el.dataset.i18nHtml); });
    const lt = $('#langToggle');
    lt.textContent = lang === 'ar' ? 'English' : 'عربي';
    lt.lang = lang === 'ar' ? 'en' : 'ar';
    lt.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
    document.title = lang === 'ar' ? 'Puzzlo — أفسِح مكاناً للدهشة' : 'Puzzlo — Make room for wonder';
    syncVideoLabel();
    renderGrid(); renderBag();
    if (dialog.open && current) fillDialog(current);
  }
  $('#langToggle').addEventListener('click', () => { lang = lang === 'ar' ? 'en' : 'ar'; store.set('lang', lang); applyLang(); });

  // ---------- products ----------
  const grid = $('#productGrid');
  function renderGrid() {
    const list = P.filter(p => filter === 'all' || p.cat === filter);
    grid.innerHTML = list.map(p => {
      const d = p[lang]; const isSaved = saved.includes(p.id);
      return `<li class="card">
        <button type="button" class="card-media" data-open="${p.id}" aria-label="${esc(t('details'))}: ${esc(d.name)}">
          <img src="${p.img}" alt="" loading="lazy" width="1000" height="1250">
        </button>
        <div class="card-body">
          <p class="card-cat">${esc(t('cat')[p.cat])}</p>
          <h3 class="card-name"><button type="button" data-open="${p.id}">${esc(d.name)}</button></h3>
          <p class="card-line">${esc(d.line)}</p>
          <p class="card-spec">${esc(d.specs.map(s => s[1]).join(' · '))}</p>
          <div class="card-foot">
            <span class="price">${money(p.price)}</span>
            <div class="card-actions">
              <button type="button" class="save-btn" data-save="${p.id}" aria-pressed="${isSaved}" aria-label="${esc(isSaved ? t('unsave') : t('save'))}: ${esc(d.name)}">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4h10v16l-5-3.6L7 20V4Z"/></svg>
              </button>
              <button type="button" class="btn btn-small" data-add="${p.id}">${esc(t('addToBag'))}</button>
            </div>
          </div>
        </div>
      </li>`;
    }).join('');
    $('#filterStatus').textContent = t('showing')(list.length);
  }
  $('#filters').addEventListener('click', e => {
    const b = e.target.closest('[data-filter]'); if (!b) return;
    setFilter(b.dataset.filter);
  });
  function setFilter(f) {
    filter = f;
    document.querySelectorAll('[data-filter]').forEach(x => x.setAttribute('aria-pressed', String(x.dataset.filter === f)));
    renderGrid();
  }
  document.querySelectorAll('[data-goto]').forEach(b => b.addEventListener('click', () => {
    setFilter(b.dataset.goto);
    $('#shop').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    $(`[data-filter="${b.dataset.goto}"]`).focus({ preventScroll: true });
  }));
  grid.addEventListener('click', e => {
    const o = e.target.closest('[data-open]'); if (o) return openProduct(o.dataset.open, o);
    const a = e.target.closest('[data-add]'); if (a) { addToBag(a.dataset.add, 1); return; }
    const s = e.target.closest('[data-save]'); if (s) { toggleSaved(s.dataset.save); }
  });

  // ---------- bag ----------
  function addToBag(id, qty) {
    const line = bag.find(l => l.id === id);
    if (line) line.qty = Math.min(99, line.qty + qty); else bag.push({ id, qty: Math.min(99, qty) });
    saved = saved.filter(x => x !== id);
    persist(); renderBag(); renderGrid(); toast(t('added')(name(byId[id])));
    bump();
  }
  function setQty(id, qty) {
    if (qty <= 0) bag = bag.filter(l => l.id !== id);
    else { const l = bag.find(x => x.id === id); if (l) l.qty = Math.min(99, qty); }
    persist(); renderBag();
  }
  function toggleSaved(id) {
    if (saved.includes(id)) saved = saved.filter(x => x !== id);
    else { saved.push(id); toast(t('savedToast')(name(byId[id]))); }
    persist(); renderGrid(); renderBag();
    if (dialog.open && current === id) fillDialog(id);
  }
  function saveForLater(id) {
    bag = bag.filter(l => l.id !== id);
    if (!saved.includes(id)) saved.push(id);
    persist(); renderBag(); renderGrid();
  }
  const totals = () => bag.reduce((a, l) => ({ items: a.items + l.qty, sub: a.sub + l.qty * byId[l.id].price }), { items: 0, sub: 0 });

  function renderBag() {
    const { items, sub } = totals();
    $('#bagCount').textContent = items;
    $('#bagCount').classList.toggle('has', items > 0);
    $('#bagOpen').setAttribute('aria-label', `${t('bag')}, ${items}`);
    $('#bagItems').textContent = items;
    $('#bagSubtotal').textContent = money(sub);
    $('#bagEmpty').hidden = bag.length > 0;
    $('#bagList').innerHTML = bag.map(l => {
      const p = byId[l.id], d = p[lang];
      return `<li class="line">
        <img src="${p.img}" alt="" width="80" height="100" loading="lazy">
        <div class="line-info">
          <p class="line-name">${esc(d.name)}</p>
          <p class="line-meta">${money(p.price)} ${esc(t('each'))}</p>
          <div class="line-ctrl">
            <div class="qty qty-sm" role="group" aria-label="${esc(t('qtyOf')(d.name))}">
              <button type="button" data-dec="${p.id}"><span class="sr">${esc(t('less'))}</span>−</button>
              <output>${l.qty}</output>
              <button type="button" data-inc="${p.id}"><span class="sr">${esc(t('more'))}</span>+</button>
            </div>
            <button type="button" class="text-btn" data-later="${p.id}">${esc(t('saveForLater'))}</button>
            <button type="button" class="text-btn" data-remove="${p.id}">${esc(t('remove'))}</button>
          </div>
        </div>
        <p class="line-total">${money(p.price * l.qty)}</p>
      </li>`;
    }).join('');
    $('#savedSection').hidden = saved.length === 0;
    $('#savedList').innerHTML = saved.map(id => {
      const p = byId[id], d = p[lang];
      return `<li class="line">
        <img src="${p.img}" alt="" width="80" height="100" loading="lazy">
        <div class="line-info">
          <p class="line-name">${esc(d.name)}</p>
          <p class="line-meta">${money(p.price)}</p>
          <div class="line-ctrl">
            <button type="button" class="text-btn strong" data-tobag="${p.id}">${esc(t('moveToBag'))}</button>
            <button type="button" class="text-btn" data-unsave="${p.id}">${esc(t('remove'))}</button>
          </div>
        </div>
      </li>`;
    }).join('');
  }
  $('#bag').addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    const ds = b.dataset;
    const line = id => bag.find(l => l.id === id);
    if (ds.inc) setQty(ds.inc, line(ds.inc).qty + 1);
    else if (ds.dec) setQty(ds.dec, line(ds.dec).qty - 1);
    else if (ds.remove) setQty(ds.remove, 0);
    else if (ds.later) saveForLater(ds.later);
    else if (ds.tobag) { addToBag(ds.tobag, 1); }
    else if (ds.unsave) toggleSaved(ds.unsave);
    else return;
    // keep focus inside the drawer after a re-render
    if (!document.activeElement || document.activeElement === document.body) $('#bagClose').focus();
  });

  const bagEl = $('#bag'), scrim = $('#scrim');
  let lastFocus = null;
  function openBag() {
    lastFocus = document.activeElement;
    bagEl.hidden = false; scrim.hidden = false;
    requestAnimationFrame(() => { bagEl.classList.add('open'); scrim.classList.add('open'); });
    document.body.classList.add('locked');
    $('#bagClose').focus();
  }
  function closeBag() {
    bagEl.classList.remove('open'); scrim.classList.remove('open');
    document.body.classList.remove('locked');
    setTimeout(() => { bagEl.hidden = true; scrim.hidden = true; }, 260);
    if (lastFocus) lastFocus.focus();
  }
  $('#bagOpen').addEventListener('click', openBag);
  $('#bagClose').addEventListener('click', closeBag);
  scrim.addEventListener('click', closeBag);
  document.addEventListener('keydown', e => {
    if (bagEl.hidden) return;
    if (e.key === 'Escape') closeBag();
    if (e.key === 'Tab') {   // trap focus in the drawer
      const f = [...bagEl.querySelectorAll('button:not([disabled])')];
      if (!f.length) return;
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
    }
  });
  function bump() { const c = $('#bagCount'); c.classList.remove('bump'); void c.offsetWidth; c.classList.add('bump'); }

  // ---------- product dialog ----------
  const dialog = $('#productDialog');
  let current = null, pdQty = 1, opener = null;
  function fillDialog(id) {
    const p = byId[id], d = p[lang];
    $('#pdImg').src = p.img; $('#pdImg').alt = d.name;
    $('#pdCat').textContent = t('cat')[p.cat];
    $('#pdName').textContent = d.name;
    $('#pdPrice').textContent = money(p.price);
    $('#pdDesc').textContent = d.desc;
    $('#pdSpecs').innerHTML = d.specs.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('');
    $('#pdQty').textContent = pdQty;
    const s = saved.includes(id);
    $('#pdSave').textContent = s ? `✓ ${t('saved')}` : t('save');
    $('#pdSave').setAttribute('aria-pressed', String(s));
  }
  function openProduct(id, from) {
    current = id; pdQty = 1; opener = from; fillDialog(id);
    dialog.showModal();
  }
  $('#pdClose').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { if (opener && document.contains(opener)) opener.focus(); });
  $('#pdMinus').addEventListener('click', () => { pdQty = Math.max(1, pdQty - 1); $('#pdQty').textContent = pdQty; });
  $('#pdPlus').addEventListener('click', () => { pdQty = Math.min(99, pdQty + 1); $('#pdQty').textContent = pdQty; });
  $('#pdAdd').addEventListener('click', () => { addToBag(current, pdQty); dialog.close(); });
  $('#pdSave').addEventListener('click', () => toggleSaved(current));

  // ---------- toast ----------
  let toastTimer;
  function toast(msg) {
    const el = $('#toast'); el.textContent = msg; el.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('show'), 2400);
  }

  // ---------- hero video ----------
  const video = $('#heroVideo'), vbtn = $('#videoToggle'), frame = video.closest('.video-frame');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let userPaused = false;
  function syncVideoLabel() {
    const playing = !video.paused;
    $('#videoToggleLabel').textContent = playing ? t('pause') : t('play');
    vbtn.setAttribute('aria-pressed', String(!playing));
    frame.classList.toggle('is-paused', !playing);
  }
  function tryPlay() {
    if (userPaused || reduce.matches) return;
    const pr = video.play();
    if (pr && pr.catch) pr.catch(() => { frame.classList.add('no-autoplay'); syncVideoLabel(); });
  }
  video.addEventListener('playing', () => { frame.classList.add('ready'); syncVideoLabel(); });
  video.addEventListener('pause', syncVideoLabel);
  video.addEventListener('error', () => frame.classList.add('failed'), true);
  video.querySelectorAll('source').forEach(s => s.addEventListener('error', () => { if (video.networkState === 3) frame.classList.add('failed'); }));
  vbtn.addEventListener('click', () => {
    if (video.paused) { userPaused = false; video.play().catch(() => frame.classList.add('failed')); }
    else { userPaused = true; video.pause(); }
  });
  if (reduce.matches) { video.removeAttribute('autoplay'); frame.classList.add('reduced'); }
  else { video.preload = 'auto'; }
  reduce.addEventListener?.('change', () => { if (reduce.matches) { video.pause(); frame.classList.add('reduced'); } });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([en]) => { if (en.isIntersecting) tryPlay(); else if (!video.paused) video.pause(); }, { threshold: 0.25 }).observe(frame);
  } else tryPlay();

  applyLang();
})();
