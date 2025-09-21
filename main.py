import os
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app=Flask(__name__)


mysql=MySQL()


app.config['MYSQL_HOST']= os.environ.get('MYSQL_HOST','localhost')
app.config['MYSQL_PORT']=int(os.environ.get('MYSQL_PORT',3306))
app.config['MYSQL_USER']=os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD']=os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB']=os.environ.get('MYSQL_DB', 'dbcrud')
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')    
@app.route('/tarefas')  
def index_tarefas():

    sql="SELECT * FROM tarefas"
    conexao=mysql.connection
    cursor=conexao.cursor()
    cursor.execute(sql)
    tarefas=cursor.fetchall()
    conexao.commit()
    return render_template('modules/tarefas/index.html', tarefas=tarefas)

@app.route('/tarefas/create')
def create():
    return render_template('modules/tarefas/create.html')

@app.route('/tarefas/create/salvar', methods=['POST'])
def tarefas_salvar():
    nome=request.form['nome']
    data=request.form['data']
    status=request.form['status']

    sql="INSERT INTO tarefas (nome, data, status) VALUES (%s, %s, %s)"
    dados=(nome, data, status)
    conexao=mysql.connection
    cursor=conexao.cursor()
    cursor.execute(sql, dados)
    conexao.commit()
    return redirect('/tarefas')

@app.route('/tarefas/apagar/<int:id>')
def tarefas_apagar(id):
    conexao=mysql.connection
    cursor=conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id=%s",(id,))
    conexao.commit()
    return redirect ('/tarefas')

@app.route('/tarefas/edit/<int:id>')
def tarefas_editar(id):
    conexao=mysql.connection
    cursor=conexao.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE id=%s", (id,))
    tarefas=cursor.fetchone()
    conexao.commit()
    return render_template('/modules/tarefas/edit.html', tarefas=tarefas)

@app.route ('/tarefas/edit/atualizar', methods=['POST'])
def  tarefas_atualizar():
    id=request.form['txtid']
    nome=request.form['nome']
    data=request.form['data']
    status=request.form['status']

    sql="UPDATE tarefas SET nome=%s, data=%s, status=%s WHERE id=%s"
    dados=(nome, data, status, id)


    conexao=mysql.connection
    cursor=conexao.cursor()
    cursor.execute(sql,dados)
    conexao.commit()
    return redirect('/tarefas')




if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)