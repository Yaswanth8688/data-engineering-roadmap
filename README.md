# Data Engineering Roadmap

This repository organizes short, practical learning modules for data engineers.
Each module focuses on a core area and includes examples, exercises and notes.

Quick links (existing modules)
- [airflow-core](../airflow-core) — Airflow DAGs, operators, and orchestration patterns.
- [etl-core](../etl-core) — ETL design patterns, pipeline examples and exercises.
- [python-core](.) — Python fundamentals and data-engineering focused examples.
- [sql-core](../sql-core) — SQL fundamentals, example queries, and exercises.

Planned modules (placeholders)
- `data-platform`, `data-processing`, `docker-core`, `kafka-core`, `pyspark-core` — coming soon.

Getting started
- Open the module directory you're interested in (see Quick links) and read its `README.md`.
- Typical folder contents: `examples/`, `exercises/`, `docs/`.

How to contribute
- Fork or clone the repo, create a small feature branch, add content, and submit a PR.
  Suggested workflow:

```bash
git clone git@github.com:Yaswanth8688/data-engineering-roadmap.git
cd data-engineering-roadmap/python-core
git checkout -b feat/my-new-examples
# add files, run tests
git add . && git commit -m "feat: add examples for ..."
git push origin feat/my-new-examples
# open a pull request on GitHub
```

License
- This repository uses the MIT license where specified in module folders.
