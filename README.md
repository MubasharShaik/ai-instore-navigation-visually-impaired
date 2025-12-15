# AI Powered Instore Navigation for Visually Impaired Individuals

## Overview
This project is an AI-powered in-store navigation system designed to assist visually impaired individuals in navigating retail environments. The system provides an interactive, accessible interface for selecting products and guides users through a virtual store layout using pathfinding algorithms and voice feedback.

## Features
- **Accessible Product Selection:** Users can select products via a visual grid or voice commands.
- **Maze Navigation:** The system generates a virtual store maze and finds the shortest path to the selected product.
- **Voice Feedback:** Instructions are provided using speech synthesis to guide users step-by-step.
- **Dynamic Pathfinding:** Utilizes Breadth-First Search (BFS) to compute optimal navigation routes.
- **User-Friendly Interface:** Responsive web interface with image-based product selection and clear navigation cues.

## How It Works
1. The user selects a product (by clicking or speaking).
2. The system generates a randomized store layout (maze) and places the selected product at a random location.
3. The shortest path from the user's starting position to the product is calculated.
4. The user is guided through the maze with step-by-step instructions, both visually and via voice.

## Requirements
- Python 3.7+
- Flask (see `requirements.txt`)

## Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/MubasharShaik/ai-instore-navigation-visually-impaired.git
   cd ai-instore-navigation-visually-impaired
   ```
2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```

## Running the Application
- Start the Flask server:
   ```powershell
   python app.py
   ```
- Open your browser and go to `http://127.0.0.1:5000/`

## Project Structure
```
app.py                  # Main Flask application
app1.py                 # (Alternate/legacy version)
requirements.txt        # Python dependencies
static/                 # Static files (CSS, images)
templates/              # HTML templates (Jinja2)
README.md               # Project documentation
.gitignore              # Git ignore rules
```

## Usage
- On the home page, select a product by clicking its image or using the voice input button.
- The system will display a maze and guide you to the product with both on-screen and spoken instructions.
- You can select another product at any time.

## Accessibility
- Designed for visually impaired users with voice input and output.
- Simple, high-contrast interface for ease of use.

## Credits
- Developed by Mubashar Shaik and team as a final year project (BATCH_NO_7_AIDS-1).
- Special thanks to faculty and contributors.

## License
This project is for educational purposes. For other uses, please contact the author.

---
For questions or contributions, open an issue or pull request on GitHub.
