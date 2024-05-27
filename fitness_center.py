# Singleton Pattern for Fitness Center
class FitnessCenter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FitnessCenter, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.customers = []
        self.training_programs = {}

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_training_program(self, name, program):
        self.training_programs[name] = program

    def notify_customers(self, message):
        for customer in self.customers:
            customer.update(message)
