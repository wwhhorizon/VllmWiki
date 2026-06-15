# vllm-project/vllm#20054: [Bug]: Accuracy Discrepancy in Qwen-7B-Chat Evaluation: vLLM Logprobs Differ from SGLANG, Impacting Performance

| 字段 | 值 |
| --- | --- |
| Issue | [#20054](https://github.com/vllm-project/vllm/issues/20054) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Accuracy Discrepancy in Qwen-7B-Chat Evaluation: vLLM Logprobs Differ from SGLANG, Impacting Performance

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We attempted to reproduce the evaluation results of Qwen-7B-Chat using different backends (SGLANG, vLLM, HuggingFace), and observed consistent accuracy drops when using vLLM compared to SGLANG across multiple test sets. To investigate, we compared logprobs under identical generation configurations and found significant differences between the two backends. ## Key Observations Accuracy Gap: vLLM shows lower accuracy than SGLANG on test sets (gsm8k, mmlu, bbh, etc). Logprobs Mismatch: Even with the same input and generation configs, logprobs returned by vLLM and SGLANG differ, as verified by single-request comparisons. ## Questions for the Community 1. How should we interpret the logprobs differences between SGLANG and vLLM? This article can provide some explanations [https://github.com/NVIDIA-NeMo/RL/blob/57eb44f32d047f5bb05b778d5d7ad5b2bc01b440/docs/adding-new-models.md#understand-discrepancies-between-backends](https://github.com/NVIDIA-NeMo/RL/blob/57eb44f32d047f5bb05b778d5d7ad5b2bc01b440/docs/adding-new-models.md#understand-discrepancies-between-backends) 2. What is the potential impact of these logprobs differences on the fin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Accuracy Discrepancy in Qwen-7B-Chat Evaluation: vLLM Logprobs Differ from SGLANG, Impacting Performance bug;stale ### Your current environment ### 🐛 Describe the bug We attempted to reproduce the evaluation resu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 5bb05b778d5d7ad5b2bc01b440/docs/adding-new-models.md#understand-discrepancies-between-backends](https://github.com/NVIDIA-NeMo/RL/blob/57eb44f32d047f5bb05b778d5d7ad5b2bc01b440/docs/adding-new-models.md#understand-discre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Accuracy Discrepancy in Qwen-7B-Chat Evaluation: vLLM Logprobs Differ from SGLANG, Impacting Performance bug;stale ### Your current environment ### 🐛 Describe the bug We attempted to reproduce the evaluation resu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: Accuracy Discrepancy in Qwen-7B-Chat Evaluation: vLLM Logprobs Differ from SGLANG, Impacting Performance bug;stale ### Your current environment ### 🐛 Describe the bug We attempted to reproduce the evaluation resu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tions Accuracy Gap: vLLM shows lower accuracy than SGLANG on test sets (gsm8k, mmlu, bbh, etc). Logprobs Mismatch: Even with the same input and generation configs, logprobs returned by vLLM and SGLANG differ, as verifie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
