# Prompt Routing Project

An NLP-based prompt classification and routing pipeline built with Python and SQL/SQLite.

## Objective
Automatically classify incoming prompts and route them to an appropriate workflow.

## Pipeline
1. Data preprocessing
2. TF-IDF feature extraction
3. Logistic Regression classification
4. Rule-based high-confidence routing
5. Sentiment detection
6. Dataset validation
7. SQL/SQLite logging
8. Model evaluation
9. Flask API

## Categories
- billing
- account
- technical
- general
- complaint
- customer_support

## Run

```bash
pip install -r requirements.txt
python src/train_model.py
python src/validation.py
python app.py
```

Then POST JSON to `/route`:

```json
{"prompt": "I was charged twice for my order"}
```

The API returns the predicted category, route, confidence, sentiment, and routing method.

## Important
The accuracy reported in the project should be the accuracy printed by the evaluation run. Do not claim 96% unless the evaluated model actually achieves it on the stated test split.

## Project Demo

### Application Interface
![Prompt Routing System](screenshots/prompt-routing-demo.png)

### Routing Result
![Prompt Routing Result](screenshots/prompt-routing-result.png)