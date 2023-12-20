from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ticket():

    extracted_info = {
        "name": "Gops",
        "id_number": "1234 5678 9012",
        "dob": "01/01/1990",
        "address": "Sample Address",
        "person_image_path": "static/person_image.jpg",
    }

    return render_template("tix.html", extracted_info=extracted_info)


if __name__ == "__main__":
    app.run(debug=True)
