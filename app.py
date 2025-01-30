# app.py
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'gizli_anahtar_123'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
        session['attempts'] = 0
    
    message = None
    if request.method == 'POST':
        guess = int(request.form.get('guess', 0))
        session['attempts'] += 1
        
        if guess < session['target_number']:
            message = f"{guess} sayısı, tuttuğum sayıdan daha düşük. Daha yüksek bir sayı deneyin"
        elif guess > session['target_number']:
            message = f"{guess} sayısı, tuttuğum sayıdan daha yüksek. Daha düşük bir sayı deneyin"
        else:
            message = f"Tebrikler! {session['attempts']} denemede bildiniz!"
            
    return render_template('index.html', message=message)

@app.route('/new-game')
def new_game():
    session.pop('target_number', None)
    session.pop('attempts', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
