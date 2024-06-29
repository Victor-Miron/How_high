Formula_one
# How High Project

## Overview
This project involves creating and managing a database using various datasets related to constructors and races. The project includes scripts for database creation, data merging, and optimization for different computer speeds.

## Project Structure
- `Create_database.py`: Script to create the database from CSV files.
- `merged.csv`: Merged CSV file containing the dataset.
- `faster_computer_dataset.py`: Script optimized for faster computers.
- `requirements.txt`: List of dependencies required for the project.
- `archive/`: Directory containing archived data or additional files.
- `myvenv/`: Virtual environment directory.
- `README.md`: Project documentation.
- `Merge_all_csv.py`: Script to merge multiple CSV files into one.
- `.gitattributes`: Git attributes file.
- `.git/`: Directory containing Git version control information.
- `slower_computer_dataset.py`: Script optimized for slower computers.
- `.idea/`: Directory for project configuration files used by JetBrains IDEs.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd How_high

2. Set up the virtual environment:

python3 -m venv myvenv
source myvenv/bin/activate   # On Windows: myvenv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the database creation script
    Create_database.py

-To merge CSV files, use Merge_all_csv.py:
    Merge_all_csv.py
    
-To run the dataset script optimized for faster computers, use :
    faster_computer_dataset.py

-To run the dataset script optimized for slower computers, use :
    slower_computer_dataset.py

License

This README file provides an overview of the project, instructions for setting it up, and information on how to use the various scripts included in the repository.

