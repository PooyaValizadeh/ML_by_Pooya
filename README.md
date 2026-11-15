# ML by Pooya

A learning portfolio of machine-learning, deep-learning, data-analysis, and NLP notebooks and small projects.

## Repository map

```text
.
├── projects/
│   ├── classification/
│   │   ├── arff-to-csv/
│   │   └── telecom-customer/
│   ├── clustering/
│   │   ├── fuel-consumption/
│   │   └── series/
│   ├── deep-learning/
│   │   ├── ai-diddy/
│   │   └── DL_bool_sheets/              # Dated experiments, CIFAR-10, YOLO, segmentation
│   └── regression/
│       └── china-gdp/
├── tutorials/
│   ├── pandas/
│   ├── preprocessing/
│   └── scikit-learn/
├── datasets/
│   └── shared-root/                # Existing root-level datasets retained during cleanup
├── README.md
└── .gitignore
```

## Projects and learning areas

| Area | Contents |
|---|---|
| Deep learning | Activation functions, optimization experiments, CIFAR-10, image segmentation, and YOLO |
| IBM machine learning course | Classification, regression, and clustering exercises, with course datasets |
| Classification | Telecom customer classification and ARFF-to-CSV workflow |
| Clustering | Fuel-consumption and streaming-series clustering |
| Regression | China GDP polynomial/regression experiment |
| NLP | Maktabkhooneh project |
| Tutorials | Pandas tips, preprocessing experiments, and scikit-learn pipelines |

## Working with notebooks

- Open a notebook in JupyterLab, VS Code, or Google Colab.
- Run a notebook from its own project directory when it reads a local CSV using a relative filename.
- Several IBM course notebooks download their own datasets with `wget`; run those cells before the data-loading cells.
- The CIFAR-10 experiment notebook that loads `model_cifar10.keras` must remain alongside that model file.
- Existing notebook outputs and model artifacts are retained as part of the learning record.

## Dependencies

There is intentionally no single root `requirements.txt`: projects use different stacks and some older IBM course notebooks pin legacy package versions. Install dependencies from the `requirements.txt` inside the project you intend to run. For notebooks without one, install the imports used by that notebook in a dedicated virtual environment.

## Repository hygiene

- Keep datasets beside the project that uses them, unless they are genuinely shared.
- Keep model checkpoints with the experiment that created or loads them.
- Avoid committing virtual environments, Python caches, temporary notebook checkpoints, and local editor settings.
- Prefer descriptive notebook names when adding new work; keep dated experiment notebooks grouped in the deep-learning notebooks folder.
