from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# ----- Simple rule-based "brain" for the chatbot -----
def get_bot_response(message):
    msg = message.lower().strip()

    responses = {
        "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
        "menu": ["menu", "coffee", "drinks", "food", "what do you have"],
        "hours": ["hours", "open", "close", "timing", "when are you open"],
        "location": ["location", "where", "address", "place"],
        "price": ["price", "cost", "how much"],
        "order": ["order", "buy", "purchase"],
        "thanks": ["thanks", "thank you", "appreciate"],
        "bye": ["bye", "goodbye", "see you", "exit"]
    }

    reply_bank = {
        "greeting": ["Hey there! Welcome to Aroma Café ☕ How can I help you today?",
                     "Hello! Great to see you. What can I get started for you?"],
        "menu": ["Here's our full menu ☕: Espresso, Americano, Latte, Cappuccino, Mocha, Cold Brew, "
                 "Caramel Macchiato, Hot Chocolate, Iced Tea, Croissants, Muffins, Bagels, Donuts, "
                 "Brownies, and Club Sandwiches!",
                 "We serve a wide range: Espresso, Latte, Cappuccino, Cold Brew, Mocha, Iced Coffee, "
                 "along with Croissants, Muffins, Donuts, Brownies, and Sandwiches."],
        "hours": ["We're open every day from 8 AM to 9 PM!"],
        "location": ["We're located at 123 Bean Street, Coffee Town."],
        "price": ["Our coffees range from $2.5 to $5.5 (₹210 to ₹460) depending on the size and type. "
                   "Pastries and snacks range from $2 to $4 (₹165 to ₹330)."],
        "order": ["You can place an order by visiting us or calling +1-234-567-890!"],
        "thanks": ["You're most welcome! 😊", "Anytime! Enjoy your day."],
        "bye": ["Goodbye! Hope to see you again soon ☕", "Take care! Come back anytime."],
        "default": ["I'm not sure I understood that. Could you rephrase?",
                     "Hmm, I don't have an answer for that yet. Try asking about our menu, hours, or location!"]
    }

    for intent, keywords in responses.items():
        if any(keyword in msg for keyword in keywords):
            return random.choice(reply_bank[intent])

    return random.choice(reply_bank["default"])


# ----- Routes -----
@app.route("/")
def home():
    return render_template("index.html")


# This is the REST API endpoint the frontend calls
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)