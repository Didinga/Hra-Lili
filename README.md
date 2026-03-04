# Hra Lili

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)

A browser-based text adventure game built with Python and Flask. The player guides Lili through a branching story with multiple paths and endings.

---

## Features

- Browser-based gameplay â€” no installation needed for players
- Branching story with multiple paths and endings
- Session-based progress tracking
- Background images for each scene
- Easy to extend with new scenes

---

## Getting Started

### Prerequisites

```bash
pip install flask
```

### Installation

```bash
git clone https://github.com/Didinga/Hra-Lili.git
cd Hra-Lili
```

### Run

```bash
python app.py
```

Then open your browser at `http://localhost:5000`

---

## Project Structure

```
Hra-Lili/
â”śâ”€â”€ app.py              # Flask app and story scenes
â”śâ”€â”€ templates/
â”‚   â”śâ”€â”€ index.html      # Start screen
â”‚   â””â”€â”€ scene.html      # Game screen
â””â”€â”€ static/
    â””â”€â”€ images/         # Scene background images
```

---

## How It Works

All story scenes are defined as a dictionary in `app.py`. Each scene has a text description, a background image, and a list of choices leading to other scenes. Adding new scenes is as simple as adding a new entry to the dictionary.

```python
"my_scene": {
    "text": "Description of the scene...",
    "background": "images/my_scene.jpg",
    "choices": [
        {"text": "Choice 1", "next": "scene_a"},
        {"text": "Choice 2", "next": "scene_b"}
    ]
}
```

---

## Requirements

- Python 3.8+
- Flask

---

## License

This project is licensed under the MIT License.

---

## Author

**Didinga Omodi**
- GitHub: [@Didinga](https://github.com/Didinga)
- LinkedIn: [didiomodi](https://www.linkedin.com/in/didiomodi/)
