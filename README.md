# MEAKIDST central link page

# KIDST AI Assistant

KIDST AI Assistant is a central AI and business assistant powered by Google Gemini.

## Features

- 🤖 Google Gemini AI assistant
- 📘 Facebook Messenger integration
- 💬 WhatsApp integration
- ✈️ Telegram integration
- 📸 Instagram integration
- 🎵 TikTok integration
- ▶️ YouTube integration
- 💼 LinkedIn integration
- 🌐 Central KIDST website/link page

## Architecture

Facebook Messenger
        ↓
KIDST AI Backend
        ↓
Google Gemini AI

## Requirements

- Node.js
- GitHub account
- Google AI Studio API key
- Facebook Developer account
- Facebook Page
- Facebook Page Access Token
- Meta Messenger Webhook

## Environment Variables

Create a `.env` file:

PORT=3000
META_VERIFY_TOKEN=YOUR_VERIFY_TOKEN
META_PAGE_ACCESS_TOKEN=YOUR_PAGE_ACCESS_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Never publish real API keys or access tokens.

## Run Locally

Install dependencies:

npm install

Start the server:

npm start

## Webhook

Facebook webhook endpoint:

/webhook

The webhook requires:

- GET verification
- POST Messenger events

## Security

Keep all API keys, access tokens, passwords and private credentials in environment variables.

Never put secret keys directly into GitHub source code.

## Project

KIDST AI Assistant

© 2026 KIDST
