# md-ref-links
A GitHub Action that transforms Markdown style [reference links][ref-links-docs] 
to inline links. Useful if your ultimate Markdown-to-HTML renderer doesn't
doesn't support reference links natively.

See the raw Markdown for this file to see an example of a reference link.

## Example usage

```yaml
name: Process Markdown
on: [push]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Transform reference links to inline links 
            uses: stevedatadog/md-ref-links@v1.0.0
            with:
              source-path: /courses/k8s-cluster-troubleshooting/labs/01-first-lab/assignment.md
              destination-path: /courses/k8s-cluster-troubleshooting/labs/01-first-lab/assignment.md
```

[ref-links-docs]: https://www.markdownguide.org/basic-syntax/#reference-style-links
