/* Tests motion preference changes and pointer event scheduling without a browser. */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const publicRoot = fs.existsSync(path.join(root, 'index.html')) ? root : path.join(root, 'dist');
const code = fs.readFileSync(path.join(publicRoot, 'script.js'), 'utf8');

function target() {
  const listeners = new Map();
  const values = new Map();
  return {
    listeners, values,
    style: { setProperty: (k,v) => values.set(k,v), removeProperty: k => values.delete(k) },
    getBoundingClientRect: () => ({ left: 10, top: 20, width: 200, height: 100 }),
    addEventListener(type, fn) {
      if (!listeners.has(type)) listeners.set(type, new Set());
      listeners.get(type).add(fn);
    },
    removeEventListener(type, fn) { listeners.get(type)?.delete(fn); },
    emit(type, value) { [...(listeners.get(type) || [])].forEach(fn => fn(value)); },
  };
}

function boot(reduce, fine) {
  const reduced = Object.assign(target(), { matches: reduce });
  const pointer = Object.assign(target(), { matches: fine });
  const art = target();
  const cards = [target(), target()];
  const frames = new Map();
  let id = 0;
  vm.runInNewContext(code, {
    window: { matchMedia: q => q.includes('reduced-motion') ? reduced : pointer },
    document: { querySelector: () => art, querySelectorAll: () => cards },
    requestAnimationFrame(fn) { frames.set(++id, fn); return id; },
    cancelAnimationFrame(key) { frames.delete(key); },
  });
  return { reduced, pointer, art, cards, frames,
    tick() { for (const [key, fn] of [...frames]) { frames.delete(key); fn(); } },
  };
}

const desktop = boot(false, true);
for (let i=0; i<20; i++) desktop.art.emit('pointermove', { pointerType:'mouse', clientX:210, clientY:120 });
assert.equal(desktop.frames.size, 1, 'Pointer events must share a single pending frame');
desktop.tick();
assert.equal(desktop.art.values.get('--art-x'), '6.00px');
assert.equal(desktop.art.values.get('--art-y'), '5.00px');
desktop.cards[0].emit('pointermove', {pointerType:'mouse', clientX:900, clientY:-100});
desktop.tick();
assert.equal(desktop.cards[0].values.get('--pointer-x'), '100.0%');
assert.equal(desktop.cards[0].values.get('--pointer-y'), '0.0%');
assert.equal(desktop.cards[0].values.get('--tilt-x'), '2.50deg');
assert.equal(desktop.cards[0].values.get('--tilt-y'), '3.00deg');
desktop.art.emit('pointerleave');
assert.equal(desktop.art.values.size, 0);
desktop.art.emit('pointermove', { pointerType:'mouse', clientX:210, clientY:120 });
desktop.reduced.matches = true;
desktop.reduced.emit('change');
assert.equal(desktop.frames.size, 0, 'Enabling reduced motion cancels pending animation frames');
assert.equal(desktop.cards[0].values.size, 0);
assert.equal(desktop.art.listeners.get('pointermove').size, 0);
desktop.reduced.matches = false;
desktop.reduced.emit('change');
assert.equal(desktop.art.listeners.get('pointermove').size, 1, 'Listeners must not accumulate');
desktop.art.emit('pointermove', { pointerType:'touch', clientX:210, clientY:120 });
assert.equal(desktop.frames.size, 0, 'Touch events must not enable cursor effects');
desktop.pointer.matches = false;
desktop.pointer.emit('change');
assert.equal(desktop.art.listeners.get('pointermove').size, 0);
assert.equal(boot(true, true).art.listeners.size, 0);
assert.equal(boot(false, false).art.listeners.size, 0);
console.log('PASS: fine-pointer gating, reduced-motion gating and live changes, coalesced frames, bounded motion, cancellation, cleanup and touch exclusion');
