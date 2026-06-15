# vllm-project/vllm#30721: [Bug]: AttributeError: 'Qwen3VLConfig' object has no attribute 'intermediate_size'

| 字段 | 值 |
| --- | --- |
| Issue | [#30721](https://github.com/vllm-project/vllm/issues/30721) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen3VLConfig' object has no attribute 'intermediate_size'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes with the following error with the docke nightly build: ``` AttributeError: 'Qwen3VLConfig' object has no attribute 'intermediate_size' ``` It seems that this is caused by some commit in: `vllm/vllm-openai:nightly-58d5b3f51455706bf4f1f2360a0feb83d161147e`. The previous nightly works fine: `vllm/vllm-openai:nightly-17eb25e3271f8f22a0d8920a8115158495827cba` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: AttributeError: 'Qwen3VLConfig' object has no attribute 'intermediate_size' bug;stale ### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes with the following error with the docke nightly build: ``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he bug Qwen3-VL crashes with the following error with the docke nightly build: ``` AttributeError: 'Qwen3VLConfig' object has no attribute 'intermediate_size' ``` It seems that this is caused by some commit in: `vllm/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ba` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: teError: 'Qwen3VLConfig' object has no attribute 'intermediate_size' bug;stale ### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes with the following error with the docke nightly build: ``` AttributeErr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
