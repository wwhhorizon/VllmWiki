# vllm-project/vllm#16594: [Bug]: examples/offline_inference/chat_with_tools.py JSONDecodeError

| 字段 | 值 |
| --- | --- |
| Issue | [#16594](https://github.com/vllm-project/vllm/issues/16594) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: examples/offline_inference/chat_with_tools.py JSONDecodeError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When run `python examples/offline_inference/chat_with_tools.py` It raised an error. So I print output and found that it has prefix '[TOOL_CALLS]' ``` Traceback (most recent call last): File "/root/vllm/examples/offline_inference/chat_with_tools.py", line 123, in tool_calls = json.loads(output) ^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/json/__init__.py", line 346, in loads return _default_decoder.decode(s) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/json/decoder.py", line 337, in decode obj, end = self.raw_decode(s, idx=_w(s, 0).end()) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/json/decoder.py", line 355, in raw_decode raise JSONDecodeError("Expecting value", s, err.value) from None json.decoder.JSONDecodeError: Expecting value: line 1 column 2 (char 1) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: examples/offline_inference/chat_with_tools.py JSONDecodeError bug;stale ### Your current environment ### 🐛 Describe the bug When run `python examples/offline_inference/chat_with_tools.py` It raised an error. So I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
