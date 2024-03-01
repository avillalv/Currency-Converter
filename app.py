from flask import Flask, render_template, request, jsonify
from currency_converter import CurrencyConverter

app = Flask(__name__)

''' 
    When URL loads --> .index()
    returns --> index.html
'''
@app.route("/")
def index():
    return render_template("index.html")



''' When formed is submitted --> .convert()
    returns --> {results: <result_message>}

'''
@app.route("/convert", methods=["POST"])
def convert():
    from_currency = request.form.get("from_currency")
    to_currency = request.form.get("to_currency")

    # To check if input is numeric. If not, returns {error: <message>}
    try:
        amount = float(request.form.get("amount"))

    except ValueError as e:
        error_message = "Please enter a valid numeric amount."
        return jsonify({"error": error_message})

    currency_converter = CurrencyConverter()
    converted_amount = currency_converter.convert(amount, from_currency, to_currency)

    result_text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    return jsonify({"result": result_text})



if __name__ == "__main__":
    app.run() #host="0.0.0.0", port=5000
