class H_AIBuddy:
    def __init__(self):
        self.name = "H-AIBuddy"
        # The robot's skill set
        self.skills = ["Science", "Math", "Physics", "English", "Deutsch"]
        self.user_data = {}

    def start_interview(self):
        print(f"🤖 {self.name}: Hello! I am your AI Guardian. I am here to assist and support your family.")
        
        # Identification
        user_type = input("🤖 Are you a mother? (yes/no): ").lower()
        
        if user_type == "yes":
            # Collect Personal Info
            self.user_data['name'] = input("🤖 What is your name? ")
            self.user_data['age'] = input("🤖 How old are you? ")
            self.user_data['career'] = input("🤖 What is your career status? ")
            self.user_data['education'] = input("🤖 What is your level of education? ")
            self.user_data['employment'] = input("🤖 Are you currently employed? (yes/no) ")
            
            child_age = input("🤖 How old is your child/children? ")
            self.user_data['child_age'] = child_age

            # Logic for older children
            if int(child_age) >= 18:
                managed_to_study = input("🤖 Did your child/children manage to study? (yes/no) ")
                if managed_to_study == "yes":
                    print("🤖 That is wonderful! Education is a powerful shield.")
                    self.check_willingness()
                else:
                    self.check_willingness()
            else:
                self.check_willingness()
        else:
            print("🤖 I see! I am still here to guard and assist you with my AI capabilities.")

    def check_willingness(self):
        print(f"\n🤖 {self.name}: I have expert skills in {', '.join(self.skills)}.")
        
        # Question 1: For the Mother
        learn_self = input("🤖 Are you willing to learn any of these subjects yourself? (yes/no) ").lower()
        
        # Question 2: For the Kids
        learn_kids = input("🤖 Would you like your child/children to learn these subjects with me? (yes/no) ").lower()

        if learn_self == "yes" or learn_kids == "yes":
            self.offer_to_teach(learn_self, learn_kids)
        else:
            print("🤖 No problem at all! I am here whenever you or your family are ready to grow. 🛡️")

    def offer_to_teach(self, learn_self, learn_kids):
        if learn_self == "yes" and learn_kids == "yes":
            print("\n🤖 Fantastic! A family that learns together stays strong.")
        elif learn_self == "yes":
            print("\n🤖 Excellent! It is never too late to master a new skill.")
        else:
            print("\n🤖 Wonderful! I will make sure your children become experts.")

        choice = input(f"🤖 Which subject should we start with? ({', '.join(self.skills)}): ")
        print(f"🤖 Perfect choice! Let's begin our journey in {choice} together! 🌟")

if __name__ == "__main__":
    buddy = H_AIBuddy()
    buddy.start_interview()
