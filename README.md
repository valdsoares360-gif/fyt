# Flask YouTube Downloader

A simple web application to download YouTube videos using Flask and yt-dlp.

## 🚀 Technologies

* Python
* Flask
* yt-dlp
* HTML
* Poetry (dependency management)

## 📌 Features

* Paste a YouTube video URL
* Download video automatically
* Direct download through browser
* Simple interface

## 📂 Project Structure

```
fyt/
│
├── src/
│   └── fyt/
│       ├── app.py
│       └── templates/
│           └── index.html
│
├── downloads/
├── pyproject.toml
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/valdsoares360-gif/fyt.git
```

Go to the project folder:

```bash
cd fyt
```

Install dependencies using Poetry:

```bash
poetry install
```

Activate the environment:

```bash
poetry shell
```

## ▶️ Running the project

```bash
python src/fyt/app.py
```

Open in your browser:

```
http://localhost:5000
```

## 🧠 How it works

The application receives a YouTube video URL, uses `yt-dlp` to download the video, and returns the file directly to the user.

## 📷 Usage

1. Paste the video URL
2. Click download
3. The download starts automatically

## 📄 License

This project is for educational purposes only.
