const express = require('express');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
app.use(express.json());

const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;

const CLAUDE_API_URL = process.env.CLAUDE_API_URL;
const CLAUDE_API_KEY = process.env.CLAUDE_API_KEY;

function forwardToClaude(text){
  const payload = { model: 'opus-4.6', input: text };
  const headers = { 'Content-Type': 'application/json' };
  if (CLAUDE_API_KEY) headers['Authorization'] = `Bearer ${CLAUDE_API_KEY}`;
  return fetch(CLAUDE_API_URL, { method: 'POST', headers, body: JSON.stringify(payload) })
    .then(r => r.json())
    .then(d => d.output || d.reply || (typeof d === 'string' ? d : 'I didn\'t get a Claude response.'))
    .catch(() => 'Error contacting internal Claude opus 4.6');
}

function sendTelegramMessage(chatId, text){
  return fetch(TELEGRAM_API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: chatId, text })
  });
}

app.post('/telegram-webhook', async (req, res) => {
  const update = req.body;
  if (!update || !update.message) return res.sendStatus(200);
  const msg = update.message;
  const chatId = msg.chat && msg.chat.id;
  const text = msg.text;
  if (!chatId || !text) return res.sendStatus(200);
  try {
    const reply = await forwardToClaude(text);
    await sendTelegramMessage(chatId, reply);
  } catch(e){
    await sendTelegramMessage(chatId, 'Internal error processing your request.');
  }
  res.sendStatus(200);
});

app.get('/health', (req, res) => res.json({ ok: true }));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Webhook listening on port ${PORT}`));
