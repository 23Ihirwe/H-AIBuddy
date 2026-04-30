class H_AIBuddy:
    def __init__(self):
        self.name = "H-AIBuddy"
        self.skills = ["Science", "Math", "Physics", "English", "Deutsch"]
        self.user_data = {}

    def greet(self):
        return f"👋 Hello! I am {self.name}, your AI Guardian."

    def start_interview(self):
        print(self.greet())
        user_type = input("🤖 Are you a mother? (yes/no): ").lower()
        
        if user_type == "yes":
            self.user_data['name'] = input("🤖 What is your name? ")
            self.user_data['age'] = input("🤖 How old are you? ")
            self.user_data['career'] = input("🤖 What is your career status? ")
            self.user_data['education'] = input("🤖 What is your level of education? ")
            self.user_data['employment'] = input("🤖 Are you employed? (yes/no) ")
            
            child_age = input("🤖 How old is your child/children? ")
            self.user_data['child_age'] = child_age

            if int(child_age) >= 18:
                managed = input("🤖 Did your child manage to study? (yes/no) ")
                if managed == "yes":
                    print("🤖 That is wonderful! Education is a powerful shield.")
                self.check_willingness()
            else:
                self.check_willingness()
        else:
            print("🤖 I see! I am still here to guard and assist you.")

    def check_willingness(self):
        print(f"\n🤖 {self.name}: I am an expert in {', '.join(self.skills)}.")
        self_learn = input("🤖 Are you willing to learn these yourself? (yes/no) ").lower()
        kids_learn = input("🤖 Would you like your children to learn with me? (yes/no) ").lower()

        if self_learn == "yes" or kids_learn == "yes":
            choice = input(f"🤖 Which subject should we start with? ")
            print(f"🤖 Excellent! I am happy to teach you {choice}! 🌟")
        else:
            print("🤖 No problem! I am here whenever you are ready.")

if __name__ == "__main__":
    buddy = H_AIBuddy()
    buddy.start_interview()
