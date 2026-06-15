# vllm-project/vllm#25821: [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

| 字段 | 值 |
| --- | --- |
| Issue | [#25821](https://github.com/vllm-project/vllm/issues/25821) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] AsyncLLM output_handler failed. (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] Traceback (most recent call last): (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] File "/opt/conda/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 457, in output_handler (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] processed_outputs = output_processor.process_outputs( (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] File "/opt/conda/lib/python3.10/site-packages/vllm/v1/engine/output_processor.py", line 435, in process_outputs (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] stop_string = req_state.detokenizer.update( (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] File "/opt/conda/lib/python3.10/site-packages/vllm/v1/engine/detokenizer.py", line 118, in update (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] self.output_text += self.decode_next(new_token_id) (APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] File "/opt/conda/lib/python3.10/site-packages/vllm/v1/engine...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nt 'id': StreamInput must be either an integer or a list of integers bug;stale ### Your current environment ### 🐛 Describe the bug APIServer pid=10005) ERROR 09-28 05:39:47 [async_llm.py:480] AsyncLLM output_handler fai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
