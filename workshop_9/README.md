# Final Project - Django Web Application

Build a full Django web application of your own choice. The topic is up to you (blog, e-shop, library catalog, recipe manager, task tracker, movie database, etc.), but it MUST satisfy the requirements below.

## Project Idea Examples
- Online store / product catalog
- Blog with posts and comments
- Library / book catalog
- Recipe sharing site
- Task / project manager
- Movie or game database
- Event management system

You may NOT submit a copy of the `web_example` shown in class. Pick your own domain.

## Technical Requirements

### 1. Project Setup
- Django **6.x**, Python **3.14+**
- Use `uv` (or `pip`) with a `pyproject.toml` / `requirements.txt` listing all dependencies
- A clear `README.md` in your repository explaining:
  - What the project is
  - How to install and run it
  - Default admin credentials (for grading)
- Project must run with `python manage.py runserver` after migrations

### 2. Models (minimum 4)
Your app must define **at least 4 models** with:
- At least one `ForeignKey` relationship
- At least one `ManyToManyField` relationship
- At least one `ImageField` or `FileField` (with working media upload)
- At least one custom field validator (e.g. like `validate_product_name`)
- A meaningful `__str__()` on every model
- At least one custom method on a model (e.g. `get_total_inventory_value`)
- `get_absolute_url()` on the main model

### 3. Admin
- All models registered in the Django admin
- Use `list_display`, `list_filter`, `search_fields` where appropriate
- Inline editing for at least one related model (e.g. `TabularInline` / `StackedInline`)

### 4. Views & URLs
- At least **5 views** total (mix of FBVs and CBVs allowed)
- Must include:
  - List view (e.g. all products)
  - Detail view (single object)
  - Create — either `CreateView` **or** a plain view that handles a `ModelForm` POST
  - Update — either `UpdateView` **or** a plain view that handles a `ModelForm` POST with `instance=...`
  - Delete view (with confirmation)
- Use Django's `reverse()` / `reverse_lazy()` for redirects — no hardcoded URLs

### 5. Templates
- Base template with `{% extends %}` and `{% block %}` inheritance
- At least one template tag loop (`{% for %}`) and one conditional (`{% if %}`)
- Use `{% url %}` template tag (no hardcoded links)
- Display uploaded images on the detail page
- Reasonably styled (Bootstrap, Tailwind, or your own CSS is fine)

### 6. Forms
- At least one `ModelForm`
- Server-side validation that displays errors back to the user

### 7. Migrations
- All migrations committed to the repo
- App must migrate cleanly from a fresh database

### 8. Tests
- At least **3 tests** in `tests.py` covering models or views
- Tests must pass: `python manage.py test`

## Bonus (Optional, +points)
- User authentication (login / register / logout)
- Permissions: only the owner can edit/delete their object
- Pagination on the list view
- Search / filter on the list view
- Deployed somewhere (Railway, Fly.io, PythonAnywhere, etc.)
- `django-debug-toolbar` configured for dev

## Submission
1. Push the project to a **public GitHub repository**
2. Repo name suggestion: `python-125-final-project`
3. Include a populated `README.md` (see Section 1)
4. Commit your `db.sqlite3` with sample data OR provide a `loaddata` fixture
5. Share the repository link with the instructor

## Grading Rubric (100 pts)
| Area | Points |
|---|---|
| Project runs & migrates cleanly | 10 |
| Models meet requirements | 20 |
| Admin configuration | 10 |
| Views (CRUD) | 20 |
| Templates & inheritance | 15 |
| Forms & validation | 10 |
| Tests pass | 10 |
| Code quality & README | 5 |
| **Bonus** | up to +15 |

## Deadline
Submit before the next class. Late submissions lose 10 points per day.

## Tips
- Start with models — get them right before touching views
- Use the admin to add sample data while you build views
- Commit often with meaningful messages
- Look at `workshop_9/web_example/` for patterns, but build your OWN domain
