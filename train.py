print("TRAIN.PY IS RUNNING")
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("emails.csv")

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", RandomForestClassifier())
])

model.fit(data["text"], data["label"])

joblib.dump(model, "model.pkl")

print("Model trained successfully!")
