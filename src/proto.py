
from modules.vabase import VoiceAssistantBase


class TasklistAssistant(VoiceAssistantBase):

    def __init__(self):
        self.tasklist = []
        self._task_index = {}

    def add_task(self, task, category=None, deadline=None):
        if task in self._task_index:
            raise Exception("Task Already Exists")
        t = {"task": task.lower(), "category": category, deadline: "deadline"}
        self.tasklist.append(t)
        self._task_index[task] = t

    def remove_last_task(self):
        t = self.tasklist.pop()
        if t['task'] in self._task_index:
            del self._task_index[t['task']]

    def remove_all_tasks(self):
        self.tasklist = []
        self._task_index = {}

    def remove_task(self, task):
        self.tasklist = list(filter(lambda x: x['task'] == task.lower(), self.tasklist))
        if task in self._task_index:
            del self._task_index[task]

    def update_task(self, task, new_task=None, new_category=None, new_deadline=None):
        if task in self._task_index:
            t = self._task_index[task]
            if new_task is not None:
                if new_task in self._task_index:
                    raise Exception("Task Already Exists")
                t['task'] = task
                # upd keys
                self._task_index[new_task] = t
                del self._task_index[task]
            if new_category is not None:
                t['category'] = new_category
            if new_deadline is not None:
                t['deadline'] = new_deadline
