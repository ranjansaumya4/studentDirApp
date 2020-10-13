from flask import Flask, request, render_template
from read_data import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    params = [int(x) for x in request.form.values()]
    print(params[0])
    result = getData(params[0])
    print(result[0])
    return render_template('index.html', result_data=result)


@app.route("/createRecord", methods=['POST'])
def createRecord():
    params = [x for x in request.form.values()]
    print(params)
    params[0] = int(params[0])
    print(params)
    createRow(params)
    #result = getData(params[0])
    # print(result[0])
    isCreated = True
    return render_template('index.html', is_record_created=isCreated)


if __name__ == "__main__":
    app.run()
