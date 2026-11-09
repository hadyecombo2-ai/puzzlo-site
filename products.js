/* Puzzlo catalogue.
   SAMPLE DATA: names, details and SAR prices below are placeholders drafted for the preview.
   Replace them with the real catalogue — the shop, filters and bag all read from this file. */
window.PUZZLO_PRODUCTS = [
  {
    id: 'arabian-coastline', cat: 'places', price: 149, img: 'assets/products/arabian-coastline.webp',
    en: { name: 'Arabian Coastline', line: 'The scene from our film, piece by piece.',
          desc: 'A dhow under a coral sun, wind towers along the shore and two palms leaning into the breeze. Calm water, plenty of edges to begin with.',
          specs: [['Pieces', '1000'], ['Finished size', '68 × 49 cm']] },
    ar: { name: 'الساحل العربي', line: 'المشهد من فيلمنا، قطعة بعد قطعة.',
          desc: 'مركب شراعي تحت شمس مرجانية، وأبراج هواء على الشاطئ، ونخلتان تميلان مع النسيم. ماء هادئ وحواف كثيرة لتبدأ منها.',
          specs: [['عدد القطع', '1000'], ['المقاس بعد التركيب', '68 × 49 سم']] }
  },
  {
    id: 'corniche-at-dusk', cat: 'places', price: 149, img: 'assets/products/corniche-at-dusk.webp',
    en: { name: 'Corniche at Dusk', line: 'City lights come on along the water.',
          desc: 'Towers in deep blues, warm windows and lamps lining the promenade. A satisfying study in colour and pattern.',
          specs: [['Pieces', '1000'], ['Finished size', '68 × 49 cm']] },
    ar: { name: 'الكورنيش عند الغروب', line: 'أضواء المدينة تشتعل على امتداد الماء.',
          desc: 'أبراج بدرجات الأزرق العميق، ونوافذ دافئة، وفوانيس على طول الممشى. تمرين ممتع في اللون والتكرار.',
          specs: [['عدد القطع', '1000'], ['المقاس بعد التركيب', '68 × 49 سم']] }
  },
  {
    id: 'old-town-wind-towers', cat: 'places', price: 119, img: 'assets/products/old-town-wind-towers.webp',
    en: { name: 'Old Town Wind Towers', line: 'Coral doors and cool shade.',
          desc: 'Tall barjeel towers that once caught the breeze, sand-coloured walls and one bright door. A gentle 500 for a single evening or two.',
          specs: [['Pieces', '500'], ['Finished size', '49 × 36 cm']] },
    ar: { name: 'أبراج الهواء في الحي القديم', line: 'أبواب مرجانية وظل بارد.',
          desc: 'أبراج البارجيل التي كانت تلتقط النسيم، وجدران بلون الرمل، وباب واحد زاهٍ. ٥٠٠ قطعة هادئة لأمسية أو اثنتين.',
          specs: [['عدد القطع', '500'], ['المقاس بعد التركيب', '49 × 36 سم']] }
  },
  {
    id: 'dhow-harbour', cat: 'places', price: 149, img: 'assets/products/dhow-harbour.webp',
    en: { name: 'Dhow Harbour', line: 'Sails in every shade of morning.',
          desc: 'Wooden dhows at anchor, a low sun and a harbour full of small ripples. Big sails make a friendly place to start.',
          specs: [['Pieces', '1000'], ['Finished size', '68 × 49 cm']] },
    ar: { name: 'مرفأ المراكب', line: 'أشرعة بكل ألوان الصباح.',
          desc: 'مراكب خشبية راسية، وشمس منخفضة، ومرفأ مليء بالتموجات الصغيرة. الأشرعة الكبيرة بداية لطيفة.',
          specs: [['عدد القطع', '1000'], ['المقاس بعد التركيب', '68 × 49 سم']] }
  },
  {
    id: 'desert-camp-night', cat: 'places', price: 135, img: 'assets/products/desert-camp-night.webp',
    en: { name: 'Desert Camp, Night', line: 'A crescent moon over four warm dunes.',
          desc: 'A lit tent, two camels resting and a sky full of stars. The night sky is the slow part, and the best part.',
          specs: [['Pieces', '750'], ['Finished size', '60 × 43 cm']] },
    ar: { name: 'مخيّم في الصحراء ليلاً', line: 'هلال فوق أربعة كثبان دافئة.',
          desc: 'خيمة مضاءة، وجملان يستريحان، وسماء مليئة بالنجوم. السماء هي الجزء البطيء، وهي الأجمل.',
          specs: [['عدد القطع', '750'], ['المقاس بعد التركيب', '60 × 43 سم']] }
  },
  {
    id: 'crescent-lock', cat: 'metal', price: 69, img: 'assets/products/crescent-lock.webp',
    en: { name: 'Crescent Lock', line: 'Two crescents, one way apart.',
          desc: 'Simple to hold, hard to forget. Separate the two pieces, then try to put them back.',
          specs: [['Difficulty', '3 of 5'], ['Pieces', '2']] },
    ar: { name: 'قفل الهلال', line: 'هلالان، وطريقة واحدة للفصل.',
          desc: 'سهل الإمساك، صعب النسيان. افصل القطعتين، ثم حاول إعادتهما.',
          specs: [['الصعوبة', '3 من 5'], ['عدد القطع', '2']] }
  },
  {
    id: 'falcon-knot', cat: 'metal', price: 79, img: 'assets/products/falcon-knot.webp',
    en: { name: 'Falcon Knot', line: 'One looping knot, one free ring.',
          desc: 'Guide the ring off the knot without bending anything. Patience works better than force.',
          specs: [['Difficulty', '4 of 5'], ['Pieces', '2']] },
    ar: { name: 'عقدة الصقر', line: 'عقدة ملتفّة وحلقة حرّة.',
          desc: 'حرّر الحلقة من العقدة دون ثني أي شيء. الصبر أنفع من القوة.',
          specs: [['الصعوبة', '4 من 5'], ['عدد القطع', '2']] }
  },
  {
    id: 'palm-ring', cat: 'metal', price: 59, img: 'assets/products/palm-ring.webp',
    en: { name: 'Palm Ring', line: 'A good first teaser.',
          desc: 'A palm caught inside a ring, and a small loop that wants to be free. Friendly, but not obvious.',
          specs: [['Difficulty', '2 of 5'], ['Pieces', '3']] },
    ar: { name: 'حلقة النخلة', line: 'لغز أول مثالي.',
          desc: 'نخلة داخل حلقة، وحلقة صغيرة تريد أن تتحرر. ودود، لكنه ليس واضحاً.',
          specs: [['الصعوبة', '2 من 5'], ['عدد القطع', '3']] }
  },
  {
    id: 'mangrove-morning-family', cat: 'together', price: 99, img: 'assets/products/mangrove-morning-family.webp',
    en: { name: 'Mangrove Morning', line: 'Large pieces for many hands.',
          desc: 'Flamingos wading under round green mangroves. Bold shapes and big pieces, made for one table and several helpers.',
          specs: [['Pieces', '300, large format'], ['Finished size', '60 × 43 cm']] },
    ar: { name: 'صباح القرم', line: 'قطع كبيرة لأيادٍ كثيرة.',
          desc: 'طيور فلامنغو تخوض الماء تحت أشجار القرم الخضراء. أشكال واضحة وقطع كبيرة، لطاولة واحدة وعدة مساعدين.',
          specs: [['عدد القطع', '300، قطع كبيرة'], ['المقاس بعد التركيب', '60 × 43 سم']] }
  },
  {
    id: 'weekend-duo', cat: 'together', price: 229, img: 'assets/products/weekend-duo.webp',
    en: { name: 'Weekend Duo', line: 'Two puzzles and a teaser in one box.',
          desc: 'Dhow Harbour and Desert Camp in 500-piece editions, plus a two-ring metal teaser for whoever finishes first.',
          specs: [['Includes', '2 × 500-piece puzzles, 1 metal teaser']] },
    ar: { name: 'ثنائي نهاية الأسبوع', line: 'لغزان وتحدٍّ معدني في علبة واحدة.',
          desc: 'مرفأ المراكب ومخيّم الصحراء بنسخة ٥٠٠ قطعة، مع لغز معدني من حلقتين لمن ينتهي أولاً.',
          specs: [['المحتوى', 'لغزان × 500 قطعة، ولغز معدني واحد']] }
  }
];
