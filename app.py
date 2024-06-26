from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id_controller = 1

@app.route('/tasks', methods=['POST'])
def create_task():
   global task_id_controller
   data = request.get_json()
   new_task = Task(id=task_id_controller, title=data.get("title"), description=data.get("description", "Descrição Padrão"))
   tasks.append(new_task)
   task_id_controller += 1
   return jsonify({"message": "Tarefa criada com sucesso" })

if __name__=="__main__":
   app.run(debug=True)

