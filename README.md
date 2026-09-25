# Intelligent Prompt Routing System

An NLP and machine-learning-based prompt routing system that automatically **classifies user prompts and routes them to the appropriate workflow**.

The system processes natural-language requests, predicts the relevant category using a trained **TF-IDF + Logistic Regression** model, and combines machine-learning predictions with rule-based routing to determine the appropriate workflow.

##  Objective

The goal of this project is to automate the classification and routing of incoming user prompts, reducing manual categorization and demonstrating how **NLP, machine learning, and workflow automation** can work together in an end-to-end application.

##  How It Works

```text
User Prompt
     ↓
Text Preprocessing
     ↓
TF-IDF Feature Extraction
     ↓
Logistic Regression Model
     ↓
Prompt Classification
     ↓
Rule-Based / ML Routing
     ↓
Workflow + Confidence + Sentiment
     ↓
SQLite Logging
```

##  Technologies Used

* **Python** — application and ML development
* **NLP** — natural-language prompt processing
* **Scikit-learn** — machine-learning model
* **TF-IDF** — text feature extraction
* **Logistic Regression** — prompt classification
* **Flask** — web interface and API
* **SQLite / SQL** — data storage and logging

##  Key Features

* NLP-based prompt classification
* TF-IDF feature extraction
* Logistic Regression classification
* Rule-based high-confidence routing
* ML-based routing for other prompts
* Sentiment detection
* Confidence score generation
* Dataset validation
* SQLite-based logging
* Model evaluation
* Flask-based web interface and API

##  Prompt Categories

The system currently classifies prompts into:

* **Billing**
* **Account**
* **Technical**
* **General**
* **Complaint**
* **Customer Support**

##  Model Evaluation

The trained classification model achieved **82.61% test accuracy** on the evaluated test split of 23 samples.

The evaluation includes precision, recall, F1-score, and support for each prompt category.

> The reported accuracy is based on the actual evaluation run and should be updated if the dataset, model, or test split changes.

##  Example

### Input

```text
I was charged twice for my order.
```

### Expected Routing

```text
Category: billing
Workflow: billing_workflow
Confidence: High
```

The API returns the predicted category, workflow route, confidence score, sentiment, and routing method.

##  Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python src/train_model.py
```

Validate the dataset:

```bash
python src/validation.py
```

Start the Flask application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

##  API Usage

Send a POST request to `/route` with:

```json
{
  "prompt": "I was charged twice for my order"
}
```

The API returns the predicted category, route, confidence, sentiment, and routing method.

##  Project Demo

### Application Interface

![Prompt Routing System](screenshots/prompt-routing-demo.png)

### Routing Result

![Prompt Routing Result](screenshots/prompt-routing-result.png)

##  Project Structure

```text
prompt-routing-project/
│
├── data/
├── models/
├── screenshots/
├── src/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

##  Project Outcome

This project demonstrates an end-to-end workflow for **NLP-based text classification, intelligent routing, model evaluation, API development, and data logging** using Python and machine-learning technologies.


