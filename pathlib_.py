from pathlib import Path

# Relative Path
files_path = Path("ML", "main.py")
print(files_path)

# Get the home path 
home = Path.home()
print(f"Home : {home}")

# Absolute path
files_abs_path = Path(home, "ML", "main.py")

# File Attributes
print(f"File name : {files_abs_path.name}")
print(f"File suffix : {files_abs_path.suffix}")


# Access parents 
shark = Path("ocean", "animals", "fish", "shark.txt")
print(shark)
print(f"Shark's parent : {shark.parent}")
