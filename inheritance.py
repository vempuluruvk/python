#single inheritance
# multilevel inheritance
# multiple level inheritance
# hiericel inheritance

                                                     #single
class parent():
    def output(self):
        print("i am the parent")
        class child(parent):
            def output(self):
                print("i am the child")
                c=child()
                c.output()#child class
                c.output()#parent class

                                                            # multi level
class grandfather():             
     def outputgf():
         print("i am the grandfather")
class parent(grandfather):
    def  output(self):
        print("i am the parent")
        
        class child(parent):
            def output(self):
                print("i am the child")
                c=child()
                c.output()#child class
                c.output()#parent class
                c.outputgf# granmd father

                                                                #multiple inheritance
                class father():             
     def output():
         print("i am the father")
class  mother():
    def output(self):
        print("i am the  mother")
        
        class child(parent, mother):
            def output(self):
                print("i am the child")
                c=child()
                c.output()#child cl ass
                c.output()#parent class
                c.outputgf()

                                                 #hericricl inheritance

class father():             
     def output():
         print("i am the father")
class  child 1( father):
    def output(self):
        print("i am the  child1")
    class child2(father):
            def output(self):
                print("i am the child2")
                c=child()#object 1 
                c2= child2()# object 2
                c.output()#child cl ass
                c.output()#parent class
                c2.output #child 2

