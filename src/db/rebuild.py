import os

def run_script(script_name):
    print(f"Running {script_name}...")
    exit_code = os.system(f"python {script_name}")
    if exit_code != 0:
        print(f"Error occurred while running {script_name}. Exiting.")
        exit(exit_code)

def main():
    print("Resetting the database...")
    
    # Run the initialization script
    run_script("src/db/db-init.py")
    
    # Run the seeders in the correct order
    run_script("src/db/patient-seed.py")
    run_script("src/db/user-seed.py")
    run_script("src/db/specimens-seed.py")
    
    print("Database reset and seeded successfully.")

if __name__ == "__main__":
    main()
