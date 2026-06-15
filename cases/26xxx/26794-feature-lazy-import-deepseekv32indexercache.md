# vllm-project/vllm#26794: [Feature]: Lazy import DeepseekV32IndexerCache

| 字段 | 值 |
| --- | --- |
| Issue | [#26794](https://github.com/vllm-project/vllm/issues/26794) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Lazy import DeepseekV32IndexerCache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I need to manually downgrade transformers to test some models, such as Qwen/Qwen2.5-Math-PRM-7B, which requires transformers==4.53.2 It's great if lazy import DeepseekV32IndexerCache, so I don't have to comment out these codes every time. https://github.com/vllm-project/vllm/blob/7e6edb14698c1a760272dd44363a288aeb07b571/vllm/v1/worker/gpu_model_runner.py#L50 https://github.com/vllm-project/vllm/blob/7e6edb14698c1a760272dd44363a288aeb07b571/vllm/v1/spec_decode/eagle.py#L23 https://github.com/vllm-project/vllm/blob/7e6edb14698c1a760272dd44363a288aeb07b571/vllm/v1/worker/gpu_model_runner.py#L4683-L4687 Reproduce code ``` pip install transformers==4.53.2 pytest -s -vvv tests/models/language/pooling/test_reward.py ``` cc @heheda12345 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Lazy import DeepseekV32IndexerCache feature request;stale ### 🚀 The feature, motivation and pitch I need to manually downgrade transformers to test some models, such as Qwen/Qwen2.5-Math-PRM-7B, which require...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Lazy import DeepseekV32IndexerCache feature request;stale ### 🚀 The feature, motivation and pitch I need to manually downgrade transformers to test some models, such as Qwen/Qwen2.5-Math-PRM-7B, which require...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vation and pitch I need to manually downgrade transformers to test some models, such as Qwen/Qwen2.5-Math-PRM-7B, which requires transformers==4.53.2 It's great if lazy import DeepseekV32IndexerCache, so I don't have to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 0272dd44363a288aeb07b571/vllm/v1/worker/gpu_model_runner.py#L4683-L4687 Reproduce code ``` pip install transformers==4.53.2 pytest -s -vvv tests/models/language/pooling/test_reward.py ``` cc @heheda12345 ### Alternative...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
