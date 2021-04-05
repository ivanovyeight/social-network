from datetime import date

from rest_framework.permissions import BasePermission


class SubscriptionIsActive(BasePermission):
    def has_permission(self, request, view):
        today = date.today()
        paid_until = request.user.profile.paid_until
        return today <= paid_until
