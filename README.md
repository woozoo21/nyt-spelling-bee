# NYT Spelling Bee Solver  

A Python-based web application that helps solve the New York Times Spelling Bee puzzle. Enter the provided letters, and the application will generate all possible valid words, identify pangrams, and categorize words by their length for easy browsing.  

## Features  
- **Letter-based Word Generation**: Input a set of letters, and the app generates all possible valid words.  
- **Pangram Detection**: Identifies and highlights words that use all the letters.  
- **Categorized Results**: Words are grouped and displayed by length, side by side for user convenience.  
- **Responsive Interface**: Simple, user-friendly web design for a seamless experience.  

## Technology Stack  
- **Backend**: Python (Flask framework)  
- **Frontend**: HTML, CSS (with styling for a honeybee theme)  
- **Deployment**: Compatible with platforms like Replit  

## Getting Started  

### Prerequisites  
- Python 3.7 or later  
- Required libraries: Flask, BeautifulSoup4  

### Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/nyt-spelling-bee-solver.git
   cd nyt-spelling-bee-solver
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
   ```bash
   pip install -r requirements.txt

## Running and Deployment
After installing dependencies, run the application locally by setting the Flask app and starting the development server:

```bash
export FLASK_APP=main  # On Windows: set FLASK_APP=main
flask --app main run
