from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Statistics'))
    def aids(self):
        print("Suggested Career Path: Artificial Intelligence and Data Science")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def mechatronics(self):
        print("Suggested Career Path: Mechatronics Engineering")

    @Rule(StudentFacts(likes='Mechanics'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")

    @Rule(StudentFacts(likes='AI Concepts'), StudentFacts(likes='Maths'))
    def ROAI(self):
        print("Suggested Career Path: RO&AI Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interested subjects separated by commas (e.g., Maths, Physics, Programming, Statistics, Circuits, Mechanics, AI Concepts): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()

if __name__ == "__main__":
 main()

