# Strategy Pattern for defining training programs
from exercise import (
    Exercise,
    WarmUpDecorator,
    CoolDownDecorator,
    StrengthExercise

 
)
class TrainingProgram:
    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises

    def execute(self):
        print(f"Executing {self.name} program:")
        for exercise in self.exercises:
            print(exercise.get_description())

class StrengthTraining:
    def __init__(self):
        self.exercises = [
            WarmUpDecorator(StrengthExercise()),
            CoolDownDecorator(StrengthExercise())
        ]

    def train(self):
        for exercise in self.exercises:
            print(exercise.get_description())



    def train(self):
        for exercise in self.exercises:
            print(exercise.get_description())
