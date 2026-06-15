# vllm-project/vllm#36109: [Bug]: TypeError when rope_scaling.factor is null in model config

| 字段 | 值 |
| --- | --- |
| Issue | [#36109](https://github.com/vllm-project/vllm/issues/36109) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError when rope_scaling.factor is null in model config

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During wip to support `Ming-omni-flash-2.0` model in vLLM-Omni (https://github.com/vllm-project/vllm-omni/issues/1343), I found that there exists `TypeError` in deriving the max model length in `vllm/config/model.py::_get_and_verify_max_len` _This is more likely to be a corner case handling_ rather than a bug. **Root Cause:** Float get multiplied with None. In the [config.json](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0/blob/main/config.json) of the model, factor is marked as null: ```json "rope_scaling": { "factor": null, "type": "video_rope" }, ``` `_get_and_verify_max_len` crashes with a TypeError when loading a model whose `rope_scaling` config contains `"factor": null` (e.g., video_rope type). `dict.get("factor", default)` only falls back to the default when the key is absent, not when it is present with a null value. And thus `scaling_factor` becomes None and the subsequent `derived_max_model_len *= scaling_factor` raises a TypeError. **Fixes:** 1. (WIP) Connect with the model team discuss if they could update the factor to 1.0, as a default placeholder 2. Please see my linked PR, as a safety check and fallback...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TypeError when rope_scaling.factor is null in model config bug ### Your current environment ### 🐛 Describe the bug During wip to support `Ming-omni-flash-2.0` model in vLLM-Omni (https://github.com/vllm-project/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: a default placeholder 2. Please see my linked PR, as a safety check and fallback for null scaling factor cc @david6666666 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ould update the factor to 1.0, as a default placeholder 2. Please see my linked PR, as a safety check and fallback for null scaling factor cc @david6666666 ### Before submitting a new issue... - [x] Make sure you alread...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 66 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
