from flask import Flask, request, render_template, jsonify

# In-memory storage for moods and responses
mood_history = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todo")
@app.route("/todo.html")
def todo():
    return render_template("todo.html")

@app.route("/diary")
@app.route("/diary.html")
def diary():
    return render_template("diary.html")

# Route for Ludo game
@app.route("/ludo")
@app.route("/ludo.html")
def ludo():
    return render_template("ludo.html")

# Route for Mario-like game
@app.route("/mario")
@app.route("/mario.html")
def mario():
    return render_template("mario.html")

# Route for Breathing exercise game/page




@app.route("/api/mood", methods=["POST"])
def get_mood_response():
    data = request.get_json()
    user_input = data.get("mood", "").strip()

    if not user_input:
        return jsonify({
            "status": "error",
            "emotion": "unknown",
            "intensity": "not specified",
            "quote": "Please describe your situation in detail.",
            "action": "Try writing a short sentence about how you feel.",
            "game": None
        }), 400

    # Expanded rule-based emotion and intensity/description detection
    text = user_input.lower()
    emotion, intensity, quote, action, game = None, None, None, None, None

    if "happy" in text or "joy" in text or "excited" in text or "content" in text:
        emotion = "happiness"
        intensity = "joy, contentment, satisfaction"
        quote = "Happiness is best when shared!"
        action = "Celebrate your joy—share it with someone or do something you love."
        game = "mario"
    elif "sad" in text or "grief" in text or "hopeless" in text or "disappointed" in text:
        if "grief" in text:
            emotion = "grief"
            intensity = "intense sorrow, often from loss"
            quote = "Grief is the price we pay for love."
            action = "Allow yourself to mourn and seek support from loved ones."
            game = "diary"
        else:
            emotion = "sadness"
            intensity = "disappointment, sorrow, or hopelessness"
            quote = "It's okay to feel down. Brighter days are ahead."
            action = "Talk to a friend or write down your feelings."
            game = "diary"
    elif "fear" in text or "afraid" in text or "scared" in text or "terrified" in text:
        emotion = "fear"
        intensity = "worry, nervousness, or terror"
        quote = "Courage is not the absence of fear, but the triumph over it."
        action = "Take deep breaths and remind yourself of your strengths."
        game = "breathing"
    elif "angry" in text or "mad" in text or "furious" in text or "rage" in text:
        emotion = "anger"
        intensity = "frustration, irritation, or rage"
        quote = "Anger is one letter short of danger. Take a deep breath."
        action = "Step away from the situation and do some deep breathing."
        game = "breathing"
    elif "surprise" in text or "shocked" in text or "astonished" in text:
        emotion = "surprise"
        intensity = "unexpected, positive or negative"
        quote = "Life is full of surprises. Embrace the unexpected."
        action = "Pause and process the new information before reacting."
        game = "diary"
    elif "disgust" in text or "revolted" in text or "repulsed" in text:
        emotion = "disgust"
        intensity = "strong aversion or revulsion"
        quote = "Disgust can be a signal to protect yourself."
        action = "Distance yourself from the source and focus on something pleasant."
        game = "diary"
    elif "love" in text or "affection" in text or "caring" in text:
        emotion = "love"
        intensity = "deep affection and care"
        quote = "To love and be loved is the greatest joy."
        action = "Express your feelings to those you care about."
        game = "diary"
    elif "jealous" in text or "jealousy" in text:
        emotion = "jealousy"
        intensity = "envy mixed with resentment"
        quote = "Jealousy is a sign of what you value."
        action = "Reflect on your feelings and communicate openly."
        game = "diary"
    elif "pride" in text or "proud" in text:
        emotion = "pride"
        intensity = "deep satisfaction in achievements"
        quote = "Be proud of how far you’ve come."
        action = "Celebrate your achievements and encourage others."
        game = "diary"
    elif "guilt" in text or "guilty" in text:
        emotion = "guilt"
        intensity = "remorse for actions or inactions"
        quote = "Guilt is a chance to learn and grow."
        action = "Make amends if possible and forgive yourself."
        game = "diary"
    elif "shame" in text or "ashamed" in text:
        emotion = "shame"
        intensity = "painful sense of failure or disgrace"
        quote = "Shame grows in secrecy. Share your feelings with someone you trust."
        action = "Remember, everyone makes mistakes. Practice self-compassion."
        game = "diary"
    elif "anxiety" in text or "anxious" in text or "nervous" in text:
        emotion = "anxiety"
        intensity = "worry, nervousness, unease"
        quote = "Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength."
        action = "Try grounding techniques and focus on the present moment."
        game = "breathing"
    elif "envy" in text or "envious" in text:
        emotion = "envy"
        intensity = "resentful longing for what others have"
        quote = "Envy is the art of counting the other fellow’s blessings instead of your own."
        action = "Focus on your own journey and practice gratitude."
        game = "diary"
    elif "embarrass" in text or "embarrassed" in text or "awkward" in text:
        emotion = "embarrassment"
        intensity = "self-consciousness or awkwardness"
        quote = "Embarrassment is a sign you’re growing."
        action = "Laugh it off and remember everyone feels this way sometimes."
        game = "diary"
    elif "worry" in text or "worried" in text:
        emotion = "worry"
        intensity = "unease about a problem or outcome"
        quote = "Worrying does not take away tomorrow’s troubles, it takes away today’s peace."
        action = "Write down your worries and focus on what you can control."
        game = "breathing"
    elif "bored" in text:
        emotion = "boredom"
        intensity = "lack of interest or stimulation"
        quote = "Boredom is the space in which creativity begins."
        action = "Try a new hobby or call a friend."
        game = "ludo"
    elif "motivated" in text or "working" in text:
        emotion = "motivation"
        intensity = "strong desire to achieve or improve"
        quote = "Motivation is what gets you started. Habit is what keeps you going."
        action = "Set small, achievable goals to build momentum."
        game = "todo"
    else:
        emotion = "unknown"
        intensity = "emotion not recognized"
        quote = "Emotions are valid. Take care of yourself."
        action = "Reflect on your feelings or talk to someone you trust."
        game = None

    # Save to mood history
    mood_history.append({
        "input": user_input,
        "emotion": emotion,
        "intensity": intensity,
        "quote": quote,
        "action": action,
        "game": game
    })

    return jsonify({
        "status": "success",
        "emotion": emotion,
        "intensity": intensity,
        "quote": quote,
        "action": action,
        "game": game
    })


if __name__ == "__main__":
    app.run(debug=True)
