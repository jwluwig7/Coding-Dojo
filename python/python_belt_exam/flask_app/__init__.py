from flask import Flask, session

app = Flask(__name__)

app.secret_key = "password is password"

DATABASE = "python_belt_exam"