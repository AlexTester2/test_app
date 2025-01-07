# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data: columns and tasks
board = {
    "To Do": ["Task 1", "Task 2"],
    "In Progress": ["Task 3"],
    "Done": []
}

@app.route('/')
def index():
    return render_template('board.html', board=board)

@app.route('/add_task', methods=['POST'])
def add_task():
    column = request.form['column']
    task = request.form['task']
    if column in board and task:
        board[column].append(task)
    return redirect(url_for('index'))

@app.route('/move_task', methods=['POST'])
def move_task():
    task = request.form['task']
    from_column = request.form['from_column']
    to_column = request.form['to_column']

    if task in board.get(from_column, []) and to_column in board:
        board[from_column].remove(task)
        board[to_column].append(task)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
