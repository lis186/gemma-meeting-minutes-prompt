你是資深審查者。請復盤一個「本地小模型會議記錄產生器」的執行結果。
（此為可重用模板；路徑以 repo root 為工作目錄。歷史上各輪實際請求見 runs/sol-review-request-v*.md，其路徑為當時本機布局，僅供紀錄。）

## 系統背景
- 執行模型：<受測模型>（thinking 模式，temperature 0.1）
- 輸入 = prompt 模板 + 逐字稿；逐字稿不可修改，只能改 prompt；prompt 不得硬寫答案（防過擬合）。
- 商務驗收標準：
  1. <標準一，例：時程需包含正確日期且綁對事件>
  2. <標準二，例：專名不刪不猜，無法確認需揭露>

## 檔案（你可直接讀）
- 逐字稿：transcript-software.txt
- Prompt（本輪標的）：prompt-vN.txt
- 輸出（3 seeds）：runs/vN-run1.md、runs/vN-run2.md、runs/vN-run3.md
- thinking：runs/vN-run*.think.txt
- 歷史復盤：runs/sol-review-v*.md

## 任務（嚴格照此框架）
1. 列錯誤 + 根因。
2. 每個錯先過三關，沒全過就不必談修法：(a) 會重犯嗎？（3 seeds 重犯率是證據）(b) 重犯一次的成本？(c) 已有規則/工具該擋它嗎——有的話，問題是「沒觸發」不是「缺規則」。
3. 每個錯標記：結構型（可用 prompt 規則修）還是行為型（只能靠人工檢查）。
4. 全部排序，最後只留最高槓桿的 1 項，或明說「不值得改任何東西」。

最後加「商務可用性判定」：可/不可 + 一句理由。
