from flask import Flask, render_template, jsonify, send_from_directory
import os
import glob

app = Flask(__name__)

# Keep track of the last sent image index
last_sent_index = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_latest_images")
def get_latest_images():
    global last_sent_index
    image_folder = "static/images"
    image_files = glob.glob(os.path.join(image_folder, "result_*.jpg"))

    # Extract camera name, timestamp, etc. from image file names
    # Modify this part based on your naming convention
    image_data = []
    for i in range(last_sent_index, len(image_files)):
        camera_name = "Camera 1"  # Extract camera name from image path
        timestamp = "2023-01-01 12:00:00"  # Extract timestamp from image path

        image_data.append(
            {
                "cameraName": camera_name,
                "timestamp": timestamp,
                "imageName": os.path.basename(image_files[i]),
            }
        )

    last_sent_index = len(image_files)

    return jsonify(image_data)


@app.route("/static/images/<path:filename>")
def static_images(filename):
    return send_from_directory("static/images", filename)

@app.route("/echalaan")
def echalaan():
    return render_template("echalaan_status.html")

@app.route("/lost")
def lostandfound():
    return render_template("lost_and_found.html")

@app.route("/peopleinmonument")
def peopleinmonument():
    return render_template("peopleinmonument.html")

@app.route("/litteringculprits")
def litteringculprits():
    return render_template("litteringculprits.html")



if __name__ == "__main__":
    app.run(debug=True)
