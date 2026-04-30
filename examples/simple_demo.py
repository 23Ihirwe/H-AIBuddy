import sys
import os

# This tells Python where to find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db.repository import init_brain
from src.core.assistant import H_AIBuddy

def run_system():
    print("🚀 --- H-AIBuddy System Booting ---")
    
    # 1. Wake up the Memory (DB)
    init_brain()
    
    # 2. Wake up the Intelligence (Core)
    buddy = H_AIBuddy()
    
    # 3. Start the Interview
    buddy.start_interview()

if __name__ == "__main__":
    run_system()
