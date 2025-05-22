# Contributing to Logflow

Thanks for your interest in contributing! Whether it's a bug fix, feature idea, or documentation update, you're welcome here.

## Ways to Contribute

- Submit issues for bugs, edge cases, or suggestions
- Improve the CLI experience or argument parsing
- Add optional integrations (Git commit capture, editor support)
- Write tests for lifecycle functions
- Help document example workflows or use cases

## Development Setup

```bash
poetry install
poetry run logflow help
```

## Running Tests

```bash
poetry run pytest
```

## Submitting Pull Requests

1. Fork the repo
2. Create a feature branch
3. Ensure tests pass
4. Submit a pull request with a clear description

## Code Style

- Use `black` for formatting
- Keep code Pythonic and readable
- Avoid adding dependencies unless optional or essential