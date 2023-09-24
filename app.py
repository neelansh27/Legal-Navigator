import os
from flask import Flask, render_template, send_from_directory,request, redirect, flash,url_for,session
from flask_sqlalchemy import SQLAlchemy
import chatbot3 as cb
# import pySQLcase as case
import summary as summ
import csv
from flask_session import Session
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("URI")
db = SQLAlchemy(app)

# Models
class case(db.Model):
    __tablename__='case'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(30))
    judge=db.Column(db.String(40))
    accused=db.Column(db.String(40))
    defendant_lawyer=db.Column(db.String(40))
    petitioner=db.Column(db.String(40))
    prosecution_lawyer=db.Column(db.String(40))
    description=db.Column(db.String(1200))
    court_name=db.Column(db.String(40))
    status=db.Column(db.String(40))
    filing=db.Column(db.Date)
    next_trail=db.Column(db.Date)

class hearing(db.Model):
    __tablename__="hearing"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    hdate=db.Column(db.Date)
    summary=db.Column(db.String(800))
    case_id=db.Column(db.Integer,db.ForeignKey('case.id'),nullable=False)

    

    
print("connected")
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

@app.route("/caseList")
def caseInfo():
    cases=case.query.all()
    return render_template('cases_list.html',cases=cases)

@app.route("/caseDetails/<id>")
def caseDetails(id):
    cases=case.query.filter_by(id=id).all()
    hear=hearing.query.filter_by(case_id=id).all()
    return render_template('case_details.html',case=cases[0],hearing=hear)

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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
