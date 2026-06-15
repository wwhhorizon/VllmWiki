# vllm-project/vllm#17476: [Bug]: Flash attention with sliding window

| 字段 | 值 |
| --- | --- |
| Issue | [#17476](https://github.com/vllm-project/vllm/issues/17476) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Flash attention with sliding window

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug `pytest -vs test_correctness_sliding_window.py::test_sliding_window_retrival\[1-5-bigcode/starcoder2-3b\]` starts to fail on H100 since https://github.com/vllm-project/vllm/pull/16998. This test can pass if I change it to `num_heads_kv=self.num_heads_q` like here https://github.com/heheda12345/vllm/tree/fa3_hack . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Flash attention with sliding window bug ### Your current environment N/A ### 🐛 Describe the bug `pytest -vs test_correctness_sliding_window.py::test_sliding_window_retrival\[1-5-bigcode/starcoder2-3b\]` starts to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _sliding_window_retrival\[1-5-bigcode/starcoder2-3b\]` starts to fail on H100 since https://github.com/vllm-project/vllm/pull/16998. This test can pass if I change it to `num_heads_kv=self.num_heads_q` like here https:/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: window bug ### Your current environment N/A ### 🐛 Describe the bug `pytest -vs test_correctness_sliding_window.py::test_sliding_window_retrival\[1-5-bigcode/starcoder2-3b\]` starts to fail on H100 since https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
