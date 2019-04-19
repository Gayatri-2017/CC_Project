from flask import Flask, render_template, request, flash
import Synonyms

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)

app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=["GET","POST"])
def login_page():
    # flash("Hi")
    error = ''
    try:
        if request.method == "POST":
            inp = request.form['textbox']
            if inp != "" :
                flash(inp)
                out = list(Synonyms.synonyms(inp))
                print(out[0])
                flash(out[0])	
            else:
                error = "Enter Text."
        return render_template("tryTextBoxFancy.html", error = error)
    except Exception as e:
        flash(e)
        return render_template("tryTextBoxFancy.html", error = error)