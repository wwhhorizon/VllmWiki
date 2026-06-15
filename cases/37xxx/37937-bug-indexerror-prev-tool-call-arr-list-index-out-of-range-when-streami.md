# vllm-project/vllm#37937: [Bug]: IndexError: prev_tool_call_arr list index out of range when streaming tool call hits max_tokens (openai parser)

| 字段 | 值 |
| --- | --- |
| Issue | [#37937](https://github.com/vllm-project/vllm/issues/37937) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IndexError: prev_tool_call_arr list index out of range when streaming tool call hits max_tokens (openai parser)

### Issue 正文摘录

### Your current environment vLLM: 0.18.1rc1.dev32+g1f0d21064 (got from nightly build) PyTorch: 2.10.0+cu129 Python: 3.12.13 CUDA: 12.9 transformers: 4.57.6 ### 🐛 Describe the bug When streaming is enabled and the model is generating tool call arguments, hitting the max_tokens limit causes an unhandled IndexError in chat_completion_stream_generator instead of returning a response chunk with finish_reason="length". The server logs a 200 OK but then throws a 500 Internal Server Error in the stream. The client receives a malformed/broken stream rather than a graceful length-truncated response. Also here is a vllm side error; ```text (APIServer pid=1) INFO: "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=1) ERROR 03-23 22:35:03 [serving.py:1261] Error in chat completion stream generator. (APIServer pid=1) ERROR 03-23 22:35:03 [serving.py:1261] Traceback (most recent call last): (APIServer pid=1) ERROR 03-23 22:35:03 [serving.py:1261] File ".../vllm/entrypoints/openai/chat_completion/serving.py", line 1133, in chat_completion_stream_generator (APIServer pid=1) ERROR 03-23 22:35:03 [serving.py:1261] args = tool_parser.prev_tool_call_arr[index].get( (APIServer pid=1) ERROR 03-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: current environment vLLM: 0.18.1rc1.dev32+g1f0d21064 (got from nightly build) PyTorch: 2.10.0+cu129 Python: 3.12.13 CUDA: 12.9 transformers: 4.57.6 ### 🐛 Describe the bug When streaming is enabled and the model is gener...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1f0d21064 (got from nightly build) PyTorch: 2.10.0+cu129 Python: 3.12.13 CUDA: 12.9 transformers: 4.57.6 ### 🐛 Describe the bug When streaming is enabled and the model is generating tool call arguments, hitting the max_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ns. development ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory cuda;quantization;sampling build_error;crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ers: 4.57.6 ### 🐛 Describe the bug When streaming is enabled and the model is generating tool call arguments, hitting the max_tokens limit causes an unhandled IndexError in chat_completion_stream_generator instead of re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory cuda;quantization;sampling build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
