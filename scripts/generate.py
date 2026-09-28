import argparse, json, os, time
from pathlib import Path
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

def load_prompts():
    return [line.strip() for line in (ROOT / "prompts.txt").read_text().splitlines() if line.strip()]

def generate(prompt_id, prompt, dry_run=False):
    payload = {"model": os.getenv("IMAGE_MODEL", "provider-image-model"), "prompt": prompt, "size": "1024x1024", "n": 1}
    if dry_run:
        return {"id": prompt_id, "status": "dry_run", "request": payload}
    url = os.environ["IMAGE_API_BASE"].rstrip("/") + "/images/generations"
    headers = {"Authorization": f"Bearer {os.environ['IMAGE_API_KEY']}", "Content-Type": "application/json"}
    for attempt in range(3):
        started = time.perf_counter()
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=120)
            r.raise_for_status()
            data = r.json()
            return {"id": prompt_id, "status": "ok", "latency_s": round(time.perf_counter()-started, 3), "response": data}
        except requests.RequestException as exc:
            if attempt == 2: return {"id": prompt_id, "status": "error", "error": str(exc)}
            time.sleep(2 ** attempt)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int, default=20); ap.add_argument("--dry-run", action="store_true"); args = ap.parse_args()
    out = ROOT / "runs"; out.mkdir(exist_ok=True)
    results = [generate(f"img-{i:02d}", line.split(" | ",1)[1], args.dry_run) for i,line in enumerate(load_prompts()[:args.limit],1)]
    manifest = {"model": os.getenv("IMAGE_MODEL"), "api_version": os.getenv("IMAGE_API_VERSION"), "count": len(results), "estimated_cost_usd": len(results)*float(os.getenv("IMAGE_PRICE_PER_IMAGE_USD", "0")), "results": results}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps({"count": len(results), "manifest": str(out / "manifest.json")}, indent=2))
if __name__ == "__main__": main()
