# Hosted Image Generation API Lab

AVIP 2026 Generative AI — Task 3. A production-minded image-generation client with typed configuration, retries, request/response capture, cost tracking, and reproducible prompt metadata.

## Run
```bash
pip install -r requirements.txt
cp .env.example .env
python scripts/generate.py --dry-run
```

The adapter is provider-neutral. Set the provider base URL, model, API version, and price in `.env`; never commit credentials. The included dry run validates the full manifest flow without claiming generated output.

## Evidence protocol
- `prompts.txt`: 20 stable prompt IDs
- `scripts/generate.py`: retries, latency, manifest, and cost estimate
- `examples/`: sanitized request/response shapes
- `docs/quality-review.md`: five-output review protocol

The selected provider's official model and terms URL must be recorded in the run manifest when real image generation is executed.
