const express = require('express');
const path = require('path');

const app = express();
const PORT = Number(process.env.PORT) || 3000;

// Serve the pages and styles.css straight from the repo root.
// extensions: ['html'] gives clean URLs: /freight-invoice-audit -> freight-invoice-audit.html
app.use(express.static(path.join(__dirname), {
  extensions: ['html'],
  index: 'index.html',
  dotfiles: 'deny'
}));

app.get('/healthz', (req, res) => res.type('text/plain').send('ok'));

app.use((req, res) => res.status(404).type('text/plain').send('Not found'));

app.listen(PORT, '0.0.0.0', () => {
  console.log(`sales-site listening on port ${PORT}`);
});
