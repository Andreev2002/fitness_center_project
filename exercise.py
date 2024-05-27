#Decorator Pattern
class Exercise:
    def __init__(self, description, duration, repetitions):
        self.description = description
        self.duration = duration
        self.repetitions = repetitions
        
             

    def get_description(self):
        return f"{self.description} for {self.duration} repetitions, {self.repetitions} sets"


    
class ExerciseDecorator:
    def __init__(self, exercise):
        self._exercise = exercise

    def get_description(self):
        return self._exercise.get_description()

class WarmUpDecorator(ExerciseDecorator):
    def get_description(self):
        return f"Warm-up: {self._exercise.get_description()}"
    


class CoolDownDecorator(ExerciseDecorator):
    def get_description(self):
        return f"{self._exercise.get_description()} Cool-down 3 min "


class StrengthExercise(Exercise):
    def __init__(self):
        super().__init__("Bench press", 10, 3)
        
class StrengthExercise1(Exercise):
    def __init__(self):
        super().__init__("Squad", 15, 3)
        
class StrengthExercise2(Exercise):
    def __init__(self):
        super().__init__("Deadlift", 8, 4)
        
class StrengthExercise4(Exercise):
    def __init__(self):
        super().__init__("Bench press", 12, 1)


class FlexibilityExercise(Exercise):
    def __init__(self):
        super().__init__("Standing lounge", 20, 1)
        
    
class FlexibilityExercise1(Exercise):
    def __init__(self):
        super().__init__("Sawnward dog", 20, 1)
        
class FlexibilityExercise2(Exercise):
    def __init__(self):
        super().__init__("Standing calf strech", 20, 3)
