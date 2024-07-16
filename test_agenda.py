import unittest
from agenda import Agenda


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("Meeting", "2023-03-15", "Discuss project updates")
        self.assertEqual(len(self.agenda.events), 1)
        self.assertEqual(self.agenda.events[0].title, "Meeting")
        self.assertEqual(self.agenda.events[0].date, "2023-03-15")
        self.assertEqual(self.agenda.events[0].description, "Discuss project updates")

    def test_remove_event(self):
        self.agenda.add_event("Meeting", "2023-03-15", "Discuss project updates")
        self.agenda.add_event("Doctor's appointment", "2023-03-20", "Annual check-up")
        self.agenda.remove_event("Meeting")
        self.assertEqual(len(self.agenda.events), 1)
        self.assertEqual(self.agenda.events[0].title, "Doctor's appointment")

    def test_list_events(self):
        self.agenda.add_event("Meeting", "2023-03-15", "Discuss project updates")
        self.agenda.add_event("Doctor's appointment", "2023-03-20", "Annual check-up")
        events_list = self.agenda.list_events()
        expected_list = "Meeting on 2023-03-15: Discuss project updates\nDoctor's appointment on 2023-03-20: Annual check-up"
        self.assertEqual(events_list, expected_list)


if __name__ == "__main__":
    unittest.main()
