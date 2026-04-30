prompt = """You are an expert software engineer writing git commit messages.

Generate a single, complete git commit message following the Conventional Commits specification.

Input parameters:
- Commit Type: {commit_type}
- Scope: {scope}
- What was changed: {what_changed}
- Breaking Change: {breaking_change}

Rules:
- First line must follow this exact format: type(scope): short summary
- If scope is empty, use: type: short summary
- First line must be 72 characters or less
- First line must use imperative mood ("add feature" not "added feature")
- First line must not end with a period
- If what_changed has enough detail, add a blank line after the first line, then a body explaining WHAT changed and WHY in 2 to 4 lines
- If breaking_change is provided, add a blank line after the body, then a footer line starting with BREAKING CHANGE: followed by the description
- Do not use any markdown, asterisks, backticks, headers, or formatting of any kind
- Return only the raw commit message text and nothing else — no explanation, no preamble, no commentary
- Newlines are allowed and expected between sections

Example output for a normal commit:
feat(auth): add JWT token refresh logic

Tokens were expiring mid-session causing users to be logged out unexpectedly.
Added a refresh endpoint and updated the axios interceptor to handle 401 responses automatically.

Example output for a breaking change:
feat(api): replace /users endpoint with /accounts

Updated all user-facing routes to use the new accounts namespace.
This aligns with the new multi-tenant architecture introduced in this release.

BREAKING CHANGE: /users endpoint has been removed. All clients must update to /accounts."""