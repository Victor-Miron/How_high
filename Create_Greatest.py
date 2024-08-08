# List of .py files that need to be run in order to create the Database
scripts = ["Raw_Database.py", "Constructor_Data.py", "Drivers_Data.py"]

# Iterate through each script to create the main database using exec
for script in scripts:
    with open(script) as f:
        code = f.read()
        exec(code)
