# 无限迭代协议

状态：active protocol。  
目标：让 VllmWiki 每一轮都能变得更好，同时不丢 source traceability。

## 循环

每一轮迭代都按同一套循环执行：

1. 为当前 lane 定义 wiki task contract。
2. 冻结 source snapshot。
3. 重建 candidate wiki 页面和生成索引。
4. 生成严格 review queue 和 candidate ledger。
5. 分派子代理做 source reading、link audit、mechanism curation、false-positive detection 和 quality gate。
6. 阅读最高价值队列项的原始 issue/PR 正文。
7. 对候选 claim 执行 promote、defer 或 reject。
8. 运行 validation 和 link gate。
9. 记录变化、blocker 和下一轮优先队列。

这对应 KernelWiki 式的知识炼化循环：每个 wiki claim 都必须通过 source 与 validation criteria。

## 当前任务契约

Task name：`bitwise-determinism-vllmwiki`。

目标：构建一个 source-backed wiki，覆盖 vLLM bitwise、deterministic decoding、batch-invariance、KV identity、quantization drift 和 deterministic dispatch 机制。

正确性要求：

- 每个 promoted measure 都必须指向 issue/PR 证据。
- 每个依赖评论的结论都必须说明本地缺失评论正文。
- 每个 curated mechanism 都要区分 observation、root mechanism、fix、verification 和 boundary。
- 宽泛关键词命中在源正文阅读前必须保持 candidate。

验证命令：

```powershell
python VllmWiki\scripts\validate_vllmwiki.py
```

迭代命令：

```powershell
python VllmWiki\scripts\run_vllmwiki_iteration.py
```

Promotion criteria：只有当 source evidence 支持 divergence path、fix mechanism、verification contract 和 scope boundary 时，claim 才能称为 curated；否则保持 `candidate`、`reviewed` 或 `blocked`。

## 迭代 Lane

| Lane | 目标 | 当前状态 |
| --- | --- | --- |
| Source ingestion | 补齐评论、PR detail、changed files 和 merge evidence | pending |
| Bitwise determinism | 优先 curated 精确/数值等价机制 | active |
| KV cache identity | 拆分 cache-key、block lifecycle、offload、metadata cleanup 子族 | active |
| Quantization semantics | Curate FP8/FP4/NVFP4/MXFP4/GPTQ dtype/scale/layout 机制 | active |
| Backend routing | Curate capability guard、fallback、backend selection、hardware-specific dispatch | next |
| Verification | Curate test/benchmark/equality-contract lesson | active |
| Noise reduction | 审计 false link 与过宽关键词命中 | continuous |

## 每轮 Review Budget

聚焦 bitwise 这类 family 时：

- 至少阅读 10 个 top queue issue。
- 至少阅读 10 个 linked PR body。
- 新增或更新至少 1 个 mechanism page。
- 新增至少 5 条具体优化手段，或标记 blocked 原因。
- 运行 link check 和 queue generation。
- 记录子代理输出：reviewed case list、promoted mechanism list、blocked source list、false-positive rule changes。

宽泛 family 的顺序：

1. 先创建 strict queue。
2. 再拆成 mechanism page。
3. 最后写 curated summary。

## 提升标准

candidate optimization measure 可进入 `reviewed` 的条件：

- 原始 issue body 已读。
- 有 PR 时，linked PR body 已读。
- 源文本支持该 mechanism。
- 页面说明 verification method，或明确标记缺失。

reviewed measure 可进入 `curated` 的条件：

- root cause 与 fix 有 source evidence 支持。
- scope 与 boundary 已说明。
- test、benchmark 或 reproduction evidence 已说明。
- comment/PR-detail 缺口已关闭，或明确为非阻塞。

## 子代理 Lane

| Lane | 任务 | 输出 |
| --- | --- | --- |
| Source reader | 阅读 bounded queue 的原始 issue 与 PR body | reviewed facts、evidence snippets、blocked missing comments/details |
| PR-link auditor | 审计 `issue_pr_links.csv` 与页面 linked PR | true fix / weak mention / false positive 标签 |
| Mechanism curator | 把重复证据转成可复用 wiki mechanism | 更新 curated pages 和 optimization measures |
| False-positive auditor | 找 noisy keyword/pattern hit | rule updates、removed candidates、bad match examples |
| Quality runner | 验证覆盖率、链接、queue count、status label | gate report 和 next risks |

子代理不能直接 promote claim；它们提出建议，主线程集成并保持文件一致。

## 当前迭代日志

### Iteration 1：Candidate Skeleton

- 从 raw issue/PR 数据构建 source-backed VllmWiki。
- 生成全部 issue page、domain page、pattern page、index、evidence ledger 和 manifest。
- 建立 quality gate 与 candidate/reviewed/curated 状态。

### Iteration 2：Bitwise First Pass

- 将 bitwise determinism 提升为优先焦点。
- 创建 curated bitwise summary 和六个 mechanism page。
- 增加 684 条 strict bitwise review queue。
- 增加 prefix-cache equivalence、batch invariance、KV identity、quant dtype semantics、deterministic dispatch/reduction、verification contracts 等具体措施。

### Iteration 3：KernelWiki 对齐

- 阅读真实 KernelWiki 源仓库。
- 增加 KernelWiki 炼化方式笔记、schemas/tags/aliases/version-claims、bitwise ledger。
- 增加 `query/get/grep/validate` 工具。
- 将 validation 纳入迭代 gate。

### Iteration 4：中文化

- 生成器模板切换为中文。
- 手写与 curated 层切换为中文。
- 原始 issue/PR 标题、正文摘录和上游链接保持原文，以保留证据准确性。
