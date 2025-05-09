from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from goals.models import Goal


class GoalViewTests(TestCase):
    def setUp(self):
        # Set up two users and one goal
        self.user1 = User.objects.create_user(
            username="alice", password="pass123")
        self.user2 = User.objects.create_user(
            username="bob", password="pass456")

        self.goal = Goal.objects.create(
            user=self.user1,
            title="Alice's Goal",
            description="Important task"
        )

    def test_login_required_for_goal_list(self):
        """
        Unauthenticated users should be redirected to login page.
        """
        response = self.client.get(reverse("goals:goal_list"))
        self.assertRedirects(response, f"{reverse(
            'accounts:login')}?next={reverse('goals:goal_list')}")

    def test_user_can_see_own_goals(self):
        """
        User should see their own goals on the list page.
        """
        self.client.login(username="alice", password="pass123")
        response = self.client.get(reverse("goals:goal_list"))
        self.assertContains(response, "Alice&#x27;s Goal")

    def test_user_cannot_see_others_goals(self):
        """
        Users should not see goals belonging to other users.
        """
        self.client.login(username="bob", password="pass456")
        response = self.client.get(reverse("goals:goal_list"))
        self.assertNotContains(response, "Alice's Goal")

    def test_create_goal(self):
        """
        Logged-in user can create a new goal.
        """
        self.client.login(username="bob", password="pass456")
        response = self.client.post(reverse("goals:goal_create"), {
            "title": "Bob's Goal",
            "description": "Do something productive"
        })
        self.assertEqual(Goal.objects.filter(user=self.user2).count(), 1)
        self.assertRedirects(response, reverse("goals:goal_list"))

    def test_update_own_goal(self):
        """
        Users can update their own goals.
        """
        self.client.login(username="alice", password="pass123")
        response = self.client.post(reverse(
            "goals:goal_update", args=[self.goal.pk]), {
            "title": "Updated Title",
            "description": "Updated description"
        })
        self.goal.refresh_from_db()
        self.assertEqual(self.goal.title, "Updated Title")

    def test_user_cannot_edit_others_goal(self):
        """
        Users should receive 404 when trying to edit another user's goal.
        """
        self.client.login(username="bob", password="pass456")
        response = self.client.post(reverse(
            "goals:goal_update", args=[self.goal.pk]), {
            "title": "Hacked",
            "description": "Shouldn't work"
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_own_goal(self):
        """
        Users can delete their own goals.
        """
        self.client.login(username="alice", password="pass123")
        response = self.client.post(reverse(
            "goals:goal_delete", args=[self.goal.pk]))
        self.assertRedirects(response, reverse("goals:goal_list"))
        self.assertFalse(Goal.objects.filter(pk=self.goal.pk).exists())

    def test_user_cannot_delete_others_goal(self):
        """
        Users cannot delete goals owned by other users.
        """
        self.client.login(username="bob", password="pass456")
        response = self.client.post(reverse(
            "goals:goal_delete", args=[self.goal.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Goal.objects.filter(pk=self.goal.pk).exists())
