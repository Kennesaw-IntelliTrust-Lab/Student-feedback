from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Replace with a secure key
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Mock data for course materials and personalized content
course_materials = [
    {"title": "Introduction to AI", "content": "Learn the fundamentals of Artificial Intelligence."},
    {"title": "Data Science with Python", "content": "Understand data analysis and visualization using Python."},
]

personalized_content = [
    "Advanced exercises in AI.",
    "Specialized topics: Deep Learning and Neural Networks.",
    "Capstone Project: Build a data pipeline."
]

# Routes
@app.route("/")
def home():
    return render_template("index.html", materials=course_materials)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        video_file = request.files.get("video")
        doc_file = request.files.get("document")
        
        if video_file:
            video_path = os.path.join(app.config["UPLOAD_FOLDER"], video_file.filename)
            video_file.save(video_path)
            flash(f"Video uploaded: {video_file.filename}")
        
        if doc_file:
            doc_path = os.path.join(app.config["UPLOAD_FOLDER"], doc_file.filename)
            doc_file.save(doc_path)
            flash(f"Document uploaded: {doc_file.filename}")
        
        return redirect(url_for("upload"))
    
    return render_template("upload.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback_text = request.form.get("feedback")
        # Save or process feedback here
        flash("Feedback submitted successfully!")
        return redirect(url_for("feedback"))
    
    return render_template("feedback.html")

@app.route("/personalized")
def personalized():
    return render_template("personalized.html", personalized=personalized_content)

if __name__ == "__main__":
    app.run(debug=True)
