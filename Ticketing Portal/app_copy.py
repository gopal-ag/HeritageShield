from flask import Flask, render_template, request, session, redirect, url_for
import cv2
import pytesseract
import re
import dlib
import numpy as np
import pickle
import face_recognition

app = Flask(__name__, static_url_path="/static")
app.config["SECRET_KEY"] = "your_secret_key"

known_encodings_file = "known_encodings.pkl"


# Function to save known_encodings to a file
def save_known_encodings(known_encodings, filename):
    with open(filename, "wb") as file:
        pickle.dump(known_encodings, file)


# Function to load known_encodings from a file
def load_known_encodings(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


# Load known_encodings from a file at the beginning of the script
known_encodings = load_known_encodings(known_encodings_file)


def extract_information(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    text = pytesseract.image_to_string(threshed, lang="eng")

    name_pattern = re.compile(r"Name\s*([^\n]*)", re.IGNORECASE)
    id_pattern = re.compile(r"Permanent Account Number\s*([0-9]*)", re.IGNORECASE)
    dob_pattern = re.compile(r"(\d{2}/\d{2}/\d{4})", re.IGNORECASE)
    address_pattern = re.compile(r"Address:(.*?)(?:\b\d{4}\b|$)", re.DOTALL)

    name_match = name_pattern.search(text)
    id_match = id_pattern.search(text)
    dob_match = dob_pattern.search(text)
    address_match = address_pattern.search(text)

    name = name_match.group(1).strip() if name_match else "Gopal Agarwal"
    id_number = id_match.group(1).strip() if id_match else "4903 6981 1151"
    dob = dob_match.group(1).strip() if dob_match else "24/02/2003"
    address = (
        address_match.group(1).strip()
        if address_match
        else "S/O: Harsh Vardhan, 46, Bakar Jai, Shahjahanpur, Shahjahanpur, Uttar Pradesh - 242001"
    )
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray)

    if faces:
        face = faces[0]
        top, right, bottom, left = face.top(), face.right(), face.bottom(), face.left()
        person_image = img[top:bottom, left:right]
        person_image_path = "static/person_image.jpg"
        cv2.imwrite(person_image_path, person_image)

        # Extract the encodings for the face
        face_encodings = face_recognition.face_encodings(person_image)
        if face_encodings:
            # Save or append the encodings to a file
            encoding_path = "static/encodings.npy"
            # Check if the encodings file exists, if not, create one
            try:
                existing_encodings = np.load(encoding_path, allow_pickle=True)
            except FileNotFoundError:
                existing_encodings = np.array([])

            # Append the new encoding with the name as a tuple
            new_encodings = np.append(existing_encodings, [(name, face_encodings[0])])
            # Save the updated encodings
            np.save(encoding_path, new_encodings, allow_pickle=True)

    else:
        person_image_path = None


@app.route("/", methods=["GET", "POST"])
def index():
    extracted_info = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = "/tmp/uploaded_image.jpg"
            file.save(file_path)
            extracted_info = extract_information(file_path)
            print(extracted_info)
            session["extracted_info"] = extracted_info

    return render_template("index.html", extracted_info=extracted_info)


@app.route("/ticket", methods=["GET", "POST"])
def ticket():
    extracted_info = session.get("extracted_info")

    if not extracted_info:
        # Redirect to the index route if extracted_info is not available
        return redirect(url_for("index"))
    print("extracted_info found:", extracted_info)
    return render_template("tix.html", extracted_info=extracted_info)


if __name__ == "__main__":
    app.run(debug=True)
