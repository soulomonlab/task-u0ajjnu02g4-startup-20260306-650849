# ML Repo Layout Proposal

Purpose
- Provide a clear, production-ready repo layout for ML components that supports reproducible experiments, CI, and easy handoff to backend and infra teams.

Top-level layout (MECE)
- /data/                -> Raw and processed data pointers (NOT large blobs). Use DVC for pointers.
- /data/raw/            -> Raw data pointers (DVC tracked)
- /data/processed/      -> Processed datasets (DVC tracked)
- /src/                 -> All source code (package importable as `src`)
  - /src/models/        -> Model architectures and PyTorch modules
  - /src/train/         -> Training scripts and training CLI entrypoints
  - /src/eval/          -> Evaluation and metric calculation
  - /src/features/      -> Feature engineering pipeline code
  - /src/serving/       -> Model serialization, inference wrappers, client utilities
  - /src/data/          -> Data loaders, dataset definitions
  - /src/utils/         -> Common utilities, logging, config
- /notebooks/           -> Analysis & EDA notebooks (narrow scope, reproducible snapshots)
- /experiments/         -> Lightweight experiment metadata (if not in MLflow)
- /models/              -> Trained model artifacts (small samples for CI only; full artifacts in remote store)
- /configs/             -> YAML configs for training and serving
- /.github/             -> CI workflows, issue templates, PR templates
- /ci/                  -> CI helper scripts & smoke tests
- /tests/               -> Unit + integration tests (pytest)
- /docker/              -> Dockerfiles for training/serving images
- /infra/               -> IaC snippets for model infra (deployment manifests)
- /docs/                -> Onboarding & runbooks
- /tools/               -> CLI tools (e.g., data sanity checks)
- /dvc.yaml             -> DVC pipeline definition
- /mlflow/              -> MLflow project files (optional)
- /README.md            -> High-level developer onboarding

Key decisions & rationale
- Keep data out of git: use DVC + remote storage (S3/GCS). Reason: repo remains small and reproducible.
- Source under `src/` to enable proper packaging/imports and simpler test discovery.
- CI should run smoke training on a tiny subset to verify pipelines without heavy compute.
- Model artifacts should be registered in MLflow (or a model registry) for traceability.

Reproducibility checklist (for repo maintainers)
- Enforce deterministic seeds in training scripts
- Pin dependency versions in requirements.txt and use constraints.txt
- Add MLflow or `src/train` wrapper to log hyperparams + artifacts
- DVC remote configured and accessible by CI/infra accounts

Integration points (who to notify)
- #ai-data (Samantha): DVC remote, sample datasets, data schema
- #ai-devops (Noah): storage credentials, container build & deployment
- #ai-backend (Marcus): API serving path, model artifact contract

Minimal files to include in repo skeleton
- README.md (with quickstart)
- CONTRIBUTING.md
- requirements.txt + requirements-dev.txt
- dvc.yaml
- .github/workflows/ci-ml.yml (sample CI)
- PR_TEMPLATE_ML.md

