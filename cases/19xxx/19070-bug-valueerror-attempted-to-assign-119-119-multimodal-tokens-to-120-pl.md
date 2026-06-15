# vllm-project/vllm#19070: [Bug]: ValueError: Attempted to assign 119 = 119 multimodal tokens to 120 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#19070](https://github.com/vllm-project/vllm/issues/19070) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 41; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Attempted to assign 119 = 119 multimodal tokens to 120 placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug qwen2-audio; A100 first request can get correct answer,then raise this error and shutting down service `INFO 06-03 17:19:10 [engine.py:310] Added request chatcmpl-dbc1b9d1833145889ac9303cf53b6ca7. ERROR 06-03 17:19:10 [serving_chat.py:885] Error in chat completion stream generator. ERROR 06-03 17:19:10 [serving_chat.py:885] Traceback (most recent call last): ERROR 06-03 17:19:10 [serving_chat.py:885] File "/data/miniconda3/envs/ljj_opencompass/lib/python3.10/site-packages/vllm/entrypoints/openai/serving_chat.py", line 487, in chat_completion_stream_generator ERROR 06-03 17:19:10 [serving_chat.py:885] async for res in result_generator: ERROR 06-03 17:19:10 [serving_chat.py:885] File "/data/miniconda3/envs/ljj_opencompass/lib/python3.10/site-packages/vllm/engine/multiprocessing/client.py", line 667, in _process_request ERROR 06-03 17:19:10 [serving_chat.py:885] raise request_output ERROR 06-03 17:19:10 [serving_chat.py:885] vllm.engine.multiprocessing.MQEngineDeadError: Engine loop is not running. Inspect the stacktrace to find the original error: ValueError('Attempted to assign 119 = 119 multimodal tokens to 120 placeholders'). ER...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ValueError: Attempted to assign 119 = 119 multimodal tokens to 120 placeholders bug;stale ### Your current environment ### 🐛 Describe the bug qwen2-audio; A100 first request can get correct answer,then raise this...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Attempted to assign 119 = 119 multimodal tokens to 120 placeholders bug;stale ### Your current environment ### 🐛 Describe the bug qwen2-audio; A100 first request can get correct answer,then raise this error and shutting...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le ### Your current environment ### 🐛 Describe the bug qwen2-audio; A100 first request can get correct answer,then raise this error and shutting down service `INFO 06-03 17:19:10 [engine.py:310] Added request chatcmpl-d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
