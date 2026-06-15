# vllm-project/vllm#17900: [Bug]: 调用mcp报错，但是使用阿里百炼上相同型号的模型就没问题

| 字段 | 值 |
| --- | --- |
| Issue | [#17900](https://github.com/vllm-project/vllm/issues/17900) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 调用mcp报错，但是使用阿里百炼上相同型号的模型就没问题

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 通过openwebui+mcpo调用工具，在本地使用阿里百炼的qwq-32b、qwen3-32b模型可以成功调用，但是在离线机器上使用vllm部署的qwq-32b、qwen3-32b模型就会报错，vllm==0.8.5，启动时已经配置--enable-auto-tool-choice --tool-call-parser hermes，错误日志如下： ERROR 05-09 04:25:03 [serving_chat.py:200] Error in preprocessing prompt inputs ERROR 05-09 04:25:03 [serving_chat.py:200] Traceback (most recent call last): ERROR 05-09 04:25:03 [serving_chat.py:200] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 183, in create_chat_completion ERROR 05-09 04:25:03 [serving_chat.py:200] ) = await self._preprocess_chat( ERROR 05-09 04:25:03 [serving_chat.py:200] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-09 04:25:03 [serving_chat.py:200] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_engine.py", line 403, in _preprocess_chat ERROR 05-09 04:25:03 [serving_chat.py:200] conversation, mm_data_future = parse_chat_messages_futures( ERROR 05-09 04:25:03 [serving_chat.py:200] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-09 04:25:03 [serving_chat.py:200] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1165, in parse_chat_messages_fut...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ### 🐛 Describe the bug 通过openwebui+mcpo调用工具，在本地使用阿里百炼的qwq-32b、qwen3-32b模型可以成功调用，但是在离线机器上使用vllm部署的qwq-32b、qwen3-32b模型就会报错，vllm==0.8.5，启动时已经配置--enable-auto-tool-choice --tool-call-parser hermes，错误日志如下： ERROR 05-09 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 调用mcp报错，但是使用阿里百炼上相同型号的模型就没问题 bug;stale ### Your current environment ### 🐛 Describe the bug 通过openwebui+mcpo调用工具，在本地使用阿里百炼的qwq-32b、qwen3-32b模型可以成功调用，但是在离线机器上使用vllm部署的qwq-32b、qwen3-32b模型就会报错，vllm==0.8.5，启动时已经配置--en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
