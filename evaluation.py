# evaluation.py
from __future__ import annotations

from redactor import redact_text

def calculate_metrics(true_positive: int, false_positive: int, false_negative: int, true_negative: int) -> tuple[float, float, float]:
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0.0
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0.0
    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative) if (true_positive + true_negative + false_positive + false_negative) else 0.0
    return recall, precision, accuracy


def run_simulation() -> tuple[int, int, int, int]:
    test_cases = [
        ("John Doe can be reached at john.doe@example.com or 555-123-4567.", True),
        ("This sentence contains no personal information.", False),
        ("Alice Johnson works at Contoso Ltd and lives at 123 Main Street, New York, NY.", True),
        ("Please review the support documentation for the latest update.", False),
        ("The employee SSN is 123-45-6789 and the card number is 4111 1111 1111 1111.", True),
        ("An internal ticket has been updated successfully.", False),
        ("Jane Smith's IP address is 192.168.1.10 and DOB is 04/12/1990.", True),
        ("Quarterly results were published without any sensitive references.", False),
    ]

    tp = fp = fn = tn = 0

    for original_text, contains_pii in test_cases:
        sanitized_text = redact_text(original_text)
        predicted_positive = sanitized_text != original_text

        if contains_pii and predicted_positive:
            tp += 1
        elif contains_pii and not predicted_positive:
            fn += 1
        elif not contains_pii and predicted_positive:
            fp += 1
        else:
            tn += 1

    return tp, fp, fn, tn


def format_percentage(value: float) -> str:
    return f"{value * 100:.2f}%"


def main() -> None:
    tp, fp, fn, tn = run_simulation()
    recall, precision, accuracy = calculate_metrics(tp, fp, fn, tn)

    print("PII Redaction Evaluation Metrics")
    print("-" * 40)
    print(f"Recall: {format_percentage(recall)}")
    print(f"Precision: {format_percentage(precision)}")
    print(f"Accuracy: {format_percentage(accuracy)}")
    print("-" * 40)
    print(f"TP={tp}  FP={fp}  FN={fn}  TN={tn}")


if __name__ == "__main__":
    main()