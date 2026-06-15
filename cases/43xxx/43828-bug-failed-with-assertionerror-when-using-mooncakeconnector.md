# vllm-project/vllm#43828: [Bug]:  failed with AssertionError when using mooncakeconnector

| 字段 | 值 |
| --- | --- |
| Issue | [#43828](https://github.com/vllm-project/vllm/issues/43828) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  failed with AssertionError when using mooncakeconnector

### Issue 正文摘录

### Your current environment v0.21.0 ### 🐛 Describe the bug (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] AsyncLLM output_handler failed. (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] Traceback (most recent call last): (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 697, in output_handler (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] logger_ref[0].record( (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] ~~~~~~~~~~~~~~~~~~~~^ (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/metrics/loggers.py", line 1342, in record (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] stat_logger.record( (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] ~~~~~~~~~~~~~~~~~~^ (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/metrics/loggers.py", line 1104, in record (APIServer pid=52555) ERROR 05-27 13:26:09 [async_llm.py:704] self.kv_connector_prom_observe( (APIServer pid=52555) ERROR 05-27 13:26:...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
