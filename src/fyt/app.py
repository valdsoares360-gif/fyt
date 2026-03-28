from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        output_path = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

        ydl_opts = {
            "outtmpl": output_path,
            "format": "best"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return send_file(filename, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)