import pandas as pd

VALID_CATEGORIES = {
    "billing", "account", "technical", "general", "complaint", "customer_support"
}

def validate_dataset(path):
    df = pd.read_csv(path)
    issues = []

    if df["prompt"].isna().any() or (df["prompt"].astype(str).str.strip() == "").any():
        issues.append("Missing or empty prompts found.")

    if df["prompt"].duplicated().any():
        issues.append("Duplicate prompts found.")

    invalid = set(df["category"].dropna()) - VALID_CATEGORIES
    if invalid:
        issues.append(f"Invalid categories: {sorted(invalid)}")

    return {"valid": len(issues) == 0, "issues": issues, "rows": len(df)}

if __name__ == "__main__":
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    print(validate_dataset(ROOT / "data" / "prompts.csv"))
