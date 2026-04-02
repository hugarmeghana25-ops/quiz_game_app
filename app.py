from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "Who developed Python?",
        "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
      
    score = 0

    if request.method == "POST":
        for i in range(len(questions)):
            selected = request.form.get(f"q{i}")
            
            if selected == questions[i]["answer"]:
                score += 1
        return render_template("index.html", questions=questions, score=score)

    return render_template("index.html", questions=questions, score=None)

if __name__ == "__main__":
    app.run(debug=True)