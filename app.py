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
 
 
@app.route('/categories') 
def categories():
    category=database.category()            
    return render_template ('categories.html', category=category )

@app.route('/categories/<int:category_id>')
def catdetails(category_id):
    header = database.catheader(category_id)
    details =database.get_category_details(category_id)
    return render_template ('catdetails.html', details=details, header=header)