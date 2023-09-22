from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("home.html")

@app.route('/bitcoins', methods = ["GET","POST"])
def coins():
    if request.method == "POST":
        coin = request.form.get("coin")
        crypto_currency =  requests.get("http://api.coinlayer.com/live?access_key=bd95fd28cf0e49d9fe5b658dd3fba2db")

        success = crypto_currency.json().get("success")
        target = crypto_currency.json().get("target")
        rate=crypto_currency.json().get("rates")
        if coin in rate:
            data=rate[coin]

        return render_template ("index.html",box=data,success=success,target=target,coin=coin)
    return render_template ("index.html")

@app.route('/result')
def result():
    return render_template ("result.html")

if __name__ == "__main__":
    app.run(debug=True)






