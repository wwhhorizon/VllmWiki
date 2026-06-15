# vllm-project/vllm#39066: [Bug]: Gemma 4 MoE (26B-A4B-it) crashes at startup — AssertionError: top_k is None in MoEMixin.recursive_replace

| 字段 | 值 |
| --- | --- |
| Issue | [#39066](https://github.com/vllm-project/vllm/issues/39066) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;quantization;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 MoE (26B-A4B-it) crashes at startup — AssertionError: top_k is None in MoEMixin.recursive_replace

### Issue 正文摘录

## Describe the bug Loading `google/gemma-4-26B-A4B-it` (or any Gemma 4 MoE variant) with the Transformers modeling backend raises an `AssertionError` immediately during model initialization, before any inference occurs. ``` File ".../vllm/model_executor/models/transformers/moe.py", line 198, in recursive_replace assert top_k is not None AssertionError ``` ### Root Cause `MoEMixin.recursive_replace` resolves the top-k value via: ```python top_k = getattr_iter(text_config, ["num_experts_per_tok", "top_k"], None) assert top_k is not None ``` `Gemma4TextConfig` stores this value under the attribute name **`top_k_experts`** — not `num_experts_per_tok` or `top_k`. The lookup returns `None` and the assert fires. ```python # transformers/models/gemma4/configuration_gemma4.py @dataclass class Gemma4TextConfig: num_experts: int | None = None top_k_experts: int | None = None # 1` in CUDA communicator) or #39000 (MXFP4 quantization crash). - The fix is a one-line addition to the attribute lookup list and is safe for all other MoE models (the new entry is only reached if the first two attributes are absent).

## 现有链接修复摘要

#39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | #41401 [Bugfix] Fix RoutedExpertsCapturer for Gemma 4 MoE (top_k_experts)

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Gemma 4 MoE (26B-A4B-it) crashes at startup — AssertionError: top_k is None in MoEMixin.recursive_replace ## Describe the bug Loading `google/gemma-4-26B-A4B-it` (or any Gemma 4 MoE variant) with the Transformers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: p_k_experts: int | None = None # 1` in CUDA communicator) or #39000 (MXFP4 quantization crash). - The fix is a one-line addition to the attribute lookup list and is safe for all other MoE models (the new entry is only r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 MoE (26B-A4B-it) crashes at startup — AssertionError: top_k is None in MoEMixin.recursive_replace ## Describe the bug Loading `google/gemma-4-26B-A4B-it` (or any Gemma 4 MoE variant) with the Transformers...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -26B-A4B-it` (or any Gemma 4 MoE variant) with the Transformers modeling backend raises an `AssertionError` immediately during model initialization, before any inference occurs. ``` File ".../vllm/model_executor/models/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oe;quantization;sampling_logits cuda;moe;quantization;sampling crash env_dependency #39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | #41401 [Bugfix] Fix RoutedExpertsCapture...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39067](https://github.com/vllm-project/vllm/pull/39067) | closes_keyword | 0.95 | [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | Fixes #39066** \`google/gemma-4-26B-A4B-it\` crashes at startup because \`Gemma4TextConfig\` stores the top-k expert count under \`top_k_experts\`, while \`MoEMixin.recursive_repl |
| [#41401](https://github.com/vllm-project/vllm/pull/41401) | mentioned | 0.6 | [Bugfix] Fix RoutedExpertsCapturer for Gemma 4 MoE (top_k_experts) | in `RoutedExpertsReader.attach_buffer`) ## Context - Related issue: #39066 (same root cause — Gemma 4 uses `top_k_experts` instead of `num_experts_per_tok`) - PR #39067 fixes the… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
