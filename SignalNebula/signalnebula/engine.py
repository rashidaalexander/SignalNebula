
from __future__ import annotations
import csv, math, statistics

def load_signal(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def analyze(path: str) -> dict:
    rows = load_signal(path)
    snrs = [float(r["power_db"]) - float(r["noise_db"]) for r in rows]
    drifts = [float(r["drift_hz"]) for r in rows]
    status = "stable" if max(drifts) < 1 else "degraded"
    return {
        "samples": len(rows),
        "avg_snr_db": round(statistics.mean(snrs), 2),
        "peak_snr_db": round(max(snrs), 2),
        "max_drift_hz": max(drifts),
        "status": status,
    }
