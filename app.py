from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

# Changed methods to POST and adjusted function accordingly
@app.route('/delete/<int:id>', methods=['POST'])  
def delete(id):
    if id >=0 and id< len(notes):  
        notes.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
