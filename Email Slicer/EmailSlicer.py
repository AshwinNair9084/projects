class email_slicer:
    def __init__(self, email) -> None:
        self.email = email
    def slicer(self):
         return self.email.split("@")
        

if __name__ == "__main__":
    print("please enter your email : ", end ="")
    email = input()
    s = email_slicer(email)
    print(f"The username is : {s.slicer()[0]} & domain is : {s.slicer()[1]}")
    
    