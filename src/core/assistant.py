class AIBuddy:
    def __init__(self, name="H-AIBuddy"):
        self.name = name

    def greet(self):
        return f"👋 Hello! I am {self.name}, your AI Guardian. How can I help you today?"

    def process_command(self, command):
        command = command.lower()
        if "status" in command:
            return "🛡️ All systems are stable. I am guarding your data."
        elif "help" in command:
            return "🆘 I can track your goals, save logs, and protect your projects!"
        else:
            return "🤔 I'm still learning that. Can you try asking for 'status' or 'help'?"

# Quick test
if __name__ == "__main__":
    buddy = AIBuddy()
    print(buddy.greet())
