from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load symptoms and medicine data from JSON file
with open("symptoms.json", "r") as file:
    medicine_kb = json.load(file)["symptoms"]

def extract_symptoms(text):
    """
    Extract symptoms from the text using a rule-based approach.
    """
    symptoms = []
    # List of common symptoms (loaded from JSON keys)
    symptom_keywords = list(medicine_kb.keys())
    for keyword in symptom_keywords:
        if keyword in text.lower():
            symptoms.append(keyword)
    return symptoms

def suggest_medicines(text):
    """
    Suggest medicines and dosage based on symptoms in the text.
    """
    symptoms = extract_symptoms(text)
    suggestions = []
    for symptom in symptoms:
        if symptom in medicine_kb:
            suggestions.extend(medicine_kb[symptom])
    return suggestions

@app.route("/")
def home():
    """
    Serve the frontend HTML file.
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Chatbot endpoint to handle user input and return medicine suggestions.
    """
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "Please provide a message."}), 400

    # Get medicine suggestions
    suggestions = suggest_medicines(user_input)
    if not suggestions:
        response = "I couldn't find any medicine suggestions for your symptoms. Please consult a doctor."
    else:
        response = "Based on your symptoms, you might consider:<br>"
        for medicine in suggestions:
            response += f"- {medicine['name']}: {medicine['dosage']}<br>"
            response += f"  Suggestion: {medicine['suggestion']}<br>"
        response += "Please consult a doctor before taking any medicine."

    return jsonify({"response": response})

@app.route("/symptoms", methods=["GET"])
def get_symptoms():
    """
    Endpoint to serve the list of symptoms for autocomplete.
    """
    symptoms = list(medicine_kb.keys())
    return jsonify(symptoms)

if __name__ == "__main__":
    app.run(debug=True)