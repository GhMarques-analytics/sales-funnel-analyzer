"""
generate_data.py
Generates a synthetic CRM dataset for Outbound sales funnel analysis.
Gera um dataset sintético de CRM para análise de funil de vendas Outbound.

Author: Gustavo Marques (@GhMarques-analytics)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# ── Seed for reproducibility | Seed para reprodutibilidade ──
np.random.seed(42)
random.seed(42)

# ── Configuration | Configuração ──
N_LEADS = 500
START_DATE = datetime(2025, 1, 1)

# ── Options | Opções ──
CHANNELS = ["Cold Email", "LinkedIn", "Phone Call"]
CHANNEL_WEIGHTS = [0.45, 0.35, 0.20]  # Cold email dominates | Cold email domina

STAGES = ["Prospected", "Contacted", "Responded", "Meeting Scheduled", "Qualified", "Lost"]

SEGMENTS = ["SaaS", "Fintech", "E-commerce", "Agtech", "Healthtech", "Logistics"]

DECISION_MAKERS = ["CTO", "VP of Sales", "Head of Engineering", "CEO", "COO"]

LOST_REASONS = [
    "No response after 3 follow-ups",
    "Not a decision maker",
    "Budget unavailable",
    "Wrong timing",
    "Competitor chosen",
    "No fit with ICP",
]

COMPANY_SIZES = ["1-10", "11-50", "51-200", "201-500", "500+"]


def random_date(start: datetime, days_range: int) -> datetime:
    """Generate a random date within a range."""
    return start + timedelta(days=random.randint(0, days_range))


def assign_stage(channel: str) -> str:
    """Assign funnel stage based on channel conversion rates."""
    rates = {
        "Cold Email":   [0.30, 0.25, 0.20, 0.12, 0.08, 0.05],
        "LinkedIn":     [0.20, 0.30, 0.25, 0.12, 0.08, 0.05],
        "Phone Call":   [0.15, 0.20, 0.25, 0.20, 0.12, 0.08],
    }
    return random.choices(STAGES, weights=rates[channel])[0]


def generate_leads(n: int) -> pd.DataFrame:
    """Generate synthetic lead records."""
    records = []

    for i in range(n):
        channel = random.choices(CHANNELS, weights=CHANNEL_WEIGHTS)[0]
        stage = assign_stage(channel)
        contact_date = random_date(START_DATE, 365)

        # Days in each stage before moving forward
        days_to_respond = random.randint(1, 7) if stage not in ["Prospected"] else None
        days_to_meeting = random.randint(2, 14) if stage in ["Meeting Scheduled", "Qualified"] else None

        records.append({
            "lead_id": f"LEAD-{i+1:04d}",
            "company": f"Company {i+1}",
            "segment": random.choice(SEGMENTS),
            "company_size": random.choice(COMPANY_SIZES),
            "decision_maker": random.choice(DECISION_MAKERS),
            "channel": channel,
            "stage": stage,
            "contact_date": contact_date.strftime("%Y-%m-%d"),
            "days_to_respond": days_to_respond,
            "days_to_meeting": days_to_meeting,
            "lost_reason": random.choice(LOST_REASONS) if stage == "Lost" else None,
            "is_qualified": 1 if stage == "Qualified" else 0,
        })

    return pd.DataFrame(records)


if __name__ == "__main__":
    print("Generating synthetic CRM dataset...")
    print("Gerando dataset sintético de CRM...\n")

    df = generate_leads(N_LEADS)

    # Create data folder if not exists | Cria pasta data se não existir
    os.makedirs("data", exist_ok=True)
    output_path = "data/crm_leads.csv"
    df.to_csv(output_path, index=False)

    print(f"Dataset saved to '{output_path}'")
    print(f"Dataset salvo em '{output_path}'")
    print(f"\nTotal leads generated | Total de leads gerados: {len(df)}")
    print(f"Stages distribution | Distribuição por etapa:")
    print(df['stage'].value_counts())
    print(f"\nChannel distribution | Distribuição por canal:")
    print(df['channel'].value_counts())
    print(f"\nQualification rate | Taxa de qualificação: {df['is_qualified'].mean():.1%}")
