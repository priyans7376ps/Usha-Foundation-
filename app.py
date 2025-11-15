from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# NGO Information
NGO_NAME = "Usha Foundation"
FOUNDER = "Akash Singh"
ADDRESS = "Azmgarh, Sardhana Bazar, UP - 276139"
CONTACT = "8076315417"

# Home Page
@app.route('/')
def home():
    return render_template("index.html",
                           ngo_name=NGO_NAME,
                           founder=FOUNDER,
                           address=ADDRESS,
                           contact=CONTACT)

# Donate Page
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']
        # Yaha Razorpay / PayPal API integrate kar sakte ho
        return redirect(url_for('success', donor=name, amount=amount))
    return render_template("donate.html")

# Success Page
@app.route('/success')
def success():
    donor = request.args.get('donor')
    amount = request.args.get('amount')
    return render_template("success.html", donor=donor, amount=amount)

if __name__ == "__main__":
    app.run(debug=True)
