from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('complete_signup', views.complete_signup, name='complete_signup'),
    path('profilecreation', views.create_profile_view, name='createprofile'),
    path('complete_profile', views.complete_profile, name='complete_profile'),
    path('home', views.home, name='home'),
    path('do_search', views.do_search, name='do_search'),
    path('profile/<int:profile_id>', views.profile_view, name='profile_view'),
    path('event/<int:event_id>', views.event_view, name='event'),
    path('profile', views.profile_view, name='profileview'),
    path('profile/post_message', views.profile_post_message_view, name='profile_post_message'),
    path('profile/edit', views.profile_edit_view, name='profileedit'),
    path('profilecreation/upload', views.profile_image_upload_endpoint, name='profile_image_upload_endpoint'),
    path('categories', views.subjectlist_view, name='subjectlist'),
    path('event/<int:event_id>/decision', views.event_management_view, name='eventmanagement'),
    path('event/<int:event_id>/edit', views.event_edit_view, name='eventedit'),
    path('signin', views.signin, name='signin'),
    path('messaging', views.messaging, name='messaging'),
    path('messaging/post_message', views.messaging_post_message_view, name='messaging_post_message'),
    path('signout', views.signout, name='signout'),
    # path('filtered_matches', views.get_filtered_matching, name='get_filtered_matching'),
    path('signin/auth', views.login_auth_view, name='login_auth'),
]
