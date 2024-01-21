from flask import Flask, render_template, jsonify

app = Flask(__name__)
data = {
  "roles": [
    {
      "name": "data analyst",
      "description": "Extracting meaningful insights from data",
      "startNode": "Programming Basics",
      "roleNode": "Data Analyst",
      "nodes": [
        {
          "name": "Programming Basics",
          "description": "The ability to write efficient and maintainable code",
          "prerequisites": [],
          "children": [
            "Python Programming"
          ]
        },
        {
          "name": "Python Programming",
          "description": "A general-purpose programming language used extensively in data analysis and machine learning",
          "prerequisites": [
            "Programming Basics"
          ],
          "children": [
            "Data Analysis Basics"
          ]
        },
        {
          "name": "Data Analysis Basics",
          "description": "Introduction to data analysis",
          "prerequisites": [
            "Python Programming"
          ],
          "children": [
            "Data Cleaning"
          ]
        },
        {
          "name": "Data Cleaning",
          "description": "Removing errors and inconsistencies from datasets",
          "prerequisites": [
            "Data Analysis Basics"
          ],
          "children": [
            "Exploratory Data Analysis"
          ]
        },
        {
          "name": "Exploratory Data Analysis",
          "description": "Understanding patterns and distributions in data",
          "prerequisites": [
            "Data Cleaning"
          ],
          "children": [
            "Data Visualization"
          ]
        },
        {
          "name": "Data Visualization",
          "description": "Communicating insights through charts and graphs",
          "prerequisites": [
            "Exploratory Data Analysis"
          ],
          "children": [
            "Data Analyst"
          ]
        },
        {
          "name": "Data Analyst",
          "description": "Role node for data analyst",
          "prerequisites": [
            "Data Visualization"
          ],
          "children": []
        }
      ]
    },
    {
      "name": "front-end engineer",
      "description": "Designing and implementing user interfaces for web applications",
      "startNode": "Programming Basics",
      "roleNode": "Front-End Engineer",
      "nodes": [
        {
          "name": "Programming Basics",
          "description": "The ability to write efficient and maintainable code",
          "prerequisites": [],
          "children": [
            "HTML and CSS"
          ]
        },
        {
          "name": "HTML and CSS",
          "description": "Markup and styling languages for building webpages",
          "prerequisites": [
            "Programming Basics"
          ],
          "children": [
            "JavaScript"
          ]
        },
        {
          "name": "JavaScript",
          "description": "A programming language for adding interactivity to webpages",
          "prerequisites": [
            "HTML and CSS"
          ],
          "children": [
            "Front-End Frameworks"
          ]
        },
        {
          "name": "Front-End Frameworks",
          "description": "Libraries and tools for streamlining front-end development",
          "prerequisites": [
            "JavaScript"
          ],
          "children": [
            "Front-End Engineer"
          ]
        },
        {
          "name": "Front-End Engineer",
          "description": "Role node for front-end engineer",
          "prerequisites": [
            "Front-End Frameworks"
          ],
          "children": []
        }
      ]
    },
    {
        "name": "machine learning engineer",
        "description": "Developing algorithms and models for machines to learn from data",
        "startNode": "Programming Basics",
        "roleNode": "Machine Learning Engineer",
        "nodes": [
          {
            "name": "Programming Basics",
            "description": "The ability to write efficient and maintainable code",
            "prerequisites": [],
            "children": [
              "Python Programming"
            ]
          },
          {
            "name": "Python Programming",
            "description": "A general-purpose programming language used extensively in data analysis and machine learning",
            "prerequisites": [
              "Programming Basics"
            ],
            "children": [
              "Data Analysis Basics"
            ]
          },
          {
            "name": "Data Analysis Basics",
            "description": "Introduction to data analysis",
            "prerequisites": [
              "Python Programming"
            ],
            "children": [
              "Data Cleaning"
            ]
          },
          {
            "name": "Data Cleaning",
            "description": "Removing errors and inconsistencies from datasets",
            "prerequisites": [
              "Data Analysis Basics"
            ],
            "children": [
              "Exploratory Data Analysis"
            ]
          },
          {
            "name": "Exploratory Data Analysis",
            "description": "Understanding patterns and distributions in data",
            "prerequisites": [
              "Data Cleaning"
            ],
            "children": [
              "Statistics"
            ]
          },
          {
            "name": "Statistics",
            "description": "The study of data analysis and inference",
            "prerequisites": [
              "Exploratory Data Analysis"
            ],
            "children": [
              "Machine Learning Basics"
            ]
          },
          {
            "name": "Machine Learning Basics",
            "description": "Introduction to machine learning",
            "prerequisites": [
              "Statistics"
            ],
            "children": [
              "Supervised Learning"
            ]
          },
          {
            "name": "Supervised Learning",
            "description": "Building models to predict a target variable based on labeled data",
            "prerequisites": [
              "Machine Learning Basics"
            ],
            "children": [
              "Deep Learning"
            ]
          },
          {
            "name": "Deep Learning",
            "description": "A subset of machine learning that focuses on artificial neural networks",
            "prerequisites": [
              "Supervised Learning"
            ],
            "children": [
              "Machine Learning Engineer"
            ]
          },
          {
            "name": "Machine Learning Engineer",
            "description": "Role node for machine learning engineer",
            "prerequisites": [
              "Deep Learning"
            ],
            "children": []
          }
        ]
      }
    ]
  }
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


