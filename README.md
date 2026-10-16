# The Digital Experience Shop App Console

A Streamlit prototype for retail intelligence and shop operations at The Digital Experience, Fourways Crossing.

## Included modules
- V1 Executive Overview
- V2 Sales & Transactions
- V3 Marketing Intelligence
- V4 Products & Inventory
- V5 Automation & Tasks
- V6 Rule-based AI Insights
- V7 Data & Governance
- V8 Growth & Reports
- Customer & CRM tools

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud
1. Create a new GitHub repository or use a repository you control.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. In Streamlit Community Cloud, choose the repository, branch, and `app.py`.
4. Deploy, then test every navigation screen.

## Important limitations
- Uses fictional demo data.
- Data changes are stored in Streamlit session state and may reset when the session restarts.
- No live POS, payments, accounting, CRM, email, or inventory integrations are configured.
- AI Insights are rule-based recommendations, not a connected AI service.
- Add authentication, persistent storage, backups, and permissions before production use.
