import os
import sys
import shutil

def add_program_to_startup(program_path):
    program_name = os.path.splitext(os.path.basename(program_path))[0]

    if not os.path.isfile(program_path):
        print(f"Error: Program file '{program_path}' not found.")
        sys.exit(1)

    startup_folder = os.path.join(os.environ["APPDATA"],
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs",
        "Startup")
    startup_program_path = os.path.join(startup_folder, f"{program_name}.lnk")

    try:
        shutil.copy2(program_path, startup_program_path)
        print(f"Program '{program_path}' added to startup successfully.")
    except Exception as e:
        print(f"Error: Failed to add program to startup - {e}")
        sys.exit(1)

program_path1="C:\\Program Files\\paint.net\\paintdotnet.exe"
add_program_to_startup(program_path1)
