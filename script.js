/* Progressive enhancement only: both links work without JavaScript. */
(() => {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  const art = document.querySelector('#identity-art');
  const cards = [...document.querySelectorAll('.destination')];
  let detach = () => {};

  function setUpMotion() {
    detach();
    if (reducedMotion.matches || !finePointer.matches || !art) return;

    const cleanups = [];
    const listen = (element, event, handler) => {
      element.addEventListener(event, handler, { passive: true });
      cleanups.push(() => element.removeEventListener(event, handler));
    };

    // One animation frame per active element, regardless of pointer event rate.
    function track(element, apply, reset) {
      let frame = 0;
      let latest = null;
      const clear = () => {
        if (frame) cancelAnimationFrame(frame);
        frame = 0;
        latest = null;
        reset();
      };
      listen(element, 'pointermove', event => {
        if (event.pointerType === 'touch') return;
        latest = { x: event.clientX, y: event.clientY };
        if (frame) return;
        frame = requestAnimationFrame(() => {
          frame = 0;
          if (!latest) return;
          const bounds = element.getBoundingClientRect();
          if (!bounds.width || !bounds.height) return;
          const x = Math.max(0, Math.min(1, (latest.x - bounds.left) / bounds.width));
          const y = Math.max(0, Math.min(1, (latest.y - bounds.top) / bounds.height));
          apply(x, y);
        });
      });
      listen(element, 'pointerleave', clear);
      listen(element, 'pointercancel', clear);
      cleanups.push(clear);
    }

    track(art, (x, y) => {
      art.style.setProperty('--art-x', `${((x - .5) * 12).toFixed(2)}px`);
      art.style.setProperty('--art-y', `${((y - .5) * 10).toFixed(2)}px`);
    }, () => {
      art.style.removeProperty('--art-x');
      art.style.removeProperty('--art-y');
    });

    cards.forEach(card => track(card, (x, y) => {
      card.style.setProperty('--pointer-x', `${(x * 100).toFixed(1)}%`);
      card.style.setProperty('--pointer-y', `${(y * 100).toFixed(1)}%`);
      card.style.setProperty('--tilt-x', `${((.5 - y) * 5).toFixed(2)}deg`);
      card.style.setProperty('--tilt-y', `${((x - .5) * 6).toFixed(2)}deg`);
    }, () => {
      card.style.removeProperty('--pointer-x');
      card.style.removeProperty('--pointer-y');
      card.style.removeProperty('--tilt-x');
      card.style.removeProperty('--tilt-y');
    }));

    detach = () => cleanups.forEach(cleanup => cleanup());
  }

  setUpMotion();
  reducedMotion.addEventListener('change', setUpMotion);
  finePointer.addEventListener('change', setUpMotion);
})();
