import unittest
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

from app.storage import load_tasks, save_tasks
from app.tasks import rename_task


class TestRenameTask(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {
                "id": 1,
                "title": "Study Python",
                "done": False,
            },
            {
                "id": 2,
                "title": "Study Git",
                "done": True,
            },
        ]

    def test_rename_existing_task(self):
        result = rename_task(
            self.tasks,
            1,
            "Study Docker",
        )

        self.assertIs(result, True)

        self.assertEqual(
            self.tasks,
            [
                {
                    "id": 1,
                    "title": "Study Docker",
                    "done": False,
                },
                {
                    "id": 2,
                    "title": "Study Git",
                    "done": True,
                },
            ],
        )

    def test_strip_surrounding_spaces(self):
        result = rename_task(
            self.tasks,
            1,
            "   Study Docker   ",
        )

        self.assertIs(result, True)
        self.assertEqual(
            self.tasks[0]["title"],
            "Study Docker",
        )

    def test_reject_blank_titles_without_changes(self):
        invalid_titles = (
            "",
            "   ",
            "\t\n",
        )

        for title in invalid_titles:
            with self.subTest(title=repr(title)):
                before = deepcopy(self.tasks)

                with self.assertRaises(ValueError):
                    rename_task(
                        self.tasks,
                        1,
                        title,
                    )

                self.assertEqual(self.tasks, before)

    def test_missing_id_does_not_change_tasks(self):
        before = deepcopy(self.tasks)

        result = rename_task(
            self.tasks,
            99,
            "Study Docker",
        )

        self.assertIs(result, False)
        self.assertEqual(self.tasks, before)

    def test_empty_list_returns_false(self):
        tasks = []

        result = rename_task(
            tasks,
            1,
            "Study Docker",
        )

        self.assertIs(result, False)
        self.assertEqual(tasks, [])

    def test_rename_completed_task_keeps_done_status(self):
        result = rename_task(
            self.tasks,
            2,
            "Study GitHub",
        )

        self.assertIs(result, True)
        self.assertEqual(
            self.tasks[1]["title"],
            "Study GitHub",
        )
        self.assertIs(
            self.tasks[1]["done"],
            True,
        )
        self.assertEqual(
            self.tasks[1]["id"],
            2,
        )

    def test_same_title_is_successful(self):
        before = deepcopy(self.tasks)

        result = rename_task(
            self.tasks,
            1,
            "Study Python",
        )

        self.assertIs(result, True)
        self.assertEqual(self.tasks, before)

    def test_new_title_survives_save_and_reload(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"

            save_tasks(self.tasks, path)
            loaded_tasks = load_tasks(path)

            result = rename_task(
                loaded_tasks,
                1,
                "Học Python nâng cao",
            )

            self.assertIs(result, True)

            save_tasks(loaded_tasks, path)
            reloaded_tasks = load_tasks(path)

            self.assertEqual(
                reloaded_tasks,
                [
                    {
                        "id": 1,
                        "title": "Học Python nâng cao",
                        "done": False,
                    },
                    {
                        "id": 2,
                        "title": "Study Git",
                        "done": True,
                    },
                ],
            )


if __name__ == "__main__":
    unittest.main()
        
