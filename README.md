# salesforce-dev-samples

This repository stores small but useful Salesforce development packages that can be used as practical examples.

## Package organization

Packages must live inside one of these directories:

- `low-code/`
- `high-code/`

Each package must be created as its own directory inside one of the roots above, for example:

```text
low-code/
  my-package/
    force-app/
    DEVELOPMENT.md
    USAGE.md
```

## Minimum data required for each package

Every package must contain:

- at least one component directory
- `DEVELOPMENT.md` describing how the package was developed
- `USAGE.md` explaining how to use the package

## Automatic validation on commits

On every push, GitHub Actions validates all packages found in `low-code/` and `high-code/`.

If one or more packages do not meet the minimum requirements, the workflow:

- fails the validation
- opens an issue mentioning the user who pushed the commit
