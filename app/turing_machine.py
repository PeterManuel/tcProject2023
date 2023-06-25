from tape import Tape
class Turing:
    def __init__(self,transition_function,initial_state,accept_state,reject_state) -> None:
        #self._Q=states #list string
        #self._W=alphabet #list string
        #self._G=tape_alphabet # list string
        self._F=transition_function #dict(tupe(str,str),(str,str,str))
        self._q0=initial_state #str
        self._qa=accept_state #str
        self._qr=reject_state #str
        self._tape=Tape() #class

        self.current_state=initial_state
        

    def run(self,word):

        #set the tape
        self._tape.set_tape(word)

        while(True):
            #read the tape
            read_symbol=self._tape.read()

            #get the machine transition

            transition=self._F[(self.current_state,read_symbol)]

            transition_state,symbol_to_write,movimentation=transition

            #pass change the current state
            self.current_state=transition_state

            #now write the symbol to the tape
            self._tape.write(symbol_to_write)

            #check the movement and move
            if movimentation == 'R':
                self._tape.move_right()
            
            elif movimentation == 'L':
                self._tape.move_left()
            
            elif movimentation == 'P':
                self._tape.stay_put()

            #now deciding
            if self.current_state == self._qa:
                return (self._tape.tape,"ACCEPTED")
            
            elif self.current_state == self._qr:
                return (self._tape.tape,"REJECTED")
            
            else:
                continue

M={('q0','n'):('q0','a','R'),('q0','u'):('q0','b','R'),('q0','b'):('q0','b','R'),
   ('q0','a'):('q0','a','R'),('q0','_'):('qa','_','R')}

T=Turing(M,'q0','qa','qr')

r=T.run('uan')

x,y=r


for c in x:
    if x[c]=='_':
        continue
    print(x[c],end="")

print()
print("state:")
print(y)

#things to define:

    #verify when a transition was not defined, better raise an exception
    #verifiy the sintax of transition function better define a regular expression