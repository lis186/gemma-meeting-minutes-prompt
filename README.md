# gemma-meeting-minutes-prompt

用本地小模型（gemma-4-e4b, 4B, LM Studio, thinking mode）把無說話者標籤的 ASR 逐字稿整理成商務會議紀錄的 prompt 迭代實驗。

**迭代方式**：Claude Fable 5 改 prompt → 每版跑 3 個 seed → GPT-5.6-sol 依四步復盤框架（列錯+根因 → 三關 → 結構型/行為型 → 只留最高槓桿 1 項）評判，直到 sol 判定可商用或宣告天花板。

## 驗收標準

1. 時程含正確日期（逐字稿：「我們的合約是 8 月 31 號要驗收」，且不得綁錯事件）
2. 專有名詞正確（ASR 誤字：金牛→金流、postg→POS 機），但 prompt 不能過度擬合（不得硬寫答案）
3. 無法確認的部分（可疑公司名等）明確列出

## 五版迭代結果

| 版本 | 修法（sol 每輪只留最高槓桿 1 項） | 關鍵結果（3 seeds） |
|---|---|---|
| v1 | 原始 | 8/31 消失 3/3、金牛/postg 未修、負責人捏造 3/3 |
| v2 | + 靜默核對清單 | 8/31 出現但綁錯事項（掛到客戶簽約期限） |
| v3 | 抽象證據綁定取代清單 | 惡化：前提被升格成決議 |
| v4 | 固定區段「重要時程／名稱待確認」+ 局部 few-shot | 8/31 綁對、可疑名稱開始揭露 |
| v5 | 完整端到端虛構 few-shot | 8/31 綁定 3/3 正確、「12 筆同一門市」3/3 保留；但「客戶簽約→我們才拿到金鑰」主體合併 3/3 未解 |

## sol 最終判定（第五輪）

- **單 prompt + 4B 已到天花板**：15 次輸出 0 次完整通過驗收，不值得再改 prompt。
- **專名還原不可靠**：無詞表、不過擬合前提下，金牛→金流 這類正字超出 4B 能力；務實解＝不刪不猜、強制列入「名稱待確認」交人工。
- **可用形態**：v5 以「AI 草稿＋人工覆核」上線（2 分鐘會議約 3–5 分鐘人工核對）；全自動需 stage-2 機械/語意 validator + 領域詞表（詞表是可重複使用的業務資產，不算過擬合）。

## 檔案導覽

```
prompt-v1.txt ~ prompt-v5.txt   五版 prompt（v1=原始標的）
transcript-software.txt          測試逐字稿（不可改，含 ASR 誤字）
runs/
  run_gemma.py                   執行腳本（LM Studio API, temp 0.1, seed 可指定）
  vN-runM.md                     第 N 版第 M 個 seed 的會議紀錄輸出
  vN-runM.think.txt              對應的 thinking 過程
  vN-runM.raw.json               原始 API 回應
  sol-review-request-vN.md       每輪給 sol 的復盤請求
  sol-review-vN.md               sol 每輪復盤結果
```

## 復現

```bash
lms server start && lms load google/gemma-4-e4b
cd runs && python3 run_gemma.py ../prompt-v5.txt out.md 1
```
