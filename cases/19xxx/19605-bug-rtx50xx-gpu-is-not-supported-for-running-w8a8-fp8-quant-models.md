# vllm-project/vllm#19605: [Bug]: RTX50xx GPU is not supported for running W8A8 FP8 quant models!

| 字段 | 值 |
| --- | --- |
| Issue | [#19605](https://github.com/vllm-project/vllm/issues/19605) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RTX50xx GPU is not supported for running W8A8 FP8 quant models!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On RTX5070 GPU, a W8A8 FP8 quant model is not supported, as `sm_120` architecture is not supported by vLLM yet. Running `vllm serve Llama-3.2-3B-Instruct-FP8-dynamic` got error: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RTX50xx GPU is not supported for running W8A8 FP8 quant models! bug ### Your current environment ### 🐛 Describe the bug On RTX5070 GPU, a W8A8 FP8 quant model is not supported, as `sm_120` architecture is not sup...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;kernel;op...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: RTX50xx GPU is not supported for running W8A8 FP8 quant models! bug ### Your current environment ### 🐛 Describe the bug On RTX5070 GPU, a W8A8 FP8 quant model is not supported, as `sm_120` architecture is not sup...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RTX50xx GPU is not supported for running W8A8 FP8 quant models! bug ### Your current environment ### 🐛 Describe the bug On RTX5070 GPU, a W8A8 FP8 quant model is not supported, as `sm_120` architecture is not sup...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
