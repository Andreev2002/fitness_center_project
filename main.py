from fitness_center import FitnessCenter
from customer import Customer
from exercise import (
    Exercise,
    WarmUpDecorator,
    CoolDownDecorator,
    StrengthExercise,
  
    FlexibilityExercise,
    StrengthExercise1,
    StrengthExercise2,
    StrengthExercise4,
    FlexibilityExercise1,
    FlexibilityExercise2
 
)
from training_program import TrainingProgram, StrengthTraining

if __name__ == "__main__":
    # Initialize the fitness center (Singleton)
    fitness_center = FitnessCenter()
    
    # Create customers (Observer)
    customer1 = Customer("Atanas Andreev")
    customer2 = Customer("Ivan Ivanov")
    fitness_center.add_customer(customer1)
    fitness_center.add_customer(customer2)
    
    # Create training programs (Strategy)
    strength_program = TrainingProgram("Strength", [
        WarmUpDecorator(StrengthExercise4()),
        StrengthExercise(),
        StrengthExercise1(),
        CoolDownDecorator(StrengthExercise2())
    ])
    

    
    flexibility_program = TrainingProgram("Flexibility", [
        WarmUpDecorator(FlexibilityExercise()),
        FlexibilityExercise1(),
        CoolDownDecorator(FlexibilityExercise2())
    ])
    
    # Add training programs to the fitness center
    fitness_center.add_training_program("Strength", strength_program)
    fitness_center.add_training_program("Flexibility", flexibility_program)
    
    # Notify customers about new programs
    fitness_center.notify_customers("New programs available!")
    
    # Execute training programs
    strength_program.execute()
    flexibility_program.execute()
