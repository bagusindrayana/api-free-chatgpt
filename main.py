from flask import Flask, jsonify,request
import os
import gpt4free
from gpt4free import Provider, forefront

app = Flask(__name__)


@app.get('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.post('/prompt')
def sendPrompt():
    # get args
    _model = request.args.get('model')
    _prompt_text = request.form.get('prompt')

    if _model == "forefront":
        token = forefront.Account.create(logging=False)
        response = gpt4free.Completion.create(
            Provider.ForeFront, prompt='Write a poem on Lionel Messi', model='gpt-4', token=token
        )
    elif _model == "theb":
        response = gpt4free.Completion.create(Provider.Theb, prompt=_prompt_text)
    else :
        response = gpt4free.Completion.create(Provider.You, prompt=_prompt_text)
    result = response
    return jsonify({
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
