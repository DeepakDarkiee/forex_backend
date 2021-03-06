from django.contrib import admin
from django.urls import include, path

from accounts.author.api import (
    ForgetPasswordView,
    LoginAuthorAPIView,
    RegisterAuthorView,
)
from accounts.editor.api import (
    ForgetEditorPasswordView,
    LoginEditorAPIView,
    RegisterEditorView,
)
from accounts.reviewer.api import (
    ForgetReviewerPasswordView,
    LoginReviewerAPIView,
    RegisterReviewerView,
)

from accounts.join_us.api import RegisterRoleView

from accounts.views import UpdateProfileApiView, UserDetailApiView

urlpatterns = [
    path("register_author/", RegisterAuthorView.as_view(), name="register_author"),
    path("login_author/", LoginAuthorAPIView.as_view(), name="login_author"),
    path("forget-password/", ForgetPasswordView.as_view(), name="forget-password"),
    # ------------------------------------------------------------------------------
    path("register_editor/", RegisterEditorView.as_view(), name="register_editor"),
    path("login_editor/", LoginEditorAPIView.as_view(), name="login_editor"),
    path(
        "forget-editor-password/",
        ForgetEditorPasswordView.as_view(),
        name="forget-editor-password",
    ),
    # ------------------------------------------------------------------------------
    path(
        "register_reviewer/", RegisterReviewerView.as_view(), name="register_reviewer"
    ),
    path("login_reviewer/", LoginReviewerAPIView.as_view(), name="login_reviewer"),
    path(
        "forget-reviewer-password/",
        ForgetReviewerPasswordView.as_view(),
        name="forget-reviewer-password",
    ),
    # ------------------------------------------------------------------------------
    path(
        "register_editor_reviewer/", RegisterRoleView.as_view(), name="register_editor_reviewer"
    ),
    # ------------------------------------------------------------------------------
    
    path("update-profile/", UpdateProfileApiView.as_view(), name="update_profile"),
    path("user-detail/", UserDetailApiView.as_view(), name="user_detail"),
    
    
]
