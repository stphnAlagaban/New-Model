from flask import Flask, request, jsonify

from GreenBot import chatWithBot

app = Flask(__name__)

@app.route('/chat', methods = ['GET', 'POST'])

def chatBot():
    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=chatWithBot(chatInput))


if __name__ == '__main__':
    app.run(host='192.168.18.237', debug=True)