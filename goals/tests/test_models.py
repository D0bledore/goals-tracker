from django.test import TestCase
from django.contrib.auth.models import User
from goals.models import Goal


class GoalModelTests(TestCase):
    def setUp(self):
        # Create a test user for assigning goals
        self.user = User.objects.create_user(
            username="goaluser", password="testpass")

    def test_goal_creation(self):
        """
        Ensure a Goal object is created correctly with required fields.
        """
        goal = Goal.objects.create(
            user=self.user,
            title="Finish MVP",
            description="Build core features and ship"
        )
        self.assertEqual(goal.title, "Finish MVP")
        self.assertEqual(goal.user, self.user)
        self.assertFalse(goal.is_completed)  # Default should be False

    def test_goal_str_representation(self):
        """
        Ensure the __str__ method returns the goal's title.
        """
        goal = Goal.objects.create(user=self.user, title="Write tests")
        self.assertEqual(str(goal), "Write tests")

    def test_goal_default_completed_false(self):
        """
        Ensure that is_completed defaults to False.
        """
        goal = Goal.objects.create(user=self.user, title="Learn Django")
        self.assertFalse(goal.is_completed)
