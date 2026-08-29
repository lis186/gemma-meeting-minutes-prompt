## 第二輪復盤結論

v2 有局部改善：不再把 `postg` 幻覺成 Postgre，三次也都保留了「最好抓隔天」的保守時程。但三項商務驗收仍是 **0/3 seed 完整通過**。

更關鍵的是：v2 加入的是「核對清單」，不是上一輪建議的「證據綁定」。模型在 thinking 階段已把 8/31 誤解成客戶簽約期限，最後只是確認這個錯誤日期「有被寫入」。證據見 [v2-run1.think.txt](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.think.txt:25)。

## 1–3. 錯誤、根因、三關與類型

| 排名 | 錯誤與根因 | (a) 會重犯？ | (b) 單次成本 | (c) 既有規則／工具 | 類型 |
|---:|---|---|---|---|---|
| 1 | **8/31 漏失或綁錯事件。** run1 寫成客戶簽約「合約截止日」；run2 雖寫「本方合約驗收日」，卻仍放在客戶簽約待辦的期限欄；run3 完全漏掉。根因是核對只檢查日期是否出現，沒有核對日期修飾的是哪個事件。[run1](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.md:17)、[run2](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run2.md:18)、[run3](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run3.md:12) | **3/3，通過** | **高**：把本方驗收期限變成客戶簽約承諾，會直接誤導排程及對外溝通。 | [Prompt v2](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:46) 已要求日期落入對應區段；run3 是**沒觸發**，run1/2 則暴露規則只驗覆蓋、不驗語意關係。 | **結構型** |
| 2 | **可疑公司名未揭露。** 三次都把「額度有限公司」當成確定名稱；run1 thinking 甚至擴寫成 “Equidote Co., Ltd.”。[thinking](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.think.txt:22) | **3/3，通過** | **高**：錯寫合約相對人有法務與客戶溝通風險。 | [第 6、49 行](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:6) 已要求不確定名稱列待確認，因此不是缺容器，而是模型錯把它判成「可以確定」，即**沒觸發**。 | **結構型**；真實名稱仍須人工確認 |
| 3 | **ASR 詞未正確處理。**「金牛」3/3 沒還原成「金流」；`postg` 3/3 被靜默刪除，沒有還原成「POS 機」，也沒有列待確認。v2 只是把 v1 的錯猜 Postgre 改成遺漏。[run1](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.md:4)、[run2](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run2.md:16)、[run3](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run3.md:4) | **3/3，通過** | **高**：遺漏關鍵系統角色，或把窗口名稱寫錯。 | [第 5–6 行](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:5) 已有校正及低信心退路，但兩者都沒觸發。 | **精準還原屬行為型**；「保留原詞並揭露」可做成結構型 |
| 4 | **推定逐字稿未明示的負責人。** 三次分別出現「未確認（團隊）」、「團隊」、「本方團隊」。[run1](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.md:16)、[run2](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run2.md:17)、[run3](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run3.md:17) | **3/3，通過** | **中高**：可能錯派責任。 | [第 28、47 行](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:28) 已明定無明示證據就寫「未確認」，所以純粹是**沒觸發**。 | **結構型** |
| 5 | **遺失「12 筆全部來自同一間門市」的範圍限定。** 三份都保留 12 筆，卻沒有明確保留「全部、同一間」。根因是摘要壓縮時只保存數字，沒有保存數字的範圍修飾詞。[三份摘要](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run1.md:3) | **3/3，通過** | **中**：會把單店資料問題誤讀成多店或系統性問題。 | [第 38 行](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:38) 已要求保留數量與影響範圍，屬**沒觸發**。 | **結構型** |
| 6 | **漏掉已確認的行動。** 三次均寫「決議：無」，但逐字稿已有「好，我去跟他們要」的明確行動確認。 | **3/3，通過** | **中**：團隊看不到已承諾的下一步。 | [決議規則](/Users/justinlee/HybridAIWorkshop/execerice/prompt-v2.txt:16) 本應辨識明確同意事項，屬**沒觸發**。 | **結構型** |
| 7 | **把核對過程輸出到成稿。** run3 加入 “Self-Correction Check”。[run3](/Users/justinlee/HybridAIWorkshop/execerice/runs/v2-run3.md:25) | **1/3，不通過 (a)** | 低至中 | Prompt 已禁止輸出核對過程。 | **行為型**；不值得單獨修 |

第 7 項沒有通過重犯關，因此不談修法。其他六項都通過三關，但依要求不各自堆疊規則。

## 4. 最後只留最高槓桿的一項

**用一條「逐字證據綁定」取代 v2 現有四條靜默 checklist；不要追加第五條規則。**

建議替換成：

> 輸出前，將每個日期、數字、範圍詞、負責人及疑似專名／技術詞對回逐字稿原句：只能保留原句直接支持的事件關係；無法確定正字時保留原詞並列入「待確認與風險」，不得省略、猜寫或移作別件事的資訊。核對過程不要輸出。

它比現在的「是否有日期、是否有名稱」更具體，同時能攔截：

- 8/31 被移作簽約期限
- `postg` 被刪除
- 「額度有限公司」被當成已確認正字
- 「同一間」被摘要掉
- 無證據的「團隊」負責人

對 4B 模型而言，這應該是**替換並縮短 prompt**，不是繼續加規則。

至於要求模型穩定把「金牛／postg」精準還原成「金流／POS 機」，在沒有領域詞表、音訊或答案提示且不能過度擬合的前提下，對這個 4B 模型不應視為可靠能力。務實驗收應改成：**能高信心還原最好；否則不得刪除或亂猜，必須原樣列入待確認，交人工一次確認。**

## 商務可用性判定

**不可。** 三個 seed 都未正確處理關鍵 ASR 詞與可疑公司名，且 8/31 沒有一次被正確、無歧義地綁定到本方專案驗收期限。