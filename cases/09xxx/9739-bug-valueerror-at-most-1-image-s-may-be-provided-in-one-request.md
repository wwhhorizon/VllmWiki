# vllm-project/vllm#9739: [Bug]: ValueError: At most 1 image(s) may be provided in one request.

| 字段 | 值 |
| --- | --- |
| Issue | [#9739](https://github.com/vllm-project/vllm/issues/9739) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: At most 1 image(s) may be provided in one request.

### Issue 正文摘录

### Your current environment vllm-openai/v06.3.1.post-1 ### Model Input Dumps a_request: None, prompt_adapter_request: None. 2024-10-27 23:04:39 INFO 10-27 09:04:39 engine.py:290] Added request chat-35d8d255cc6f44359126404d2bcefd72. 2024-10-27 23:04:40 INFO: 172.24.0.1:51444 - "POST /v1/chat/completions HTTP/1.1" 200 OK 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] Error in applying chat template from request 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] Traceback (most recent call last): 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 124, in create_chat_completion 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] conversation, mm_data_future = parse_chat_messages_futures( 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 529, in parse_chat_messages_futures 2024-10-27 23:04:47 ERROR 10-27 09:04:47 serving_chat.py:156] sub_messages = _parse_chat_mes...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug;stale ### Your current environment vllm-openai/v06.3.1.post-1 ### Model Input Dumps a_request: None, prompt_adapter_request: None. 2024-10-27 23:04:39 INFO 10-27 09:04:39 engine.py:290] Added request chat-35d8d255cc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ValueError: At most 1 image(s) may be provided in one request. bug;stale ### Your current environment vllm-openai/v06.3.1.post-1 ### Model Input Dumps a_request: None, prompt_adapter_request: None. 2024-10-27 23:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
