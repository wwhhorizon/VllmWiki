# vllm-project/vllm#39056: vLLM 0.19 may lose tool calls for Qwen/Qwen3.5-35B-A3B-FP8 when XML tool_call is emitted inside <think>

| 字段 | 值 |
| --- | --- |
| Issue | [#39056](https://github.com/vllm-project/vllm/issues/39056) |
| 状态 | open |
| 标签 |  |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM 0.19 may lose tool calls for Qwen/Qwen3.5-35B-A3B-FP8 when XML tool_call is emitted inside <think>

### Issue 正文摘录

## Problem With vLLM 0.19, when serving the model: - `Qwen/Qwen3.5-35B-A3B-FP8` using: - `--reasoning-parser qwen3` - `--tool-call-parser qwen3_coder` non-streaming tool-call parsing can fail if the model emits XML tool-call markup inside the reasoning region, for example: ```text ... 204 ``` In this case, the model may have produced a valid tool call, but the OpenAI-compatible response ends up with populated `reasoning` and empty `tool_calls`. ## Observed model The issue was observed and reproduced with: - `Qwen/Qwen3.5-35B-A3B-FP8` It may also affect other Qwen3 / Qwen3.5 models that use the same parser combination, but the confirmed reproduction here is specifically on `Qwen/Qwen3.5-35B-A3B-FP8`. ## Why this happens The issue appears to come from the interaction between the reasoning parser and the tool parser: 1. `qwen3_reasoning_parser` extracts everything before ` ` into `reasoning`. 2. downstream tool parsing only inspects `content`. 3. if ` ... ` remains inside `reasoning`, it never reaches `qwen3_coder`. So the bug is not that vLLM makes Qwen3.5 generate tool calls inside ` `. The bug is that vLLM currently does not recover those tool calls when that output pattern occurs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vLLM 0.19 may lose tool calls for Qwen/Qwen3.5-35B-A3B-FP8 when XML tool_call is emitted inside <think> ## Problem With vLLM 0.19, when serving the model: - `Qwen/Qwen3.5-35B-A3B-FP8` using: - `--reasoning-parser qwen3`...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ` and empty `tool_calls`. ## Observed model The issue was observed and reproduced with: - `Qwen/Qwen3.5-35B-A3B-FP8` It may also affect other Qwen3 / Qwen3.5 models that use the same parser combination, but the confirme...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e the same parser combination, but the confirmed reproduction here is specifically on `Qwen/Qwen3.5-35B-A3B-FP8`. ## Why this happens The issue appears to come from the interaction between the reasoning parser and the t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vLLM 0.19 may lose tool calls for Qwen/Qwen3.5-35B-A3B-FP8 when XML tool_call is emitted inside <think> ## Problem With vLLM 0.19, when serving the model: - `Qwen/Qwen3.5-35B-A3B-FP8` using: - `--reasoning-parser qwen3`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: vllm-project/vllm/pull/39055 That patch promotes embedded XML tool-call blocks out of `reasoning` into `content` in `qwen3_reasoning_parser`, so the existing `qwen3_coder` tool parser can still parse them. ## Request Pl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
