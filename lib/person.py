#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name  # Use the property setter
        self.job = job  # Use the property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

if __name__ == "__main__":
    alice = Person("Alice Smith", "Marketing")
    print(alice.name)  # Should print "Alice Smith" in title case
    print(alice.job)  # Should print "Marketing"

    bob = Person("Bob Johnson", "Engineering")  # Should print an error message
    bob.name = "Robert Johnson with a Very Long Name"  # Should print an error message

