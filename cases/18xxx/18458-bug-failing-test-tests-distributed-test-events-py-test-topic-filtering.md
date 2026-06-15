# vllm-project/vllm#18458: [Bug] [Failing Test] :  tests/distributed/test_events.py::test_topic_filtering - AttributeError: 'KVEventsConfig' object has no attribute 'model_copy'

| 字段 | 值 |
| --- | --- |
| Issue | [#18458](https://github.com/vllm-project/vllm/issues/18458) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [Failing Test] :  tests/distributed/test_events.py::test_topic_filtering - AttributeError: 'KVEventsConfig' object has no attribute 'model_copy'

### Issue 正文摘录

### Your current environment Test failing on main branch. ### 🐛 Describe the bug Failing Test: FAILED tests/distributed/test_events.py::test_topic_filtering - AttributeError: 'KVEventsConfig' object has no attribute 'model_copy' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tributed/test_events.py::test_topic_filtering - AttributeError: 'KVEventsConfig' object has no attribute 'model_copy' bug ### Your current environment Test failing on main branch. ### 🐛 Describe the bug Failing Test: FA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: py' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug] [Failing Test] : tests/distributed/test_events.py::test_topic_filtering - AttributeError: 'KVEventsConfig' object has no attribute 'model_copy' bug ### Your current environment Test failing on main branch. ### 🐛 D...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
