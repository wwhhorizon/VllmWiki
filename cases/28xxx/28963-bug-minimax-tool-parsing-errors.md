# vllm-project/vllm#28963: [Bug]: MiniMax tool parsing errors

| 字段 | 值 |
| --- | --- |
| Issue | [#28963](https://github.com/vllm-project/vllm/issues/28963) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniMax tool parsing errors

### Issue 正文摘录

### Your current environment Running `vllm/vllm-openai:nightly-5bb1da5190b54aefb08478c6b1170f97722b8bdb` ### 🐛 Describe the bug While using MiniMax-M2 with the Kilo Code extension I hit a lot of the following errors: ``` │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] Error in chat completion stream generator. │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] Traceback (most recent call last): │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 1006, in chat_completion_stream_generator │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] delta_message = tool_parser.extract_tool_calls_streaming( │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/minimax_m2_tool_parser.py", line 613, in extract_tool │ │ (APIServer pid=1) ERROR 11-18 13:56:21 [serving_chat.py:1278] converted_value = self._convert_param_value( │ │ (APIServer pid=1) E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Error: 'list' object has no attribute 'lower' ``` Running the model with the following parameters: ``` non-default args: {'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'minimax_m2', 'trust_remo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: MiniMax tool parsing errors bug;stale ### Your current environment Running `vllm/vllm-openai:nightly-5bb1da5190b54aefb08478c6b1170f97722b8bdb` ### 🐛 Describe the bug While using MiniMax-M2 with the Kilo Code exte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
