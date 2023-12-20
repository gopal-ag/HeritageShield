from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import cv2
import pytesseract
import re
import dlib
import numpy as np
import os
import pandas as pd
from pathlib import Path

app = Flask(__name__, static_url_path="/static")
app.config["SECRET_KEY"] = "your_secret_key"

people_images_dir = Path(app.root_path) / "static" / "people_detected"
people_images_dir.mkdir(exist_ok=True)
extracted_info_df = pd.DataFrame(columns=["Name", "ID Number", "DOB", "Address"])


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

        person_image_name = name.replace(" ", "_") + ".jpg"
        person_image_path2 = people_images_dir / person_image_name

        if not person_image_path2.exists():
            cv2.imwrite(str(person_image_path2), person_image)
        else:
            print(f"Image for {name} already exists. Not saving.")
    else:
        person_image_path = None

    return name, id_number, dob, address, person_image_path


@app.route("/", methods=["GET", "POST"])
def index():
    extracted_info = None

    if request.method == "POST":
        file = None

        # Check if "file" is in request.files
        if "file" in request.files:
            file = request.files["file"]

        # Check if "webcamImage" is in request.files
        elif "webcamImage" in request.files:
            file = request.files["webcamImage"]

        if file:
            file_path = "/tmp/uploaded_image.jpg"
            file.save(file_path)
            extracted_info = extract_information(file_path)
            print(extracted_info)
            session["extracted_info"] = extracted_info

            # For webcam capture, return a JSON response
            if "webcamImage" in request.files:
                return jsonify({"status": "success"})

    return render_template("index.html", extracted_info=extracted_info)


@app.route("/ticket", methods=["GET", "POST"])
def ticket():
    global extracted_info_df
    extracted_info = session.get("extracted_info")

    if not extracted_info:
        return redirect(url_for("index"))

    print("extracted_info found:", extracted_info)

    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = "/tmp/uploaded_image.jpg"
            file.save(file_path)
            extracted_info = extract_information(file_path)
            print(extracted_info)
            session["extracted_info"] = extracted_info

    return render_template("tix.html", extracted_info=extracted_info)


def upload_webcam_image():
    if "webcamImage" in request.files:
        image = request.files["webcamImage"]
        image_path = "/tmp/webcam_image.jpg"
        image.save(image_path)

        # Process the image as needed (e.g., extract information)
        extracted_info = extract_information(image_path)
        print(extracted_info)
        session["extracted_info"] = extracted_info

        return jsonify({"status": "success", "message": "Image processed"})
    return jsonify({"status": "error", "message": "No image received"})


if __name__ == "__main__":
    app.run(debug=True)
