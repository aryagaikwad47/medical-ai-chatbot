from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_response(message):
    message = message.lower()

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! I am a simple Medical AI Chatbot. How can I help you today?"

    # Fever
    elif "fever" in message:
        return (
            "Fever can occur due to infections or other conditions. "
            "Rest, drink plenty of fluids, and monitor your temperature. "
            "If the fever is very high, persistent, or accompanied by serious symptoms, "
            "please consult a doctor."
        )

    # Headache
    elif "headache" in message:
        return (
            "Headaches can have many causes such as stress, dehydration, lack of sleep, "
            "or illness. Try resting and drinking enough water. "
            "If the headache is severe, sudden, or recurring, consult a healthcare professional."
        )

    # Cold
    elif "cold" in message or "runny nose" in message:
        return (
            "A common cold may cause a runny nose, sneezing, sore throat, and cough. "
            "Get adequate rest and drink plenty of fluids. "
            "Seek medical advice if symptoms become severe or do not improve."
        )

    # Cough
    elif "cough" in message:
        return (
            "A cough can occur because of a cold, allergies, infection, or other causes. "
            "Stay hydrated and get enough rest. "
            "If you have difficulty breathing, chest pain, or a persistent cough, "
            "seek medical attention."
        )

    # Stomach pain
    elif "stomach pain" in message or "abdominal pain" in message:
        return (
            "Stomach pain can have many causes, including indigestion, infection, "
            "or food-related problems. Drink water and avoid heavy foods temporarily. "
            "If the pain is severe or persistent, consult a doctor."
        )

    # Sore throat
    elif "sore throat" in message or "throat pain" in message:
        return (
            "A sore throat can be caused by infections, allergies, or irritation. "
            "Drink warm fluids and stay hydrated. "
            "If you have severe pain, difficulty swallowing, or breathing problems, "
            "seek medical care."
        )

    # Diabetes
    elif "diabetes" in message:
        return (
            "Diabetes is a condition in which blood glucose levels are too high. "
            "Common symptoms can include increased thirst, frequent urination, "
            "and tiredness. Proper diagnosis requires medical testing and consultation "
            "with a healthcare professional."
        )

    # Blood pressure
    elif "blood pressure" in message or "bp" in message:
        return (
            "Blood pressure measures the force of blood against artery walls. "
            "High or low blood pressure may require medical evaluation. "
            "Regular monitoring and a healthy lifestyle can be helpful."
        )

    # Emergency
    elif any(word in message for word in [
        "chest pain",
        "difficulty breathing",
        "can't breathe",
        "cannot breathe",
        "unconscious",
        "severe bleeding"
    ]):
        return (
            "This may require urgent medical attention. "
            "Please contact your local emergency medical service or go to the nearest "
            "emergency department immediately."
        )

    # Medicine
    elif "medicine" in message or "medication" in message:
        return (
            "Medicines should be taken according to a doctor's or pharmacist's advice. "
            "Do not start, stop, or change a medicine without professional guidance."
        )

    # Healthy lifestyle
    elif "healthy" in message or "health tips" in message:
        return (
            "Some general healthy habits include eating a balanced diet, drinking enough "
            "water, exercising regularly, getting adequate sleep, and avoiding tobacco."
        )

    # Thank you
    elif "thank" in message:
        return "You're welcome! Stay healthy and take care."

    # Default response
    else:
        return (
            "I'm sorry, I don't have information about that topic. "
            "You can ask me about common topics such as fever, headache, cough, cold, "
            "stomach pain, diabetes, blood pressure, or general health tips."
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    response = get_response(message)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)