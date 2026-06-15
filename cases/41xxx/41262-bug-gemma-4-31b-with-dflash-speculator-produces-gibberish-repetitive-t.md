# vllm-project/vllm#41262: [Bug]: Gemma-4 31B with DFlash speculator produces gibberish/repetitive token loop

| 字段 | 值 |
| --- | --- |
| Issue | [#41262](https://github.com/vllm-project/vllm/issues/41262) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-4 31B with DFlash speculator produces gibberish/repetitive token loop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Model `RedHatAI/gemma-4-31B-it-speculator.dflash` (resolves to `google/gemma-4-31B-it` with a DFlash speculative decoding head) ### How to reproduce ```bash vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash -tp 2 # In a separate terminal: vllm chat ``` Then send any message, e.g. "Hello". ### Description When serving `RedHatAI/gemma-4-31B-it-speculator.dflash` with tensor parallelism 2, responses frequently (but not always) start coherent and then degrade into repetitive token loops / gibberish. Short, simple prompts seem most affected. ### Example output ``` > Hello Hello! How can I help1 ay1/saj dey-//-o-1sCj?C-o la laay1sCj?C-o laCj?C-oenCjC-oCjC-oCjC-o CjC-1sCj?C-1sCj1sCj1sCj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1Cj1C1y1y/C/C/C/C/C/C /C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C /C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C/C ... ``` The output starts with a coherent fragment ("Hello! How can I help") then immediately corrupts into garbled characters and eventually collapses into an infinite `/C` repetition loop until max tokens or man...

## 现有链接修复摘要

#41657 Fix KV cache tensor sharing across block sizes

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: serving `RedHatAI/gemma-4-31B-it-speculator.dflash` with tensor parallelism 2, responses frequently (but not always) start coherent and then degrade into repetitive token loops / gibberish. Short, simple prompts seem mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma-4 31B with DFlash speculator produces gibberish/repetitive token loop bug ### Your current environment ### 🐛 Describe the bug ### Model `RedHatAI/gemma-4-31B-it-speculator.dflash` (resolves to `google/gemma...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: gle/gemma-4-31B-it` with a DFlash speculative decoding head) ### How to reproduce ```bash vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash -tp 2 # In a separate terminal: vllm chat ``` Then send any message, e.g. "H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: up: **no issue** — outputs are coherent. This suggests the problem is specific to the DFlash speculator, not Gemma-4 31B or the speculative decoding pipeline in general. - **`z-lab/Qwen3.5-27B-DFlash`** with the same se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: it-speculator.dflash` (resolves to `google/gemma-4-31B-it` with a DFlash speculative decoding head) ### How to reproduce ```bash vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash -tp 2 # In a separate terminal: vllm...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41657](https://github.com/vllm-project/vllm/pull/41657) | closes_keyword | 0.95 | Fix KV cache tensor sharing across block sizes | Fixes #41262. This PR fixes KV cache corruption in hybrid KV cache layouts where KV cache groups with different `block_size` values could share the same raw `KVCacheTensor`. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
