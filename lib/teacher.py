#!/usr/bin/env python

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None or len(knowledge) == 0:
            self.knowledge = ["Default Knowledge"]
        else:
            self.knowledge = knowledge
    
    def teach(self, teaches):
        self.knowledge.append(teaches)
