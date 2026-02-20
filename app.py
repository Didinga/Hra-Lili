from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "lili_magie_2026"

SCENES = {
    "forest": {
        "text": "🌲 Lili vstupuje do stříbrného lesa. Ve tmě blikají světélka...",
        "background": "images/forest.jpg",
        "choices": [
            {"text": "Jít za světélkem", "next": "fairy"},
            {"text": "Prozkoumat stopy", "next": "goblin"}
        ]
    },

    "fairy": {
        "text": "🧚 Tajemná víla vystupuje ze světla a žádá o pomoc.",
        "background": "images/fairy.jpg",
        "choices": [
            {"text": "Pomoci víle", "next": "riddle"}
        ]
    },

    "goblin": {
        "text": "🍄 Skřítek hlídá kouzelný kámen.",
        "background": "images/goblin.jpg",
        "choices": [
            {"text": "Promluvit se skřítkem", "next": "riddle"}
        ]
    },

    "riddle": {
        "text": "✨ Hádanka: Co má klíče, ale neotevírá dveře?",
        "background": "images/riddle.jpg",
        "choices": [
            {"text": "Odpovědět: Klavír", "next": "end"},
            {"text": "Nevím", "next": "forest"}
        ]
    },

    "end": {
        "text": "👑 Lili se stává Ochránkyní stříbrného lesa!",
        "background": "images/end.jpg",
        "choices": [
            {"text": "Hrát znovu", "next": "forest"}
        ]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["scene"] = "forest"
        return redirect(url_for("game"))
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    if "scene" not in session:
        session["scene"] = "forest"

    if request.method == "POST":
        next_scene = request.form.get("next")
        session["scene"] = next_scene
        return redirect(url_for("game"))

    scene_id = session["scene"]
    scene = SCENES[scene_id]

    return render_template("scene.html", scene=scene)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

