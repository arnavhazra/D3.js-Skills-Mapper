# D3 Visualization Mini App

This web application uses Flask and D3.js to visualize a hierarchical structure of skills and roles, representing the learning path for different roles in the fields of data analysis, front-end engineering, and machine learning engineering.

## Prerequisites

Make sure you have the following installed on your machine:

- Python (3.x recommended)
- Flask (`pip install Flask`)
- Internet connection to fetch D3.js library from [d3js.org](https://d3js.org/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/d3-visualization-web-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd d3-visualization-web-app
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Flask application by executing the following command in the project directory:

```bash
python app.py
```

This will start the development server, and you can access the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## Endpoints

- `/`: Displays the main visualization page.
- `/data`: Provides the hierarchical data in JSON format.

## Visualization

The main visualization page (`index.html`) uses D3.js to create an interactive force-directed graph. The graph represents the learning path for different roles, including data analyst, front-end engineer, and machine learning engineer. The relationships between skills are visualized using nodes and links.

The color-coded nodes represent different roles, and the links between nodes represent the progression from one skill to another. The visualization is created dynamically based on the hierarchical data fetched from the `/data` endpoint.
