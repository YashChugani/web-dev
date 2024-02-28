Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request, redirect, url_for
... import random
... app = Flask(_name_)
... ... 
... ... # In-memory data storage (Replace with a database in a production environment)
... ... quizzes = {}
... ... users = {}
... ... 
... ... @app.route('/')
... ... def home():
... ...     return render_template('index.html')
... ... 
... ... # Quiz Creation
... ... @app.route('/create_quiz', methods=['GET', 'POST'])
... ... def create_quiz():
... ...     if request.method == 'POST':
... ...         title = request.form['title']
... ...         questions = request.form.getlist('question')
... ...         options = request.form.getlist('options')
... ...         correct_answers = request.form.getlist('correct_answer')
... ...         
... ...         quiz_id = random.randint(1000, 9999)
... ...         quizzes[quiz_id] = {'title': title, 'questions': []}
... ...         
... ...         for q, o, a in zip(questions, options, correct_answers):
... ...             quizzes[quiz_id]['questions'].append({'question': q, 'options': o.split(','), 'correct_answer': a})
... ...         
... ...         return redirect(url_for('share_quiz', quiz_id=quiz_id))
... ...     
... ...     return render_template('create_quiz.html')
... ... 
... ... # Quiz Sharing
... ... @app.route('/share_quiz/<int:quiz_id>')
... ... def share_quiz(quiz_id):
... ...     return render_template('share_quiz.html', quiz_id=quiz_id)
... 
... # Quiz Taking
... @app.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
... def take_quiz(quiz_id):
...     if request.method == 'POST':
...         answers = request.form.getlist('answer')
...         score = 0
...         
        for qid, ans in zip(range(len(quizzes[quiz_id]['questions'])), answers):
            if ans == quizzes[quiz_id]['questions'][qid]['correct_answer']:
                score += 1
        
        return render_template('result.html', score=score, total=len(quizzes[quiz_id]['questions']))
    
    return render_template('take_quiz.html', quiz=quizzes[quiz_id])

