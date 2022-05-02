from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def northwind():
    facts=database.supplier()
    return render_template ('index.html', facts=facts )
 
@app.route('/products/<int:supplier_id>')
def products(supplier_id):
    products =database.products(supplier_id)
    header=database.supplier_name(supplier_id)
    return render_template ('products.html', products=products,header=header )
 