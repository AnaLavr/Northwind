import sqlite3

def supplier(): 
    conn=sqlite3.connect('Northwind_large.sqlite') 
    cur=conn.cursor()    
    cur.execute ('SELECT CompanyName, City, Country FROM  Supplier')  
    
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
