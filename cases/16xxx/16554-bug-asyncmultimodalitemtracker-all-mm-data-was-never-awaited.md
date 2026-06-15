# vllm-project/vllm#16554: [Bug]: 'AsyncMultiModalItemTracker.all_mm_data' was never awaited

| 字段 | 值 |
| --- | --- |
| Issue | [#16554](https://github.com/vllm-project/vllm/issues/16554) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 'AsyncMultiModalItemTracker.all_mm_data' was never awaited

### Issue 正文摘录

### Your current environment python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer-mode mistral --config-format mistral --load-format mistral --tool-call-parser mistral --chat-template examples/tool_chat_template_mistral_parallel.jinja --enable-auto-tool-choice --limit_mm_per_prompt 'image=10' --gpu-memory-utilization 0.95 --api-key [retracted] --max-model-len 8128 --served-model-name fmax --guided-decoding-backend auto --tensor-parallel-size 2 ### 🐛 Describe the bug Doing a request would raise the following error: ```python INFO: Application startup complete. WARNING 04-13 06:57:15 [protocol.py:70] The following fields were present in the request but ignored: {'strict'} INFO 04-13 06:57:15 [chat_utils.py:396] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. WARNING 04-13 06:57:15 [chat_utils.py:317] 'add_generation_prompt' is not supported for mistral tokenizer, so it will be ignored. WARNING 04-13 06:57:15 [chat_utils.py:321] 'continue_final_message' is not supported for mistral tokenizer, so it will be ignored. ERROR 04-13...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 'AsyncMultiModalItemTracker.all_mm_data' was never awaited bug;stale ### Your current environment python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s.openai.api_server --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer-mode mistral --config-format mistral --load-format mistral --tool-call-parser mistral --chat-template exam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 'AsyncMultiModalItemTracker.all_mm_data' was never awaited bug;stale ### Your current environment python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tracted] --max-model-len 8128 --served-model-name fmax --guided-decoding-backend auto --tensor-parallel-size 2 ### 🐛 Describe the bug Doing a request would raise the following error: ```python INFO: Application startup...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
