# Commit 审查报告（近 20 条）

状态：completed
审查时间 UTC：2026-06-22
审查范围：89d35c4..e5e8124（20 条 commit）
审查方法：两个 explorer subagent 分批审查 + 主 agent 验证关键质疑点

## 审查维度

1. 偏离主线：是否属于 bitwise 专题主线（token/logprob/KV/tensor/metadata identity 确定性等价）
2. 强行分类：mechanism 分类是否自然，是否为了塞进机制页而牵强附会
3. 事实证据不足/主观臆断：结论是否有 issue/PR body、comments、changed files 等实际证据支撑
4. 冗余宽泛/非核心 insight：是否提供具体可操作的 insight，还是泛泛而谈

## 审查结论汇总

### 通过（13 条）

| Commit | PR/Issue | 判断 |
| --- | --- | --- |
| 7363ac0 | #41995 | 通过。Mamba metadata pointer 截断归入 kv_cache_identity 自然，证据充分 |
| 1ad2a48 | #43650 | 通过。MTP cache hit search 边界差异归入 prefix_cache_equivalence 自然 |
| 32ab45b | #42779 | 通过。padded inputs zeroing 归入 verification_contract 自然 |
| 3c4bede | #42903 | 通过。kv_offload gpu_block_ids dedup 归入 kv_cache_identity 自然 |
| 8c5dca9 | #42359 | 通过。ghost block race 归入 kv_cache_identity 自然，contested hypothesis 标注审慎 |
| 3a28437 | #39146 | 通过。recycled-block zeroing 证据链完整，insight 最丰富 |
| 99f362e | #42580 | 通过。关闭追踪准确，覆盖范围克制 |
| fbcc1df | 多条 | 通过。批量更新分类映射自然，open PR 处理谨慎 |
| d160b28 | 多条 | 通过。调研报告分类自然，反例纳入体现诚实性 |
| 2a59df3 | 多条 | 通过。kernel constraints bridge 页映射准确 |
| fdcd1c4 | #38991 | 通过。loading lifetime 收紧范围准确，scope 限定克制 |
| 5355231 | #44250/#42125 | 通过。adapter identity schema 分叉分析精确 |
| 89d35c4 | 队列重构 | 通过。辅助边界队列结构清晰，contested hypothesis 标注得当 |

### 通过附注（2 条）

| Commit | PR/Issue | 附注 |
| --- | --- | --- |
| df87564 | #44319 | 通过。证据链最完整。附注：归入 verification_contract 是从 bug 提炼验证启示角度，非机制本质归类，但 boundary 中已给出可操作的 verification contract |
| e5e8124 | #44115 | 通过（经主 agent 验证）。subagent 质疑偏离主线/强行分类，但验证后 deterministic_dispatch_reduction.md 范围明确包含 backend dispatch fallback，#44115 的 FlashInfer-to-Triton fallback 属于同类 dispatch fallback 模式（与 #39849/#42670 并列），分类合理 |

### 需要讨论（3 条）

| Commit | PR/Issue | 问题 |
| --- | --- | --- |
| 09854d4 | #44395 | 需要讨论（轻度）。partial wake_up KV lifecycle 本质是 use-after-free 内存安全 bug，归入 kv_cache_identity 的生命周期维度略牵强。但 boundary 用交叉措辞自承牵强，且标注无 linked fix。建议明确 functional correctness bug 与 bitwise 确定性等价的界限 |
| 6b1b5bd | 治理规则 | 需要讨论。commit message 是 taxonomy rules，但 diff 混入了 #42699/#38991 的具体 claim 内容，scope 与 message 不符。规则内容本身无误 |
| a2a82d7 + a51af82 | #38991 | 需要讨论。与 fdcd1c4 内容重复度高，三条 commit 围绕 #38991 反复迭代相同信息。作为连续迭代可理解，但最终 wiki 内容存在冗余 |

### 已排除的 subagent 质疑（2 条）

| 质疑 | 排除原因 |
| --- | --- |
| #39591（9eb3286）信息不足/需要修正 | subagent 因审查文件截断只看到 blocking_reason 部分。实际 ledger row 完整：target_evidence 引用 block_table.py/test_block_table.py/test_concurrent_prefill_determinism.py，promotion_reason 解释 move_row 整行复制与 slice+tail-zero 在 correctness 上等价。证据充分 |
| #42699/#40896（d160b28）fp32/BATCH_INVARIANT 断言无 comment 来源 | 验证 #42699 issue comments：用户 abinggo 确认 VLLM_BATCH_INVARIANT=1 和 fp32 都能让输出收敛。断言有据 |

## 跨条共性问题

1. 截断假象：审查时 diff 提取脚本截取每行前 300 字符，导致 subagent 误判多条 commit 内容截断。实际文件内容完整，此问题不存在
2. 功能性 bug 边界：#44115（capture 全零）和 #44395（use-after-free）处于 bitwise 专题边缘，建议在专题定义层面明确 functional correctness under specific path 与 bitwise/deterministic invariance 的界限
3. #38991 迭代冗余：fdcd1c4/a2a82d7/a51af82 三条 commit 围绕同一主题反复迭代，增量信息递减

## 建议行动

1. 对 #44395 的分类边界做专题定义层面澄清（轻度，不阻塞）
2. 对 #38991 的三条迭代 commit 考虑在后续轮次合并精简（不回溯修改历史）
3. 其余 17 条 commit 无需修正
