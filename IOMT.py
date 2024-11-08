import os
xrvm phep xgmv cgka
# Define the project structure as a dictionary
project_structure = {
    "IoMT_Malware_Detection": {
        "data": {},                     # Folder to store datasets
        "models": {},                   # Folder to store trained models
        "src": {                        # Folder for source code
            "data_generator.py": "",    # Script for generating synthetic data
            "train_model.py": "",       # Script for training models
            "predict.py": "",           # Script for predictions
            "shap_explainer.py": ""     # Script for model explainability
        },
        "webapp": {                     # Folder for web application code
            "app.py": "",               # Flask API server
            "templates": {              # Folder for HTML templates
                "index.html": "<!-- Main dashboard page HTML -->"
            },
            "static": {                 # Folder for CSS and JS files
                "style.css": "/* CSS styles for dashboard */",
                "script.js": "// JavaScript for dynamic dashboard elements"
            }
        },
        "logs": {                       # Folder for log files
            "anomalies.log": ""         # Log file for detected anomalies
        },
        "README.md": "# Project Documentation"  # README file for documentation
    }
}

# Function to create the file structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create a folder
            os.makedirs(path, exist_ok=True)
            # Recursively create subfolders and files
            create_structure(path, content)
        else:
            # Create a file and write content (if any)
            with open(path, 'w') as file:
                file.write(content)

# Base path where the project should be created
base_path = "."

# Create the project structure
create_structure(base_path, project_structure)

print("Project structure created successfully!")
