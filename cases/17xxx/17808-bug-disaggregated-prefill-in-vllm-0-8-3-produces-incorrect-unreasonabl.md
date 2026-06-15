# vllm-project/vllm#17808: [Bug]: Disaggregated Prefill in vLLM 0.8.3 Produces Incorrect/Unreasonable Outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#17808](https://github.com/vllm-project/vllm/issues/17808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 | mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Disaggregated Prefill in vLLM 0.8.3 Produces Incorrect/Unreasonable Outputs

### Issue 正文摘录

### Your current environment # Issue: Disaggregated Prefill in vLLM 0.8.3 Produces Incorrect/Unreasonable Outputs ## Description When using vLLM 0.8.3 with **disaggregated prefill**, the generated text becomes semantically incorrect or repetitive compared to the standard (monolithic) prefill run. I’ve observed this issue on two different open-source models running on a single V100 GPU. ## Environment - **vLLM version:** 0.8.3 - **Hardware:** NVIDIA V100 (single GPU) - **Models tested:** 1. `meta-llama/Llama-2-7b-hf` 2. `DeepSeek-R1-Distill-Qwen-1.5B` ## Steps to Reproduce 1. Install vLLM 0.8.3 and load the chosen model on a V100 GPU. 2. Run standard (non-disaggregated) prefill + generate sampling for a set of prompts. 3. Run with the sample disaggregated prefill example (disaggregated_prefill.py) with the same prompts. The only thing I changed is adding `dtype=half` and model 4. Compare the outputs. ## Expected Behavior Outputs from the disaggregated prefill should **match** (or be at least semantically equivalent to) those from the standard prefill run for the same prompts and sampling settings. ## Actual Behavior The disaggregated prefill run yields outputs that are often irrele...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: thic) prefill run. I’ve observed this issue on two different open-source models running on a single V100 GPU. ## Environment - **vLLM version:** 0.8.3 - **Hardware:** NVIDIA V100 (single GPU) - **Models tested:** 1. `me...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pen-source models running on a single V100 GPU. ## Environment - **vLLM version:** 0.8.3 - **Hardware:** NVIDIA V100 (single GPU) - **Models tested:** 1. `meta-llama/Llama-2-7b-hf` 2. `DeepSeek-R1-Distill-Qwen-1.5B` ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: | `What are you thinking? What are you feeling?` `Relationship with You` | ### 2. DeepSeek-R1-Distill-Qwen-1.5B | Prompt | Standard Prefill Output | Disaggregated Prefill Output
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: llama/Llama-2-7b-hf` 2. `DeepSeek-R1-Distill-Qwen-1.5B` ## Steps to Reproduce 1. Install vLLM 0.8.3 and load the chosen model on a V100 GPU. 2. Run standard (non-disaggregated) prefill + generate sampling for a set of p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Disaggregated Prefill in vLLM 0.8.3 Produces Incorrect/Unreasonable Outputs bug;stale ### Your current environment # Issue: Disaggregated Prefill in vLLM 0.8.3 Produces Incorrect/Unreasonable Outputs ## Descripti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
