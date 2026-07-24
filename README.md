# PII Redaction Tool

This project provides a lightweight enterprise-style Word document redaction workflow for detecting and replacing personally identifiable information (PII) in `.docx` files.

## What it does

The tool reads a Word document from the `input_docs` folder, identifies sensitive fields such as:

- full names
- email addresses
- phone numbers
- company names
- physical addresses
- IDs such as PAN/SSN-style values
- credit card numbers
- dates of birth
- IP addresses

It uses a hybrid approach:

- regular expressions for structured PII detection
- spaCy NER with `en_core_web_sm` for unstructured entity detection

Detected values are replaced with consistent fake alternatives using the `Faker` library, and the sanitized output is saved into the `output_docs` folder.

## How to run

From the project root, activate the workspace virtual environment and run:

```powershell
.\.venv\Scripts\python.exe redactor.py
```

This will:

1. read the first `.docx` file in `input_docs`
2. redact PII in the document
3. save a sanitized copy to `output_docs`
4. print evaluation metrics in the terminal

## Evaluation

The evaluation script can be run separately with:

```powershell
.\.venv\Scripts\python.exe evaluation.py
```

It prints recall, precision, and accuracy percentages for the simulated evaluation run.
