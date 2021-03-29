from flask import Flask,jsonify
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)


#consula a base de datos 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'arb'
mysql = MySQL(app)

@app.route('/cp/<c_CP>',methods=['GET','POST'])
def cp(c_CP):
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cur.execute('''SELECT * FROM codigo_postal_mexico where c_CP = %s '''(c_CP))
   
   rv = cur.fetchall()
   employee = []
   content = {}
   for result in rv:
       content = {
                  'id': result['id'], 
                  'd_codigo': result['d_codigo'], 
                  'd_asenta': result['d_asenta'], 
                  'd_tipo_asenta': result['d_tipo_asenta'], 
                  'D_mnpio': result['D_mnpio'], 
                  'd_estado': result['d_estado'], 
                  'd_ciudad': result['d_ciudad'], 
                  'd_CP': result['d_CP'], 
                  'c_estado': result['c_estado'], 
                  'c_oficina': result['c_oficina'], 
                  'c_CP': result['c_CP'], 
                  'c_tipo_asenta': result['c_tipo_asenta'], 
                  'c_mnpio': result['c_mnpio'],
                  'id_asenta_cpcons': result['id_asenta_cpcons'], 
                  'd_zona': result['d_zona'],
                  'c_cve_ciudad': result['c_cve_ciudad'],
                  }
       employee.append(content)
       content = {}
   return jsonify(employee) 

'''@app.route('/codigo',methods=['GET','POST'])
def cp():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cur.execute(''''SELECT * FROM codigo_postal_mexico  '''')
   
   rv = cur.fetchall()
   employee = []
   content = {}
   for result in rv:
       content = {
                  'id': result['id'], 
                  'd_codigo': result['d_codigo'], 
                  'd_asenta': result['d_asenta'], 
                  'd_tipo_asenta': result['d_tipo_asenta'], 
                  'D_mnpio': result['D_mnpio'], 
                  'd_estado': result['d_estado'], 
                  'd_ciudad': result['d_ciudad'], 
                  'd_CP': result['d_CP'], 
                  'c_estado': result['c_estado'], 
                  'c_oficina': result['c_oficina'], 
                  'c_CP': result['c_CP'], 
                  'c_tipo_asenta': result['c_tipo_asenta'], 
                  'c_mnpio': result['c_mnpio'],
                  'id_asenta_cpcons': result['id_asenta_cpcons'], 
                  'd_zona': result['d_zona'],
                  'c_cve_ciudad': result['c_cve_ciudad'],
                  }
       employee.append(content)
       content = {}
   return jsonify(employee) '''

if __name__ == '__main__':
    app.run(host='127.0.0.3',port ='9200', debug=False)