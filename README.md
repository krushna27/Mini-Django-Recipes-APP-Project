# Django Recipe Management Mini Project

This is a simple Django-based Recipe Management System. It allows users to add, view, update, delete, and search for recipes. Each recipe contains a name, description, and image.

## Features

- Add new recipes with name, description, and image
- View all recipes in a table
- Search recipes by name
- Update existing recipes
- Delete recipes

## Usage

- **Add Recipe:** Fill the form and submit to add a new recipe.
- **Search Recipe:** Use the search bar to filter recipes by name.
- **Update/Delete:** Use the buttons in the table to update or delete recipes.

## Notes

- Uploaded images are stored in the `media/recipe/` directory.
- Make sure `MEDIA_URL` and `MEDIA_ROOT` are properly set in your `settings.py` for image uploads.
- For production, configure static and media file serving appropriately.
