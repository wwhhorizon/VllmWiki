# vllm-project/vllm#26797: [Bug]: Token id 5279552648203111001 is out of vocabulary

| 字段 | 值 |
| --- | --- |
| Issue | [#26797](https://github.com/vllm-project/vllm/issues/26797) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Token id 5279552648203111001 is out of vocabulary

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug File "/data/xuelei12/vllm/vllm/vllm/v1/engine/processor.py", line 365, in _validate_model_inputs self._validate_model_input(decoder_inputs, File "/data/xuelei12/vllm/vllm/vllm/v1/engine/processor.py", line 391, in _validate_model_input raise ValueError( ValueError: Token id 5279552648203111001 is out of vocabulary ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Token id 5279552648203111001 is out of vocabulary bug;stale ### Your current environment ### 🐛 Describe the bug File "/data/xuelei12/vllm/vllm/vllm/v1/engine/processor.py", line 365, in _validate_model_inputs sel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ary ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /xuelei12/vllm/vllm/vllm/v1/engine/processor.py", line 365, in _validate_model_inputs self._validate_model_input(decoder_inputs, File "/data/xuelei12/vllm/vllm/vllm/v1/engine/processor.py", line 391, in _validate_model_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
