from flask import Flask, jsonify
import sqlite3
import ast


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def test():
    return "Everything is work !"


@app.route("/getAllImage", methods=['GET'])
def getAllImage():
    con = sqlite3.connect('mydatabase.db')
    # SELECT TABLE
    data = []
    for row in con.execute('''SELECT * from ptt_beauty'''):
        data.append({'title': row[1], "urls": ast.literal_eval(row[2]), "date": row[3]})
    con.close()
    print(data)
    response = jsonify({'msg': data})
    return response


if __name__=="__main__":
    app.run(host='0.0.0.0')