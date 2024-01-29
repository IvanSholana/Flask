from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    list_penjualan = [
    {"nama_barang": "Laptop", "harga": 1200, "jumlah": 5, "total": 6000},
    {"nama_barang": "Smartphone", "harga": 800, "jumlah": 8, "total": 6400},
    {"nama_barang": "Printer", "harga": 300, "jumlah": 3, "total": 900},
    {"nama_barang": "Mouse", "harga": 20, "jumlah": 10, "total": 200},
    {"nama_barang": "Keyboard", "harga": 30, "jumlah": 7, "total": 210}
]
    return render_template('market.html', items=list_penjualan)

@app.route("/about/<username>")
def about_page(username):
    return f"<p>hallo {username}</p>"
    