import os
from flask import Flask, render_template, send_from_directory,request, redirect, flash,url_for,session
import chatbot3 as cb
# import pySQLcase as case
import summary as summ
import csv
from flask_session import Session
app = Flask(__name__)

# Define the folder where your PDF files are stored
pdf_folder = "\\PDFs\\"  # Create a folder named "pdfs" and place your PDF files inside

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def home():
    return render_template('entry_point.html')

@app.route('/chatbot',methods=['GET', 'POST'])
def chatbot():
    while True:
        if request.method== "POST":
            user_input = request.form["input"]
            if user_input.lower() == "exit":
                    break
    response = cb.chatbot_response(user_input)
    return response;

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    with open("sample.csv", mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))

    flash('Invalid username or password. Please try again.', 'error')
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open("sample.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username:
                    flash('Username already exists. Please choose a different username.', 'error')
                    return redirect(url_for('signup'))

        with open("sample.csv", mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')

@app.route("/summary",methods=['GET', 'POST'])
def summary():
    selected_article= request.form["article"]
    result=summ.get_article_summary(selected_article)
    return result

@app.route("/casinfo",methods=['GET', 'POST'])
def casinfo():
    if 'username' in session:
        username = session['username']
    
    result=case.Show_Case_Info(username)
    return result

@app.route('/FIR')
def firpdf():
    # List all PDF files in the folder
    pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]
    return render_template('fir.html', pdf_files=pdf_files)

@app.route('/FIR/pdf/<filename>')
def serve_pdf(filename):
    try:
        # Serve the selected PDF file from the specified folder
        return send_from_directory(pdf_folder, filename)
    except FileNotFoundError:
        return "PDF not found", 404

if __name__ == '__main__':
    app.run(debug=True)
