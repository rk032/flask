from flask import Flask, request

app = Flask(__name__)

student ={
    "1" : {"name" : "asdfg","roll no" : "1234"},
    "2":{"name":"aweyu","roll no":"1235"},
    "3":{"name":"vcbn","roll no":"1236"}
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/students")
def f():
    return student

@app.route("/students/<rollno>")
def f1(rollno):
    temp = {}
    #for key,value in student.items():
     #   if value["roll no"]==rollno:
      #      temp=key
    #return  student[temp]
    for i in student:
        if student[i]["roll no"]==rollno:
            return student[i]

@app.route("/insert", methods =["POST"])
def insert():
    if request.method=="POST":
        for key,value in request.json.items():
            print(key,value)
            student[key]=value
    return student

if __name__=='__main__':
    app.run()