from flask import Flask, render_template, request, redirect # type: ignore

app = Flask(__name__)

tasks = []
error = ""

@app.route('/')
def home():

    return render_template(
        'index.html',
        tasks=tasks,
        error=error
    )

@app.route('/add', methods=['POST'])
def add_task():

    global error

    task = request.form['task']

    # Validation

    if len(task) > 10:

        error = "Task must not exceed 10 characters"

        return redirect('/')

    error = ""

    if task:

        tasks.append({
            'name': task,
            'completed': False
        })

    return redirect('/')

@app.route('/complete/<int:index>')
def complete_task(index):

    tasks[index]['completed'] = True

    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):

    tasks.pop(index)

    return redirect('/')

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )