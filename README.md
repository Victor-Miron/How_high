
# How High Project

## Project Description

The **How High Project** focuses on analyzing and processing datasets related to F1 drivers and constructor teams. The project aims to provide insights into the performance metrics of F1 entities and to visualize the data using tools like Tableau.

## Prerequisites

- Python 3.10 or later
- Virtual Environment (optional but recommended)
- Visual Studio Code (VS Code) or any other preferred IDE with Jupyter Notebook support

## Installation Instructions

To set up this project, follow these steps:

1. **Clone the Repository:**

   Open your IDE terminal and run:

   ```sh
   git clone git@github.com:Victor-Miron/How_high.git
   ```

2. **Navigate to the Project Directory:**

   ```sh
   cd How_high
   ```

3. **Create and Activate a Virtual Environment:**

   ```sh
   python -m venv myvenv
   source myvenv/bin/activate   # On Windows, use `myvenv\Scripts\activate`
   ```

4. **Install the Required Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Install Jupyter Notebook (if not already installed):**

   ```sh
   pip install notebook
   ```

## Usage

### Running the Project

1. **Open the Project in Your IDE:**

   - Open Visual Studio Code (VS Code) or your preferred IDE.
   - Go to `File` > `Open Folder` and select the project directory.

2. **Run the Main Script:**

   - Open the terminal within your IDE (`View` > `Terminal` in VS Code).
   - Run the main script:

     ```sh
     python Greatest.py
     ```

   This will execute all necessary steps to process the data and create the database `Greatest.db`.

### Visualizing the Clean Data

To visualize the clean data, use **DB Browser for SQLite**:

1. **Install DB Browser for SQLite:**
   - You can download it from the official website: [DB Browser for SQLite](https://sqlitebrowser.org/).

2. **Open the Database:**
   - Launch DB Browser for SQLite and open the generated SQLite database file located in the project directory.

3. **Explore the Data:**
   - Use the built-in tools to explore tables, run queries, and visualize the clean data.
   - The clean data will be in two tables:
     - Constructor Data
     - Drivers Data

### Running the Data Handling Demo

1. **Launch Jupyter Notebook from Your IDE:**

   - In VS Code, use the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and select `Python: Create New Blank Notebook`.
   - Open the terminal within your IDE (`View` > `Terminal` in VS Code).
   - Run Jupyter Notebook:

     ```sh
     jupyter notebook
     ```

2. **Open the Notebook:**

   - In the Jupyter Notebook interface, navigate to the project directory and open `Data_handling_demo_in_python.ipynb`.

3. **Run the Notebook:**

   - Execute the cells in the notebook to run the data handling demo.

## Script Descriptions

For reviewers who want more information about the code, each Python script in this project serves a specific purpose. Below is the order and description of each script:

1. **Raw_Database.py**: Initializes the database structure required for storing F1 data.

2. **Create_Drivers_data_table.py**: Creates and cleans the drivers data table. This is one method for handling driver data.

3. **Drivers_Data_Using_Join_method.py**: An alternative, faster method for creating and cleaning the drivers data table using joins.

4. **Create_Constructor_data_table.py**: Creates and cleans the constructor data table. This is one method for handling constructor data.

5. **Constructors_Data_Using_Join_method.py**: An alternative, faster method for creating and cleaning the constructor data table using joins.

6. **Convert_Drivers_data_to_sql.py**: Transforms and loads driver data into the SQL database for further analysis.

7. **Convert_Constructor_data_to_sql.py**: Transforms and loads constructor data into the SQL database for further analysis.

8. **Data_handling_demo_in_python.py**: Demonstrates data manipulation techniques in Python. Also available as a Jupyter Notebook for interactive exploration.

## Directory Structure

- **`archive/`**: Contains archived datasets and backup files.
- **`myvenv/`**: The virtual environment directory for managing project dependencies.
- **`__pycache__/`**: Compiled Python files for faster execution.
- **`.git/`**: Git version control directory for tracking changes.
- **`.idea/`**: Configuration files for IDE support.

## Future Enhancements

- Implement advanced analytics for driver and constructor performance predictions.
- Integrate additional data sources for enriched analysis.
- Develop a user-friendly web interface for data interaction through Tableau.

## Contributors

- **Victor Miron**: Project Lead and Developer

## Tableau Visualization

Visualize the processed data in Tableau by visiting the following link (I advise using Chrome or Firefox for a better experience):

[View on Tableau](https://public.tableau.com/app/profile/victor.miron/viz/HowHigh/Story1?publish=yes)

---

This `README.md` file provides a comprehensive overview of the project, including setup instructions, usage guidelines, visualization tools, and a link to visualize the data in Tableau. Feel free to further customize any sections or provide additional details as needed!
