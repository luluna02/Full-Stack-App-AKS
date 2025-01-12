from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'task'  
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    done = db.Column(db.Boolean)

    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def json(self):
        return {
            'id': self.id,
            'task': self.task,
            'done': self.done
        }

@app.route('/')
def home():
    return make_response(jsonify({'message': "App works"}), 200)

@app.route('/tasks', methods=['GET'])
def index():
    tasks = Task.query.all()  
    return make_response(jsonify({'message': [task.json() for task in tasks]}), 200)

@app.route('/tasks',methods =['POST'])
def creat_task():
    try:
        data = request.get_json()
        new_user = Task(task=data['task'], done=data.get('done', False))
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user'}), 500)
    

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    try:
        task = Task.query.filter_by(id=id).first()
        if task:
            return make_response(jsonify({'task': task.json()}), 200)
        return make_response(jsonify({'message': 'Task not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error getting task', 'error': str(e)}), 500)
    

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        task = Task.query.filter_by(id=id).first()
        if task:
            data = request.get_json()
            if 'task' in data:
                task.task = data['task']
            if 'done' in data:
                task.done = data['done']
            db.session.commit()
            return make_response(jsonify({'message': 'Task updated', 'task': task.json()}), 200)
        return make_response(jsonify({'message': 'Task not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error updating task', 'error': str(e)}), 500)


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.filter_by(id=id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return make_response(jsonify({'message': 'Task deleted'}), 200)
        return make_response(jsonify({'message': 'Task not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error deleting task', 'error': str(e)}), 500)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



