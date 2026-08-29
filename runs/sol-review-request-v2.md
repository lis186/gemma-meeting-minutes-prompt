延續上一輪復盤（你判定 prompt-v1 不可商用，最高槓桿修法=「輸出前靜默證據核對」）。fable 已據此寫出 prompt-v2 並重跑 3 個 seed。請對 v2 的執行結果做第二輪復盤。

## 背景（同上一輪）
- 執行模型：gemma-4-e4b（4B，本地，thinking 模式，temperature 0.1）；逐字稿不可改，只能改 prompt。
- 商務驗收標準：
  1. 時程需包含正確的日期（逐字稿：「我們的合約是 8 月 31 號要驗收」——這是本方專案驗收期限，不是客戶簽約期限）
  2. 專有名詞正確（金牛→金流、postg→POS 機），prompt 不能過度擬合（不能把答案硬寫進 prompt）
  3. 無法確認的部分（可疑公司名如「額度有限公司」）需明確列出

## 檔案
- 逐字稿：execerice/transcript-software.txt
- Prompt v2（本輪標的）：execerice/prompt-v2.txt；v1 對照：execerice/prompt-v1.txt
- v2 輸出：execerice/runs/v2-run1.md、v2-run2.md、v2-run3.md（v1 輸出仍在 runs/ 可對照）
- v2 run1 thinking：execerice/runs/v2-run1.think.txt
- 你上一輪的復盤：execerice/runs/sol-review-v1.md

## 任務（嚴格照此框架）
1. 列錯誤 + 根因。
2. 每個錯先過三關，沒全過就不必談修法：(a) 會重犯嗎？(b) 重犯一次的成本？(c) 已有規則/工具該擋它嗎——有的話，問題是「沒觸發」不是「缺規則」。
3. 每個錯標記：結構型（可用 prompt 規則修）還是行為型（只能靠人工檢查）。
4. 全部排序，最後只留最高槓桿的 1 項，或明說「不值得改任何東西」。

注意：4B 模型的 prompt 遵循能力有限，規則越多稀釋越嚴重；你提的修法要考慮這個限制。若你認為某驗收標準（如 ASR 專名還原）在「不過度擬合」前提下對 4B 模型實際上不可達，請明說並提出務實替代（例如：改由「待確認清單」揭露而非強行還原）。

最後加「商務可用性判定」：可/不可 + 一句理由。
