"""
__dict__ -> show attributes and methods will be accessible by dot '.' on a class
"""
class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr) -> None:
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute {self.class_attr}")
        print(f"Instance attribute {self.instance_attr}")




print(
    SampleClass.__dict__
)

print(
    SampleClass.__dict__['class_attr']
)