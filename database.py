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
    cur.execute ('SELECT ProductName, QuantityPerUnit, UnitPrice From Product Where SupplierId=?',(supplier_id,) )  
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