from flask import Flask,jsonify, json, request
import pymongo


app = Flask(__name__)

with open("../resource/student_data.json", "r") as fr:
    content = fr.read()
    t = content.split("\n")
    p = [json.loads(i) for i in t if len(i) > 0]
    print(p)

def connect_to_mongodb():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient
def insert_into_mongodb(myclient):
    data = request.get_json()
    print(data)
    p.append(data)
    myclient = connect_to_mongodb()
    stdb = myclient["student_db"]
    stcol = stdb["students"]


    #for i in stcol.find():
    #    print(i)


@app.route('/', methods=['GET'])
def get_student_date():
    r = read_from_file("student_data.json")
    p = insert_into_mongodb(myclient)
    return jsonify()

@app.route('/getbyname/<string:name>', methods=['GET'])
def get_student_by_name(name):
    data = None
    for i in st:
        if i["name"] == name:
            data = i
            return jsonify(data)




if __name__ =='__main__':
    myclient = connect_to_mongodb()
    insert_into_mongodb(myclient)
    app.run()

