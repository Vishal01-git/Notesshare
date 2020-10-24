from django.contrib import admin
from django.urls import path 
from notes import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('',views.index,name='index'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
   path('login',views.userlogin,name='login'),
   path('login_admin',views.login_admin,name='login_admin'),
   path('signup',views.signup1,name='signup'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('logout',views.Logout,name='logout'),
   path('profile',views.profile,name='profile'),
   path('changepassword',views.changepassword,name='changepassword'),
   path('edit_profile',views.edit_profile,name='edit_profile'),
   path('upload_notes',views.upload_notes,name='upload_notes'),
   path('view_mynotes',views.view_mynotes,name='view_mynotes'),
   path('delete_mynotes/<int:pid>',views.delete_mynotes,name="delete_mynotes"),
   path('view_users',views.view_users,name="view_users"),
   path('delete_users/<int:pid>',views.delete_users,name="delete_users"),
   path('pending_notes',views.pending_notes,name='pending_notes'),
   path('accepted_notes',views.accepted_notes,name='accepted_notes'),
   path('rejected_notes',views.rejected_notes,name='rejected_notes'),
   path('all_notes',views.all_notes,name='all_notes'),
   path('assign_status/<int:pid>',views.assign_status,name="assign_status"),
    path('delete_notes/<int:pid>',views.delete_notes,name="delete_notes"),
     path('viewallnotes',views.viewallnotes,name='viewallnotes'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
