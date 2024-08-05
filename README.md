
# How High Project

## Project Description

The **How High Project** focuses on analyzing and processing datasets related to F1 drivers and constructor teams. The project aims to provide insights into the performance metrics of F1 entities and to visualize the data using tools like Tableau.

## Installation Instructions

To set up this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone git@github.com:Victor-Miron/How_high.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd How_high
   ```

3. **Create and activate a virtual environment:**
   ```sh
   python -m venv myvenv
   source myvenv/bin/activate   # On Windows, use `myvenv\Scripts\activate`
   ```

4. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the scripts in this project, follow these steps:

1. **Create the database:**
   - This script initializes the database structure required for storing F1 data.
   ```sh
   python Create_database.py
   ```

2. **Create the drivers data table:**
   - Use this script to create a table for storing driver-related data. 
   - Also, this script cleans the drivers data table.
   - Please be patient.It will take up to 1 minute to create the table due to sql raw code.
   
   ```sh
   python Create_Drivers_data_table.py
   ```

3. **Create the constructor data table:**
   - Use this script to create a table for storing constructor-related data.
   - Also, this script cleans the constructor data table.
   - Please be patient.It will take up to 1 minute to create the table due to sql raw code.
   ```sh
   python Create_Constructor_data_table.py
   ```

4. **Convert drivers data to SQL:**
   - This script transforms and loads driver data into the SQL database for further analysis.
   ```sh
   python Convert_Drivers_data_to_sql.py
   ```

5. **Convert constructor data to SQL:**
   - This script transforms and loads constructor data into the SQL database.
   ```sh
   python Convert_Constructor_data_to_sql.py
   ```

6. **Data Handling Demo:**
   - Demonstrates data manipulation techniques in Python.
   ```sh
   python Data_handling_demo_in_python.py
   ```

## Visualizing the Clean Data

To visualize the clean data, use **DB Browser for SQLite**:

1. **Install DB Browser for SQLite:**
   - You can download it from the official website: [DB Browser for SQLite](https://sqlitebrowser.org/).

2. **Open the Database:**
   - Launch DB Browser for SQLite and open the generated SQLite database file located in the project directory.

3. **Explore the Data:**
   - Use the built-in tools to explore tables, run queries, and visualize the clean data.
   - The clean data will be in two tables:
      + Constructor_Data,
      + Drivers_Data

## Directory Structure

- **`archive/`:** Contains archived datasets and backup files.
- **`myvenv/`:** The virtual environment directory for managing project dependencies.
- **`__pycache__/`:** Compiled Python files for faster execution.
- **`.git/`:** Git version control directory for tracking changes.
- **`.idea/`:** Configuration files for IDE support.

## Future Enhancements

- Implement advanced analytics for driver and constructor performance predictions.
- Integrate additional data sources for enriched analysis.
- Develop a user-friendly web interface for data interaction.

## Contributors

- **Victor Miron:** Project Lead and Developer

## Tableau Visualization

Visualize the processed data in Tableau by visiting the following link
( I advise using Chrome or Firefox for a better experience):

[View on Tableau](https://public.tableau.com/app/profile/victor.miron/viz/HowHigh/Story1?publish=yes)

---

This `README.md` file provides a comprehensive overview of the project, including setup instructions, usage guidelines, visualization tools, and a link to visualize the data in Tableau. Feel free to further customize any sections or provide additional details as needed!
