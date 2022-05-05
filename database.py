import sqlite3

def supplier(): 
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ('SELECT CompanyName, City, Country, Id FROM  Supplier')  
    column_names = []
    for column in cur.description:
        column_names.append(column[0])  
    rows=cur.fetchall() 
    dicts=[]
    for row in rows:
        d=dict(zip(column_names, row))
        dicts.append(d)  
    conn.close() 
    return dicts 

def products(supplier_id):
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ('SELECT CategoryId, ProductName, QuantityPerUnit, UnitPrice From Product Where SupplierId=?',(supplier_id,) )  
    column_names = []
    for column in cur.description:
        column_names.append(column[0])  
    rows=cur.fetchall() 
    dicts=[]
    for row in rows:
        d=dict(zip(column_names, row))
        dicts.append(d)   
    conn.close() 
    return dicts 
    
    
def supplier_name(supplier_id):
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ('SELECT CompanyName FROM Supplier WHERE Id=?',(supplier_id,) )  
    column_names = []
    for column in cur.description:
        column_names.append(column[0])  
    rows=cur.fetchall() 
    dicts=[]
    for row in rows:
        d=dict( zip(column_names, row))
        dicts.append(d)   
    conn.close() 
    return str(*row)


def category():
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute (""" SELECT Category.Id,Category.CategoryName,Category.Description,  COUNT(Product.ProductName)  AS "Product Count" FROM Category
                        INNER JOIN Product on Category.Id=Product.CategoryId
                        GROUP BY Product.CategoryId""" )  
    column_names = []
    for column in cur.description:
        column_names.append(column[0])  
    rows=cur.fetchall() 
    dicts=[]
    for row in rows:
        d=dict(zip(column_names, row))
        dicts.append(d)   
    conn.close() 
    return dicts 
    
def get_category_details(category_id):
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ("""SELECT  Product.CategoryId, Product.ProductName,Supplier.CompanyName FROM Product
                        INNER JOIN Supplier on Product.CategoryId= Supplier.Id
                        WHERE CategoryId=?""", (category_id,) )  
    column_names = []
    for column in cur.description:
        column_names.append(column[0])  
    rows=cur.fetchall() 
    dicts=[]
    for row in rows:
        d=dict(zip(column_names, row))
        dicts.append(d)   
    conn.close() 
    return dicts 


def catheader(category_id):
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ("""SELECT  CategoryName, Id    FROM Category
                        WHERE Id=?""", (category_id,) )  
   
    rows=cur.fetchmany()     #!!!! plus precise which row
    
    for row in rows:
        return row[0]        # precised here
         
    conn.close() 
   