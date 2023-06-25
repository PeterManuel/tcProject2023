class Tape:
    def __init__(self) -> None:
        self.tape={}
        self.head=0
        self.tail=0

    def set_tape(self,word):
        i=-1
        for c in word:
            i+=1
            self.tape[str(i)]=c
            
    def get_tape(self):
        return self.tape

    def move_right(self):
        self.head+=1
        if(self.head)>len(self.tape)-1:
            self.tape[str(self.head)]='_'

    
    def move_left(self):
        self.head-=1
        if(self.head)<self.tail:
            self.tape[str(self.head)]='_'
    
    def stay_put(self):
        self.head = self.head

    def write(self,symbol):
        self.tape[str(self.head)]=symbol

    def read(self):
        return self.tape[str(self.head)]
