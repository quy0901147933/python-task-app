import unittest 

from app.tasks import complete_task 

class TestCompleteTask(unittest.TestCase):
    def test_existing_id(self):
        tasks = [
            {"id": 1, "title": "Study Python", "done": False}
        ]
        result = complete_task(tasks, 1)
        self.assertIs(result, True)
        self.assertIs(tasks[0]["done"], True)
    
    def test_missing_id(self):
        tasks = [
            {"id": 1, "title": "Study Git", "done": False}
        ]
        before = [task.copy() for task in tasks]

        result = complete_task(tasks, 99)

        self.assertIs(result, False)
        self.assertEqual(before, tasks)
    
    def test_empty_list(self):
        self.assertIs(complete_task([],1), False)