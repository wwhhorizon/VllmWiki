# vllm-project/vllm#23359: [Bug]: Qwen3 coder 480b awq fails to load on v0.10.1.1

| 字段 | 值 |
| --- | --- |
| Issue | [#23359](https://github.com/vllm-project/vllm/issues/23359) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 coder 480b awq fails to load on v0.10.1.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempt to load `koushd/Qwen3-Coder-480B-A35B-Instruct-AWQ` (I'm using -pp 2 and -tp 2 if that matters). The model will fail to load with a KeyError during Qwen3MoeModel.load_weights: `'layers.23.mlp.gate.weight'` However, the key `'layers.23.mlp.gate.qweight'` is present in the dictionary when observing in the debugger. I believe the regression was caused by this change: https://github.com/vllm-project/vllm/pull/20815 There seems to be some key remapping in that change that may have missed/broke something. I did not test v0.10.1. Last working build for v0.10.0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t may have missed/broke something. I did not test v0.10.1. Last working build for v0.10.0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 coder 480b awq fails to load on v0.10.1.1 bug ### Your current environment ### 🐛 Describe the bug Attempt to load `koushd/Qwen3-Coder-480B-A35B-Instruct-AWQ` (I'm using -pp 2 and -tp 2 if that matters). The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: present in the dictionary when observing in the debugger. I believe the regression was caused by this change: https://github.com/vllm-project/vllm/pull/20815 There seems to be some key remapping in that change that may...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
