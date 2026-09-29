# Hosted Image Generation API Lab

A production-minded image-generation client and live prompt studio for AVIP 2026.

## Live demo

**Image Lab:** https://novaai-8endm8ng.manus.space/image-lab

The demo accepts a prompt and aspect ratio, sends the request to a server-side image endpoint, and displays the returned image. Platform credentials never reach the browser.

## Real inference evidence

A real image request was completed through the managed image runtime and saved as `runs/real-inference-001.png` with metadata in `runs/real-inference-001.json`.

- Model: `MODEL_GEMINI_2_5_FLASH_IMAGE_PREVIEW`
- Aspect ratio: `1:1`
- Safety result: `passed`
- Prompt: editorial still life of a cobalt ceramic cup on a pale stone table

## Local CLI

```bash
pip install -r requirements.txt
cp .env.example .env
python scripts/generate.py --dry-run
```

The CLI keeps provider configuration, retries, request and response capture, latency, cost estimates, and reproducible prompt metadata in one place. Credentials belong only in environment variables.

## Evidence protocol

- `prompts.txt` contains stable prompt IDs
- `scripts/generate.py` handles retries, latency, manifest, and cost estimates
- `examples/` contains sanitized request and response shapes
- `docs/quality-review.md` defines a five-output review protocol
- `runs/real-inference-001.json` records a completed real inference
