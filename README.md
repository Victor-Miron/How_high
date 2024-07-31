
# How High Project

## Project Description

This project analyzes and processes datasets about drivers and constructor teams in F1!

## Installation Instructions

To set up this project, follow these steps:

1. Clone the repository:
   ```sh
   git clone git@github.com:Victor-Miron/How_high.git
   ```

2. Navigate to the project directory:
   ```sh
   cd How_high
   ```

3. Create and activate a virtual environment:
   ```sh
   python -m venv myvenv
   source myvenv/bin/activate   # On Windows, use `myvenv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the scripts in this project, follow these steps:

1. **Create the database**:
   ```sh
   python Create_database.py
   ```

2. **Create the drivers data table**:
   ```sh
   python Create_Drivers\ data_table.py
   ```

3. **Create the constructor data table**:
   ```sh
   python Create_Constructor_data_table.py
   ```

4. **Convert drivers data to SQL**:
   ```sh
   python Convert_Drivers_data_to_sql.py
   ```

5. **Convert constructor data to SQL**:
   ```sh
   python Convert_Constructor_data_to_sql.py
   ```

## File Descriptions

- `Create_database.py`: Script to create the initial database from raw data.
- `Create_Drivers data_table.py`: Script to create the drivers data table.
- `Create_Constructor_data_table.py`: Script to create the constructor data table.
- `Convert_Drivers_data_to_sql.py`: Script to convert drivers data to SQL.
- `Convert_Constructor_data_to_sql.py`: Script to convert constructor data to SQL.
- `requirements.txt`: List of required Python packages for the project.
- `README.md`: Project documentation file (this file).

## Credits

This project was created by Victor Miron. Special thanks to all contributors and supporters.
