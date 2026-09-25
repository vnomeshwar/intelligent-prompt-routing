from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import clean_text

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "prompts.csv")
df["clean_prompt"] = df["prompt"].map(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    df["clean_prompt"], df["category"], test_size=0.25, random_state=42, stratify=df["category"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)),
    ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced"))
])
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"Accuracy: {accuracy:.4f}")
print(classification_report(y_test, pred, zero_division=0))
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))

(ROOT / "models").mkdir(exist_ok=True)
joblib.dump(model, ROOT / "models" / "prompt_classifier.pkl")
print("Saved model to models/prompt_classifier.pkl")
