# Afuopulse

Afuopulse is a multilingual, AI-native agricultural field intelligence platform connecting farmers, extension officers, governments, NGOs, and approved market infrastructure through verified field evidence, human review, voice access, and low-connectivity channels.

## Included

- Consent-first authentication and farm records
- Specialist agent framework
- Government/NGO analytics and paid access
- WhatsApp and USSD webhook foundations
- Safety, Privacy, Terms, and AI Guardrails
- Expo Router frontend scaffold
- FastAPI + MongoDB backend
- CI and Docker configuration

## Start

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn server:app --reload --port 8001
```

```bash
cd frontend
cp .env.example .env
npm install
npm run start
```

Never commit secrets or `.env` files. AI outputs are provisional decision support.
