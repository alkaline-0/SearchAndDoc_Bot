# Contributing to the Project

## Branches
### Main Branch -> main/
The main branch is supposed to be stable and tested at all times. Branches are merged on a trunk based workflow, albeit currently without a development branch.

### Feature Branches -> feature/
For developing new features collaboratively, merged back to main via a Pull Request once it passes tests and review.

Naming examples:
```
feature/authentication
feature/chat-crawler
feature/document-writer
```

### Hotfix Branches -> hotfix/
For urgent fixes with fast-track reviews to ensure stability on main.

## Commit messages

For commit messages there are a few standard prefixes to quickly indicate what the commit roughly does.
- `ADD`: New features or additions
- `FIX`: Bug fixes or corrections
- `DEL`: Remove code or files
- `UPD`: Updates to existing functionalities

Before a feature branch is ready for a PR, the pre-commit needs to be run for linting to check formatting.

