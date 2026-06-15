# vllm-project/vllm#28317: [Bug]: Prefix caching leads to different outputs for Hermes-3-Llama-3.1-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#28317](https://github.com/vllm-project/vllm/issues/28317) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching leads to different outputs for Hermes-3-Llama-3.1-8B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With the NousResearch/Hermes-3-Llama-3.1-8B model, I've found that `enable_prefix_caching` causes the output to change for certain prompts when the temperature has been set to 0. This contradicts the assumption in https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/prefix_caching.py, where it's expected that output will be invariant of prefix caching. Curiously, prefix_caching.py works as written for me using the `opt-125m` model, but the third output produces different completions when I modify the script to use `model="NousResearch/Hermes-3-Llama-3.1-8B"` in both constructors (and explicitly set `enable_prefix_caching=False` in the first): * Without caching: ` Paris. Paris is the largest city in France and is located in the north-central` * With caching: ` Paris. Paris is a beautiful city with many famous landmarks such as the Eiff` I also created a simplified test script based on prefix_caching.py, but using a smaller prefix and more easily comparable output, which also reproduces this in two of the four test cases for me: When I run this in the environment above, the first two outputs have a mismatch: ``...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: Prefix caching leads to different outputs for Hermes-3-Llama-3.1-8B bug;stale ### Your current environment ### 🐛 Describe the bug With the NousResearch/Hermes-3-Llama-3.1-8B model, I've found that `enable_prefix_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: del="NousResearch/Hermes-3-Llama-3.1-8B"` in both constructors (and explicitly set `enable_prefix_caching=False` in the first): * Without caching: ` Paris. Paris is the largest city in France and is located in the north...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ## Your current environment ### 🐛 Describe the bug With the NousResearch/Hermes-3-Llama-3.1-8B model, I've found that `enable_prefix_caching` causes the output to change for certain prompts when the temperature has been...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Prefix caching leads to different outputs for Hermes-3-Llama-3.1-8B bug;stale ### Your current environment ### 🐛 Describe the bug With the NousResearch/Hermes-3-Llama-3.1-8B model, I've found that `enable_prefix_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Prefix caching leads to different outputs for Hermes-3-Llama-3.1-8B bug;stale ### Your current environment ### 🐛 Describe the bug With the NousResearch/Hermes-3-Llama-3.1-8B model, I've found that `enable_prefix_caching...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
