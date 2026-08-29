#!/usr/bin/env python3
# ponytail: minimal runner — prompt file + transcript -> LM Studio chat completion
import json, sys, urllib.request, pathlib

prompt_file, out_file = sys.argv[1], sys.argv[2]
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
base = pathlib.Path("/Users/justinlee/HybridAIWorkshop/execerice")
prompt = (base / prompt_file).read_text() if not prompt_file.startswith("/") else pathlib.Path(prompt_file).read_text()
transcript = (base / "transcript-software.txt").read_text()

body = {
    "model": "google/gemma-4-e4b",
    "messages": [{"role": "user", "content": prompt.rstrip() + "\n" + transcript.strip() + "\n--- 逐字稿結束 ---"}],
    "temperature": 0.1,
    "seed": seed,
    "max_tokens": 4096,
}
req = urllib.request.Request("http://localhost:1234/v1/chat/completions",
                             json.dumps(body).encode(), {"Content-Type": "application/json"})
resp = json.load(urllib.request.urlopen(req, timeout=600))
msg = resp["choices"][0]["message"]
out = pathlib.Path(out_file)
out.write_text(msg.get("content") or "")
# stash reasoning + raw for inspection
if msg.get("reasoning_content"):
    out.with_suffix(".think.txt").write_text(msg["reasoning_content"])
out.with_suffix(".raw.json").write_text(json.dumps(resp, ensure_ascii=False, indent=1))
print("keys:", list(msg.keys()), "| finish:", resp["choices"][0].get("finish_reason"), "| usage:", resp.get("usage"))
