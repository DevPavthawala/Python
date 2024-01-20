class human:

    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):

        if self.occupation == "data_scientist":
            print(self.name,"data scientist expert")
        elif self.occupation == "video editor":
            print(self.name, "free lancer video editor")

    def speak(self):
        print(self.name,"says how are you")


dev = human("Dev Pavthawala","data_scientist")
dev.do_work()
dev.speak()

dev_patel = human("Dev Patel","video editor")
dev_patel.do_work()
dev_patel.speak()