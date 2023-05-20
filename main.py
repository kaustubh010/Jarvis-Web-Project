from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from Bard import Chatbot

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://ribhu:8824854410Ka@ribhu.gji8rri.mongodb.net/Jarvis"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats= mongo.db.Chats.find({})
    myChats = [chat for chat in chats]
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    data = {}
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.Chats.find_one({"question": question})
        if chat:
            data = {"result": f"{chat['solution']}"}
            return jsonify(data)
        else:
            token = "WggUu-JOGF9Ts5EXUAgGe0H26qyDbvALsmc1YQV1FC3yKeUnENonxDp9onmxILLhzsHgEg."
            chatbot = Chatbot(token)
            solution = chatbot.ask(question)
            data = {"result": solution['content']}
            mongo.db.Chats.insert_one({"question": question, "solution": f"{solution['content']}"})
            return jsonify(data)
        
    return jsonify(data)