# Simple Flask Frontend for Bank Account Project

from flask import Flask, render_template_string, request

app = Flask(__name__)

class BankAccount:
    def __init__(self, current_balance):
        self.current_balance = current_balance

    def check_balance(self):
        return self.current_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            return True
        return Falsei
    def transfer(self, recipient, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            recipient.deposit(amount)
            return True
        return False

account = BankAccount(1000)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Bank Account App</title>
<style>
body { font-family: Arial; text-align:center; margin-top:50px }
.container { width:300px; margin:auto }
button { padding:10px; margin:5px }
input { padding:8px; width:90% }
</style>
</head>
<body>
<h2>Simple Bank Account</h2>
<div class="container">
<p><b>Current Balance:</b> {{balance}}</p>

<form method="post" action="/deposit">
<input type="number" name="amount" placeholder="Deposit Amount" required>
<br>
<button type="submit">Deposit</button>
</form>

<form method="post" action="/withdraw">
<input type="number" name="amount" placeholder="Withdraw Amount" required>
<br>
<button type="submit">Withdraw</button>
</form>

<h3>Transfer Money (Account1 ➜ Account2)</h3>
<form method="post" action="/transfer">
<input type="number" name="amount" placeholder="Transfer Amount" required>
<br>
<button type="submit">Transfer</button>
</form>

</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, balance=account.check_balance())

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = int(request.form['amount'])
    account.deposit(amount)
    return render_template_string(HTML, balance=account.check_balance())

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = int(request.form['amount'])
    account.withdraw(amount)
    return render_template_string(HTML, balance=account.check_balance())

if __name__ == '__main__':
    app.run(debug=True)

