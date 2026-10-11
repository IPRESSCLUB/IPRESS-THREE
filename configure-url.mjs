#!/usr/bin/env node
// Optional: change the canonical and social-preview URLs for another repository.
// Usage: node scripts/configure-url.mjs https://your-domain.example/path/
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const project = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const indexPath = existsSync(resolve(project, 'index.html'))
  ? resolve(project, 'index.html') : resolve(project, 'dist/index.html');
const input = process.argv[2];
if (!input) {
  console.error('Supply the complete HTTPS URL where you will host this page.');
  process.exit(1);
}
let url;
try { url = new URL(input); } catch {
  console.error('The supplied URL is invalid.');
  process.exit(1);
}
if (url.protocol !== 'https:' || url.username || url.password || url.search || url.hash) {
  console.error('Use an HTTPS URL without credentials, a query, or a fragment.');
  process.exit(1);
}
if (!url.pathname.endsWith('/')) url.pathname += '/';
const base = url.href;
const social = new URL('assets/social-preview.png', base).href;
const escape = value => value.replaceAll('&', '&amp;').replaceAll('"', '&quot;');
let html = readFileSync(indexPath, 'utf8');
html = html.replace(/(<link rel="canonical" href=")[^"]*(">)/, `$1${escape(base)}$2`)
  .replace(/(<meta property="og:url" content=")[^"]*(">)/, `$1${escape(base)}$2`)
  .replace(/(<meta property="og:image" content=")[^"]*(">)/, `$1${escape(social)}$2`)
  .replace(/(<meta name="twitter:image" content=")[^"]*(">)/, `$1${escape(social)}$2`);
writeFileSync(indexPath, html);
console.log(`Canonical and social metadata updated for ${base}`);
