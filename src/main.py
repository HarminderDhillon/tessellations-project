import os
import sys
from datetime import datetime

def main():
    print("Tessellations Generator")
    print(f"Python version: {sys.version}")
    print(f"Current time: {datetime.now()}")
    print("Output directory:", os.path.abspath("output"))
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    print("Setup complete!")

if __name__ == "__main__":
    main()