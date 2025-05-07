from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from goals.models import Goal

class GoalSecurityTests(TestCase):
    def setUp(self):
        # Setup two users and a goal
        self.user1 = User.objects.create_user(
            username="alice", password="pass123")
        self.user2 = User.objects.create_user(
            username="bob", password="pass456")

        self.goal = Goal.objects.create(
            user=self.user1,
            title="Secure Goal"
        )

    def test_unauthenticated_cannot_access_goal_views(self):
        """
        Unauthenticated users should be redirected
        when accessing goal views.
        """
        urls = [
            reverse("goals:goal_list"),
            reverse("goals:goal_create"),
            reverse("goals:goal_update", args=[self.goal.pk]),
            reverse("goals:goal_delete", args=[self.goal.pk]),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    def test_404_on_nonexistent_goal(self):
        """
        Accessing a goal that doesn't exist should return 404.
        """
        self.client.login(username="alice", password="pass123")
        response = self.client.get(reverse(
            "goals:goal_update", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_access_other_users_goal_directly(self):
        """
        A user should get 404 if trying to edit
        or delete another user's goal.
        """
        self.client.login(username="bob", password="pass456")

        edit_url = reverse("goals:goal_update", args=[self.goal.pk])
        delete_url = reverse("goals:goal_delete", args=[self.goal.pk])

        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 404)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 404)

    def test_cannot_create_goal_with_invalid_data(self):
        """
        Submitting invalid form data should not create a new goal.
        """
        self.client.login(username="alice", password="pass123")
        response = self.client.post(reverse("goals:goal_create"), {
            "title": "",  # Required field
        })
        self.assertEqual(response.status_code, 200)  # Form re-rendered
        self.assertEqual(Goal.objects.filter(user=self.user1).count(), 1)
