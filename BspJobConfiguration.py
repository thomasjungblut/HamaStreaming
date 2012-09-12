"""

A mimic configuration object contains a dictionary that maps keys to values to store information.

"""
class BspJobConfiguration:
    def __init__(self):
        self.conf = {}

    def get(self, key):
        return self.conf[key]

    def put(self, key, value):
        self.conf[key] = value