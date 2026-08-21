(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const A = '#123a6b', G = '#b9c4cd';
  const XR = [
    { k: 'VR', t: 'VR（仮想現実）', d: '現実は見えず、すべて仮想空間。ヘッドマウントディスプレイで没入する。',
      svg: '<rect x="8" y="10" width="104" height="60" rx="4" fill="' + A + '"/><circle cx="40" cy="40" r="10" fill="#fff" opacity=".8"/><circle cx="80" cy="40" r="10" fill="#fff" opacity=".8"/><text x="60" y="82" font-size="10" text-anchor="middle" fill="#858a92">すべて仮想</text>' },
    { k: 'AR', t: 'AR（拡張現実）', d: '現実の風景に、情報やキャラクターを重ねて表示する。',
      svg: '<rect x="8" y="10" width="104" height="60" rx="4" fill="' + G + '"/><rect x="20" y="26" width="26" height="34" fill="#9aa7b2"/><circle cx="82" cy="38" r="14" fill="' + A + '" opacity=".9"/><text x="60" y="82" font-size="10" text-anchor="middle" fill="#858a92">現実＋情報</text>' },
    { k: 'MR', t: 'MR（複合現実）', d: '現実と仮想が互いに影響し合う。仮想の物体を現実の位置に固定して操作できる。',
      svg: '<rect x="8" y="10" width="104" height="60" rx="4" fill="' + G + '"/><rect x="14" y="44" width="92" height="16" fill="#9aa7b2"/><circle cx="60" cy="36" r="15" fill="' + A + '" opacity=".9"/><path d="M45 44 h30" stroke="#c0392b" stroke-width="2"/><text x="60" y="82" font-size="10" text-anchor="middle" fill="#858a92">現実と仮想が影響</text>' }
  ];
  let xrCur = -1;
  function drawXR() {
    $('xrBox').innerHTML = XR.map((x, i) =>
      '<div class="c' + (i === xrCur ? ' on' : '') + '" data-i="' + i + '">' +
      '<svg viewBox="0 0 120 88" role="img" aria-label="' + x.t + '">' + x.svg + '</svg>' +
      '<div class="t">' + x.t + '</div></div>').join('');
    $('xrBox').querySelectorAll('.c').forEach(el => el.addEventListener('click', () => {
      xrCur = +el.dataset.i; drawXR();
      const n = $('xrNote'); n.className = 'note ok';
      n.innerHTML = '<strong>' + XR[xrCur].t + '</strong>　' + XR[xrCur].d;
    }));
  }
  const CASES = [
    { k: 'A', t: 'ヘッドマウントディスプレイを使って、仮想空間で体験する飛行機操縦シミュレーション。', a: 'VR', why: '現実は見えず、完全に仮想空間の中で体験しています。' },
    { k: 'B', t: 'スマートフォンのカメラを通じて、現実世界にアニメのキャラクターを重ねて表示させる。', a: 'AR', why: '現実の映像に情報を重ねているのでARです。' },
    { k: 'C', t: '患者のCTデータから生成した仮想臓器を現実の身体に重ね合わせ、医師が手術の動きを事前にシミュレーションする。', a: 'MR', why: '現実の身体と仮想の臓器が<strong>位置を合わせて影響し合っている</strong>のでMRです。' }
  ];
  const CCH = ['VR', 'AR', 'MR'];
  let cAns = {};
  function drawCases() {
    $('caseBox').innerHTML = CASES.map((c, i) =>
      '<div style="border:1px solid var(--line);border-radius:3px;padding:10px 12px;margin-bottom:8px">' +
      '<div style="margin-bottom:8px"><strong>' + c.k + '</strong>　' + c.t + '</div>' +
      '<div class="choice4" data-i="' + i + '">' + CCH.map(x =>
        '<button class="btn" data-i="' + i + '" data-c="' + x + '" style="text-align:center">' + x + '</button>').join('') + '</div>' +
      '<div class="note" id="cfb' + i + '" hidden style="margin-top:8px"></div></div>').join('');
    $('caseBox').querySelectorAll('button[data-c]').forEach(b => b.addEventListener('click', () => {
      const i = +b.dataset.i, c = CASES[i], ok = b.dataset.c === c.a;
      const row = $('caseBox').querySelector('.choice4[data-i="' + i + '"]');
      row.classList.add('locked');
      [...row.children].forEach(x => { if (x.dataset.c === c.a) x.classList.add('correct'); else if (x === b) x.classList.add('wrong'); });
      const fb = $('cfb' + i); fb.hidden = false; fb.className = 'note ' + (ok ? 'ok' : 'ng');
      fb.innerHTML = '<strong>' + c.a + '</strong>　' + c.why;
      cAns[i] = ok;
      const done = Object.keys(cAns).length, right = Object.values(cAns).filter(Boolean).length;
      const n = $('caseNote');
      n.className = 'note ' + (done === CASES.length ? (right === done ? 'ok' : 'warn') : 'info');
      n.innerHTML = done + ' / ' + CASES.length + ' 問（正解 ' + right + ' 問）' +
        (done === CASES.length ? '<br>A＝VR、B＝AR、C＝MR。この組合せが【イ】＝<strong>⓪</strong>です。' : '');
    }));
    $('caseNote').className = 'note info'; $('caseNote').textContent = '0 / ' + CASES.length + ' 問';
  }

  /* ===== STEP 2 ===== */
  const GAPS = [
    { t: '年齢による差', d: '操作に慣れている若年層と、そうでない高齢者との間で差が生まれます。' },
    { t: '地域による差', d: '通信環境が整っていない地域では、同じサービスが受けられません。' },
    { t: '経済状況による差', d: '端末や通信費の負担が大きいと、そもそも使えません。' },
    { t: '障がいの有無による差', d: 'アクセシビリティに配慮のないサービスは、使えない人を生みます。' },
    { t: '言語による差', d: '日本語だけの案内では、外国にルーツをもつ人に情報が届きません。' }
  ];
  let gOpen = {};
  function drawGap() {
    $('gapBox').innerHTML = GAPS.map((g, i) =>
      '<div class="g' + (gOpen[i] ? ' on' : '') + '" data-i="' + i + '"><strong>' + g.t + '</strong>' +
      (gOpen[i] ? '<br><span class="small" style="color:var(--muted)">' + g.d + '</span>' : '') + '</div>').join('');
    $('gapBox').querySelectorAll('.g').forEach(el => el.addEventListener('click', () => {
      gOpen[+el.dataset.i] = true; drawGap();
      const c = Object.keys(gOpen).length;
      const n = $('gapNote');
      n.className = 'note ' + (c === GAPS.length ? 'ok' : 'info');
      n.innerHTML = c + ' / ' + GAPS.length + ' 個' +
        (c === GAPS.length ? '<br>このような差をまとめて<strong>デジタルデバイド（情報格差）</strong>といいます。原因は1つではありません。' : '');
    }));
    $('gapNote').className = 'note info'; $('gapNote').textContent = 'カードをクリックして確かめましょう。';
  }

  /* ===== STEP 3 ===== */
  const ERA = [
    { y: '1940年代', t: '世界初の電子計算機が作られる。部屋いっぱいの大きさだった。' },
    { y: '1970年代', t: 'マイクロプロセッサが登場し、コンピュータが小型化。' },
    { y: '1980年代', t: 'パーソナルコンピュータ（PC）が普及しはじめる。' },
    { y: '1990年代', t: 'インターネットが一般に開放され、Webが広まる。' },
    { y: '2000年代', t: '携帯電話・ブロードバンドの普及。SNSが登場。' },
    { y: '2010年代', t: 'スマートフォンが普及。クラウド・ビッグデータ・AIの実用化が進む。' },
    { y: '2020年代', t: '5G・IoT・生成AIが広がり、Society 5.0 が構想される。' }
  ];
  function drawEra() {
    $('eraBox').innerHTML = ERA.map(e => '<div class="e"><div class="y">' + e.y + '</div><div class="t">' + e.t + '</div></div>').join('');
    $('techTable').innerHTML = '<thead><tr><th>技術</th><th>意味</th><th>身近な例</th></tr></thead><tbody>' +
      '<tr><td><strong>AI（人工知能）</strong></td><td>大量のデータから学習し、判断や生成を行う技術</td><td>音声アシスタント、生成AI</td></tr>' +
      '<tr><td><strong>IoT</strong></td><td>さまざまなモノがインターネットにつながるしくみ</td><td>スマート家電、見守りセンサー</td></tr>' +
      '<tr><td><strong>ビッグデータ</strong></td><td>従来の方法では扱いきれない大量・多様なデータ</td><td>購買履歴、位置情報、SNSの投稿</td></tr>' +
      '<tr><td><strong>クラウド</strong></td><td>インターネット経由でサービスや保存領域を使うしくみ</td><td>オンラインストレージ、Webメール</td></tr>' +
      '<tr><td><strong>Society 5.0</strong></td><td>仮想空間と現実空間を高度に融合させた社会の構想</td><td>自動運転、遠隔医療</td></tr></tbody>';
  }

  function init() {
    drawXR(); drawCases(); drawGap(); drawEra();
    Quiz.choice('q1Box', 'q1Note', [
      { k: 'ア', q: 'デジタルデバイドに関する記述として最も適当なものは',
        ch: ['パソコンやスマートフォンを長時間使いすぎることで視力や集中力が低下する身体的問題のことを指す', 'インターネットやSNSの普及によって、人とのつながりが減り、孤独を感じる人が増える現象のことを指す', '外国にルーツを持つ住民が、日本語を十分に理解できず、必要なサービスを受けにくくなる問題のことを指す', '情報技術の発達によって生じる情報格差のことを指し、特に若年層が高齢者よりもテクノロジーに習熟していることが原因の一つとしてある'],
        a: 3, why: 'デジタルデバイド＝<strong>情報格差</strong>です。⓪は健康の問題、①は人間関係の問題で別のこと。②は言語の壁による格差で、デジタルデバイドの一例ではありますが、定義としては③が最も適当です。' }
    ], '本文の答えは【ア】③ です。');
    Quiz.choice('q2Box', 'q2Note', [
      { k: 'イ', q: 'A〜C の事例は、それぞれVR・AR・MRのいずれに適するか',
        ch: ['A VR／B AR／C MR', 'A AR／B VR／C MR', 'A MR／B AR／C VR', 'A MR／B VR／C AR'],
        a: 0, why: '完全な仮想空間＝VR、現実に重ねる＝AR、現実と仮想が影響し合う＝MRです。' }
    ], '本文の答えは【イ】⓪ です。');
    window.Terms.glossary($('glossBox'), ['デジタルデバイド', '情報格差', 'VR', 'AR', 'MR', 'IoT', 'ビッグデータ', '人工知能']);
    Worksheet.make('wsBox', {
      name: 'digital-tech-evolution',
      fields: [
        { id: 't1', label: '① 取り上げる道具', hint: '電話・音楽・写真・地図・買い物・お金など。', rows: 2, ph: '例：写真のとり方と見せ方' },
        { id: 't2', label: '② 昔（聞き取り）', hint: 'だれに聞いたか、どう使っていたか。', rows: 3,
          ph: '例：祖母に聞いた。フィルムカメラで撮り、写真屋に出して1週間後に紙で受け取っていた' },
        { id: 't3', label: '③ いま', hint: '自分の使い方。', rows: 2, ph: '例：スマートフォンで撮ってすぐ共有し、クラウドに保存する' },
        { id: 't4', label: '④ 何が変わったか', hint: '速さ・量・費用・だれが使えるか。数で書けるとよい。', rows: 3,
          ph: '例：1週間→数秒。1本36枚→ほぼ無制限。現像代が不要になった' },
        { id: 't5', label: '⑤ 変化で生まれた新しい問題', hint: '便利になったぶん、何が起きたか。', rows: 3,
          ph: '例：勝手に撮られて公開される。データが多すぎて探せない。保存先がなくなると消える' },
        { id: 't6', label: '⑥ これからどうなると思うか', hint: '根拠もいっしょに。', rows: 2, ph: '例：AIが自動で整理する。だからこそ「何を残すか」を人が決める必要が出てくる' }
      ],
      build: function (v, e) {
        return '<h4>技術の変化 年表シート</h4><dl>' +
          '<dt>① 取り上げる道具</dt><dd>' + e(v.t1) + '</dd>' +
          '<dt>② 昔（聞き取り）</dt><dd>' + e(v.t2) + '</dd>' +
          '<dt>③ いま</dt><dd>' + e(v.t3) + '</dd>' +
          '<dt>④ 変わったこと</dt><dd>' + e(v.t4) + '</dd>' +
          '<dt>⑤ 生まれた新しい問題</dt><dd>' + e(v.t5) + '</dd>' +
          '<dt>⑥ これから</dt><dd>' + e(v.t6) + '</dd></dl>';
      },
      note: '④を「速い・便利」ではなく<strong>数</strong>で書くと、変化の大きさが伝わります。'
    });

    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
