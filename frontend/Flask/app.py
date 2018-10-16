from flask import Flask
from flask import render_template,jsonify,request
import requests
from pprint import pprint

app = Flask(__name__)
#app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat',methods=['POST'])
def chat():
    ##try:
        user_message = request.form["text"]
        print(user_message)
        user_query = '{"query":"'+user_message+'"}'
        ##print(user_query)

        response = requests.post("http://localhost:5005/conversations/N/respond",user_query)
        pprint(response.content)
        value= response.json()
        pprint(value[0]['text'])
        return jsonify({"status":"success","response":value[0]['text']})
        #return 'OK'
    ##except Exception as e:
        ##print(e)
        ##return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)