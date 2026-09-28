# Hosted Image Generation API Lab

AVIP 2026 Generative AI — Task 3. A production-minded image-generation client with typed configuration, retries, request/response capture, cost tracking, and prompt metadata.

## Why this is resume-worthy
- Uses a provider adapter instead of hard-coding a single vendor.
- Keeps secrets in environment variables and redacts them from logs.
- Captures reproducibility metadata: model, API version, prompt ID, latency, and usage.
- Includes retry/backoff handling and a dry-run mode for safe testing.

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/generate.py --dry-run
# Real run after setting IMAGE_API_KEY:
python scripts/generate.py --limit 20
```

Do not commit `.env` or API keys. The `generated_images/` directory is intentionally git-kept with `.gitkeep`; generated outputs should be reviewed for provider terms before publishing.

## AVIP evidence
- `prompts.txt`: 20 varied prompts with stable IDs
- `scripts/generate.py`: request code, retries, metadata, and cost note
- `examples/`: sanitized request/response examples
- `docs/quality-review.md`: output-quality and failure review template

## Model and terms
Set `IMAGE_MODEL` and record the exact provider model/API version in `runs/manifest.json`. Add the provider's official terms URL before submission.
