import json
from time import time
from flask import Flask, render_template, make_response
import random
#리얼할 것
app = Flask(__name__)

#   txt 데이터 읽어와서 넘기는 곳
def get_data():
    f=open('countData.txt','r')
    print(f)
    data=[]
    while True:
        line=f.readline()
        if not line:break
        data.append(int(line.strip()))
    print(data)
    return [[time()*1000,data[0]],[time()*1000,data[1]]] # [man],[woman]

def get_data2():
    f=open('ratingData.txt','r')
    print(f)
    data2=[]
    while True:
        line=f.readline()
        if not line:break
        data2.append(int(line.strip()))
    print(data2)
    return [[time()*1000,data2[0]],[time()*1000,data2[1]],[time()*1000,data2[2]],[time()*1000,data2[3]],[time()*1000,data2[4]],[time()*1000,data2[5]]] # [clothes],[devices],[perfume]



@app.route('/')
def hello_world():
    return render_template('real_time_chart.html', data='test')


@app.route('/live-data')
def live_data():
    #data 들어가는 부분
    #[ [남자]  ,[여자]  ]

    # data=[[time()*1000,random.randrange(1,100)],[time()*1000,random.randrange(1,30)]]
    data=get_data()

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/live-data2')
def live_data2():
    #data 들어가는 부분
    #[ [남자]  ,[여자]  ]

    # data=[[time()*1000,random.randrange(1,100)],[time()*1000,random.randrange(1,30)]]
    data2=get_data2()

    response2 = make_response(json.dumps(data2))
    response2.content_type = 'application/json'
    return response2



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)