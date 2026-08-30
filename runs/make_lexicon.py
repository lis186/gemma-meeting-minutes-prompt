#!/usr/bin/env python3
# ponytail: stage-1 lexicon extractor. 重現 emptylex 對照組：把 meeting-notice-lexicon.txt 清空再跑 run_gemma.py
import json, urllib.request, pathlib
base = pathlib.Path(__file__).resolve().parent.parent
notice = (base / "meeting-notice.txt").read_text()
def extract(instr, seed=1):
    body = {"model": "google/gemma-4-e4b", "messages": [{"role": "user", "content": instr + "\n\n" + notice}],
            "temperature": 0.1, "seed": seed, "max_tokens": 2048}
    req = urllib.request.Request("http://localhost:1234/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    resp = json.load(urllib.request.urlopen(req, timeout=300))
    return (resp["choices"][0]["message"].get("content") or "").strip()
lex = extract("以下是一份會議通知。請只抽出其中的「公司名稱」與「產品或系統名稱」，一行一個，照原文寫法輸出名稱本身。不要輸出人名、日期、地點、角色、標點或任何說明文字。")
if not lex:
    lex = extract("從下面的會議通知抽出所有公司名稱與產品/系統名稱。直接輸出清單，一行一個名稱，照原文寫法。")
assert lex, "fail closed：詞彙表為空，不得進入 stage-2"  # sol: 空輸出/漏抽必須 fail closed
(base / "meeting-notice-lexicon.txt").write_text(lex)
print(lex)
