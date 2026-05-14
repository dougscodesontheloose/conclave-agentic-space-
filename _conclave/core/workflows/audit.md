---
description: Audit project dependencies for vulnerabilities using $ARGUMENTS
---

This workflow audits your project dependencies and attempts to fix them.

**Target Path**: $ARGUMENTS (Default: current directory)

1. Run security audit:
   // turbo
   `npm audit`

2. Attempt to fix vulnerabilities:
   // turbo
   `npm audit fix`

3. Verify integrity:
   // turbo
   `npm test`

Summary:
- Audited: $ARGUMENTS
- Fixes applied
- Tests verified
