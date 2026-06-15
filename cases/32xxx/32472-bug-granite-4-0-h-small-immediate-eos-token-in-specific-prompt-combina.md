# vllm-project/vllm#32472: [Bug]: Granite 4.0-H Small immediate EOS token in specific prompt combinations

| 字段 | 值 |
| --- | --- |
| Issue | [#32472](https://github.com/vllm-project/vllm/issues/32472) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Granite 4.0-H Small immediate EOS token in specific prompt combinations

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the `ibm-granite/granite-4.0-h-small` model I'm observing an issue where specific prompts cause the model to immediately generate an end token, resulting in an empty response. For example: - **Prompt (failing):** `"What are the key differences between machine learning and deep learning?"` -> **Result:** Empty string. - **Prompt (working):** `"What are the main differences between machine learning and deep learning?"` -> **Result:** Normal text generation. The only difference is changing the word "key" to "main". To reproduce the issue: 1. Run the provided reproduction script. 2. It will attempt to generate text for both prompts. 3. Observe that the first prompt yields an empty result. ### Reproduction Script ```python from vllm import LLM, SamplingParams MODEL_NAME = "ibm-granite/granite-4.0-h-small" # "key differences" produces empty output, "main differences" works prompts = [ "What are the key differences between machine learning and deep learning?", "What are the main differences between machine learning and deep learning?" ] sampling_params = SamplingParams( temperature=0, top_p=0.95, max_tokens=256, seed=42, )...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Granite 4.0-H Small immediate EOS token in specific prompt combinations bug;stale ### Your current environment ### 🐛 Describe the bug When running the `ibm-granite/granite-4.0-h-small` model I'm observing an issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Granite 4.0-H Small immediate EOS token in specific prompt combinations bug;stale ### Your current environment ### 🐛 Describe the bug When running the `ibm-granite/granite-4.0-h-small` model I'm observing an issu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: eration. The only difference is changing the word "key" to "main". To reproduce the issue: 1. Run the provided reproduction script. 2. It will attempt to generate text for both prompts. 3. Observe that the first prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nite 4.0-H Small immediate EOS token in specific prompt combinations bug;stale ### Your current environment ### 🐛 Describe the bug When running the `ibm-granite/granite-4.0-h-small` model I'm observing an issue where sp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 00 words. Include keywords: algorithms, neural networks, data, training, accuracy, models, features, layers, input, output, supervised, unsupervised, reinforcement. At the end of your response, please explicitly add a p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
