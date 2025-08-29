# Blog Application

This is a simple Django blog application with CRUD (Create, Read, Update, Delete) functionality for posts.

## Features
- **Create Post**: Authenticated users can create a new blog post. The author is automatically set to the logged-in user.
- **Update Post**: Only the post author can edit their post.
- **Delete Post**: Only the post author can delete their post.
- **View Posts**: Posts are displayed in a list and can be viewed individually.

## Permissions
- **Login Required**: Users must be logged in to create, edit, or delete posts.
- **Author Restriction**: Users can only edit or delete their own posts. This is handled using `UserPassesTestMixin`.

## Forms
- Uses Django’s `ModelForm` to handle post creation and updates.
- Fields included: `title`, `content`.
- Author is automatically set in the view (`form_valid` method).

## Templates
- `post_list.html`: Displays all posts.
- `post_detail.html`: Displays a single post.
- `post_form.html`: Form for creating and editing posts.
- `post_confirm_delete.html`: Confirmation page for deleting a post.

## Notes
- Ensure migrations are applied before running.
- Login/logout functionality must be set up for permissions to work properly.
