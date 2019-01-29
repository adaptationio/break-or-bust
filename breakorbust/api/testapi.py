from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from utilities import DataTransforms
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)
import numpy as np

DATA = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

ACTIONS = {
    'buy': "buy"
}
temp = []
dictlist = []
def dictolist():
    for key, value in args.iteritems():
        temp = [key,value]
        dictlist.append(temp)
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('data1')
parser.add_argument('data2')

response = {
    'record': 'data recorded',
    'predict': 'pretict action'
}
test = DataTransforms()
def data_converted(data):
        data_converted  = []
        data1 = data['data1']
        data2 = data['data2']
        data_converted.append([data1, data2])
            #data_converted.append([i['volume'], i['time'],i['mid']['c'], i['mid']['h'], i['mid']['l'], i['mid']['o']])
        return data_converted
# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class Record(Resource):
    def get(self):
        return response['record']

    def post(self):
        args = parser.parse_args()
        data = data_converted(args)
        data = test.toarray(data)
        #data2 = np.zeros((1, 1, 1))
        #data2[0][0]= data
        print(data)
        test.tocsv_single(data,'test_data.csv')
        #return args['task']
        return args

class Predict(Resource):
    def get(self):
        return response['preditc']

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Record, '/record')
api.add_resource(Predict, '/predict')


if __name__ == '__main__':
    app.run(debug=True)