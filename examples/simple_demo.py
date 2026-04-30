import sys
import os
# Adds the main folder to the path so it can find 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db.repository import init_brain
from src.core.assistant import AIBuddy

def run_complete_demo():
    print("🚀 --- H-AIBuddy Full System Boot ---")
    
    # 1. Wake up the Memory (DB)
    init_brain()
    
    # 2. Wake up the Intelligence (Core)
    buddy = AIBuddy()
    print(f"\n{buddy.greet()}")
    
    # 3. Test a Command
    user_input = "What is your status?"
    print(f"\nUser: {user_input}")
    
    response = buddy.process_command(user_input)
    print(f"AI: {response}")
    
    print("\n✨ System check complete. Core and Brain are communicating!")

if __name__ == "__main__":
    run_complete_demo()
