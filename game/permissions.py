from rest_framework import permissions


class HasAccessToGame(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user == obj.owner:
            return True

        if request.user == obj.opponent:
            return True

        if not obj.private:
            return True

        return False


class HasAccessToGameRelatedModels(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user == obj.game.owner:
            return True

        if request.user == obj.game.opponent:
            return True

        if not obj.game.private:
            return True

        return False
