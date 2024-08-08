# Accessing the .py files that need to be run in order to create the Database
scripts = ["Raw_Database.py", "Constructor_Data.py", "Drivers_Data.py"]

# Iterating through every script to create the main database using exec
for script in scripts:
    with open(script) as f:
        code = f.read()
        exec(code)
