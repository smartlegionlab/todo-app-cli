# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# --------------------------------------------------------
"""Tests for TaskView.get_task_name.

A task name made only of whitespace must be rejected just like an
empty name, and surrounding whitespace must not be stored.
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

from core.view import TaskView


class GetTaskNameTests(unittest.TestCase):
    def run_get_task_name(self, inputs):
        view = TaskView()
        with mock.patch("builtins.input", side_effect=inputs):
            with redirect_stdout(io.StringIO()):
                return view.get_task_name()

    def test_whitespace_only_name_is_rejected(self):
        """'   ' then Enter, '' then Enter, then a real name."""
        name = self.run_get_task_name(["   ", "", "", "", "  real task  "])
        self.assertEqual(name, "real task")

    def test_surrounding_whitespace_is_stripped(self):
        """Stored names carry no leading/trailing whitespace."""
        name = self.run_get_task_name(["  buy milk  "])
        self.assertEqual(name, "buy milk")


if __name__ == "__main__":
    unittest.main()
