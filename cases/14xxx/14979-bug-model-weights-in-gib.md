# vllm-project/vllm#14979: [Bug]: Model weights in GiB 

| 字段 | 值 |
| --- | --- |
| Issue | [#14979](https://github.com/vllm-project/vllm/issues/14979) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model weights in GiB 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I think there's a small error in the unit displayed by model_runner.py concerning the weight of a model. Given the calculation, I suggest replacing GB with GiB. What do you think? self.model_memory_usage = m.consumed_memory logger.info("Loading model weights took %.4f GB", self.model_memory_usage / **float(2**30))** Incorrect output : model_runner.py:1115] Loading model weights took 12.5523 **GB** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: concerning the weight of a model. Given the calculation, I suggest replacing GB with GiB. What do you think? self.model_memory_usage = m.consumed_memory logger.info("Loading model weights took %.4f GB", self.model_memor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment ### 🐛 Describe the bug Hello, I think there's a small error in the unit displayed by model_runner.py concerning the weight of a model. Given the calculation, I suggest replacing GB with GiB. What do...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Model weights in GiB bug ### Your current environment ### 🐛 Describe the bug Hello, I think there's a small error in the unit displayed by model_runner.py concerning the weight of a model. Given the calculation, I

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
