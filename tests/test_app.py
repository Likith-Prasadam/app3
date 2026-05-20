import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..'
        )
    )
)

from app import app, tasks

def setup_function():
    tasks.clear()

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_add_task():
    client = app.test_client()
    response = client.post('/add', data={
        'task': 'Study'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 1

def test_complete_task():
    tasks.append({
        'name': 'Study',
        'completed': False
    })
    client = app.test_client()
    response = client.get('/complete/0', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] == True

def test_delete_task():
    tasks.append({
        'name': 'Study',
        'completed': False
    })
    client = app.test_client()
    response = client.get('/delete/0', follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 0

def test_task_length_validation():
    client = app.test_client()
    response = client.post('/add', data={
        'task': 'abcdefghijklmnop'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Task must not exceed 10 characters" in response.data

