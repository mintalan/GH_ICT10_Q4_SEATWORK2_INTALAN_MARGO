from pyscript import display
from js import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject


c1 = Classmate("Atasha", "Sapphire", "Social Studies")
c2 = Classmate("Ainah", "Ruby", "Science")
c3 = Classmate("Mergal", "Emerald", "Math")
c4 = Classmate("Tessa", "Topaz", "English")
c5 = Classmate("Ishan", "Sapphire", "Filipino")


def add_classmate(e):

    document.getElementById("output").innerHTML = ""
    
    display(f"I am {c1.name} from {c1.section}. My favorite subject is {c1.favorite_subject}.", target="output")
    display(f"I am {c2.name} from {c2.section}. My favorite subject is {c2.favorite_subject}.", target="output")
    display(f"I am {c3.name} from {c3.section}. My favorite subject is {c3.favorite_subject}.", target="output")
    display(f"I am {c4.name} from {c4.section}. My favorite subject is {c4.favorite_subject}.", target="output")
    display(f"I am {c5.name} from {c5.section}. My favorite subject is {c5.favorite_subject}.", target="output")

    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_c = Classmate(name, section, subject)

    display(f"I am {new_c.name} from {new_c.section}. My favorite subject is {new_c.favorite_subject}.", target="output")