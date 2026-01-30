# OctoFit Tracker: AI Agent Instructions

This document guides AI agents in developing the OctoFit Tracker fitness application—a full-stack app for PE teachers to engage students in fitness tracking with competitive leaderboards and personalized coaching.

## Project Overview

**Tech Stack**: React.js (frontend) • Django REST API (backend) • MongoDB (database)
**Architecture**: Frontend at `octofit-tracker/frontend/` • Backend at `octofit-tracker/backend/octofit_tracker/`
**Key Features**: User authentication, activity logging, team management, leaderboards, workout suggestions

## Directory Structure and Conventions

```
octofit-tracker/
├── backend/
│   ├── venv/                           # Python 3.9+ virtual environment
│   ├── requirements.txt                # Django 4.1.7, djangorestframework, djongo (MongoDB ORM)
│   └── octofit_tracker/
│       ├── manage.py
│       ├── settings.py
│       └── urls.py
└── frontend/
    ├── public/
    └── src/
        ├── index.js                    # Must import Bootstrap CSS at line 1
        └── components/
```

## Critical Setup Commands

**Never change directories in terminal commands.** Always use absolute paths from workspace root:

```bash
# Python environment activation (use in all backend commands)
source octofit-tracker/backend/venv/bin/activate

# Install backend dependencies
pip install -r octofit-tracker/backend/requirements.txt

# React development server
npm start --prefix octofit-tracker/frontend

# Django migrations and startup
cd octofit-tracker/backend && python manage.py migrate
cd octofit-tracker/backend && python manage.py runserver 0.0.0.0:8000
```

## Port Configuration

**Do NOT propose other ports.** Only use:
- **8000** (public): Django REST API
- **3000** (public): React frontend  
- **27017** (private): MongoDB

Configured in `.devcontainer/devcontainer.json`.

## Backend: Django + MongoDB

### Settings Pattern (settings.py)

```python
import os

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

### Serializer Convention

- Convert MongoDB `ObjectId` fields to strings in serializers
- Example: `id = serializers.SerializerMethodField(read_only=True)`
- Use `def get_id(self, obj): return str(obj.id)`

### URL Configuration

Always support both local and Codespace environments:

```python
import os

codespace_name = os.environ.get('CODESPACE_NAME')
base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
```

### Database Operations

- Use **Django ORM** exclusively—never write direct MongoDB scripts
- Verify MongoDB service: `ps aux | grep mongod`
- Use `mongosh` as the official client (not mongo)
- Models inherit from `djongo.models.Model`

## Frontend: React with Bootstrap

### Initialization

```bash
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
npm install bootstrap react-router-dom --prefix octofit-tracker/frontend
```

### Bootstrap Integration

- Import at **top of src/index.js (line 1)**: `import 'bootstrap/dist/css/bootstrap.min.css';`
- Use Bootstrap utility classes for responsive layouts

### App Image

- Logo: `docs/octofitapp-small.png` (used in header/branding)

## Common Workflows

### Testing REST API Endpoints

Use curl from terminal (no GUI tools needed):
```bash
curl http://localhost:8000/api/users/
curl -X POST http://localhost:8000/api/activities/ -H "Content-Type: application/json" -d '{"type":"run"}'
```

### Debugging Code

- Backend: Use VS Code debugger configured in `.vscode/launch.json` (auto-configured by devcontainer)
- Frontend: Browser DevTools in Chrome (React tab available)

### Environment-Aware Configuration

- Check `os.environ.get('CODESPACE_NAME')` to detect GitHub Codespaces vs local development
- Adjust API URLs, allowed hosts, and CORS based on this flag

## Key Dependencies & Versions

**Backend Critical Versions**:
- Django 4.1.7
- djangorestframework 3.14.0
- djongo 1.3.6 (MongoDB ORM adapter)
- pymongo 3.12
- dj-rest-auth 2.2.6 (auth endpoints)
- django-cors-headers 4.5.0 (frontend cross-origin requests)

**Frontend**:
- React.js (latest via create-react-app)
- Bootstrap 5
- react-router-dom (page routing)

## Agent Mode Best Practices

1. **Always activate venv before Python work**: `source octofit-tracker/backend/venv/bin/activate`
2. **Use fully qualified paths**: Commands reference `octofit-tracker/backend/` explicitly
3. **Test endpoints with curl** after backend changes
4. **Mirror environment detection**: Write code that checks `CODESPACE_NAME` for production readiness
5. **Preserve existing prompts**: `.github/prompts/` contain reusable task templates—reference them for multi-step work

## Related Documentation

- Setup instructions: [.github/instructions/octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
- Django backend: [.github/instructions/octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
- React frontend: [.github/instructions/octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)
- Prompts: [.github/prompts/](./prompts/) for agent-mode task templates
