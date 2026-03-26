# DEBUGGING.md

## 1) Issues Found

### Functionality bugs

- **Workflow only runs on push**  
  No PR checks, so bad code can be merged.

- **Deploy step runs every time**  
  No deploy condition, so it can run when not intended.

- **No guarantee deploy script works**  
  It calls `./deploy.sh` without checking file/permissions.

### Security issues

- **Using `actions/checkout@latest`**  
  `@latest` can change anytime and break runs.

- **Hardcoded API key**  
  API key in YAML is unsafe. It should be in Secrets.

### Best practice issues

- **Outdated Node version**  
  Node 16 is old and not ideal for new deps.

- **No separation between CI and deploy**  
  CI and deploy are mixed, which makes debugging harder.

## 2) Corrected Workflow

```yaml
name: Build

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      # Check out repository code
      - name: Checkout code
        uses: actions/checkout@v4

      # Set up Node.js
      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      # Install dependencies
      - name: Install dependencies
        run: npm ci

      # Run tests
      - name: Run tests
        run: npm test

      # Build application
      - name: Build
        run: npm run build

      # Deploy only from main branch
      - name: Deploy
        if: github.ref == 'refs/heads/main'
        run: ./deploy.sh
        env:
          API_KEY: ${{ secrets.API_KEY }}
```

## 3) Explanation of Fixes

- **Added pull request and manual triggers**  
  CI now runs on PRs and manual runs. Issues show up before merge.

- **Pinned action version**  
  Pinned versions avoid random breakage from `@latest`.

- **Updated Node version**  
  Moved to Node 20 for better support and security.

- **Used GitHub Secrets for API key**  
  API key is now in Secrets, not in code.

- **Added condition to deploy step**  
  Deploy runs only on `main`, so accidental deploys are reduced.

- **Used `npm ci` instead of `npm install`**  
  `npm ci` is deterministic and lockfile-based, so CI is more consistent.

## 4) Additional Improvement

Split deploy into a separate workflow. Keeps CI cleaner and failures easier to trace.
