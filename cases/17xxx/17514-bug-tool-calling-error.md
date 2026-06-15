# vllm-project/vllm#17514: [Bug]: tool calling error

| 字段 | 值 |
| --- | --- |
| Issue | [#17514](https://github.com/vllm-project/vllm/issues/17514) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tool calling error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start vllm openai server: ``` export VLLM_ATTENTION_BACKEND=FLASH_ATTN && vllm serve /models/Qwen2.5-7B-Instruct --served-model-name helium --disable-log-requests --gpu-memory-utilization 0.95 --max-model-len 16384 --pipeline-parallel-size 1 --enable-prefix-caching --enable-chunked-prefill --port 8000 --tensor-parallel-size 1 --enable-auto-tool-choice --tool-call-parser hermes ``` send request with tool calling. I got following error: ``` INFO 05-01 01:51:54 [chat_utils.py:379] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. ERROR 05-01 01:51:54 [serving_chat.py:898] Error in chat_completion_full_generator - cannot determine if tools should be extracted. Returning a standard chat completion. INFO: 114.242.33.191:32107 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 05-01 01:51:54 [serving_chat.py:898] Error in chat_completion_full_generator - cannot determine if tools should be extracted. Returning a standard chat completion. INFO: 114.242.33.191:27283 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 05-01 01:51:54 [serving_chat.py:898] Error in chat_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: tool calling error bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug start vllm openai server: ``` export VLLM_ATTENTION_BACKEND=FLASH_ATTN && vllm serve /models/Qwen2.5-7B-Instruct --ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operato...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: enai server: ``` export VLLM_ATTENTION_BACKEND=FLASH_ATTN && vllm serve /models/Qwen2.5-7B-Instruct --served-model-name helium --disable-log-requests --gpu-memory-utilization 0.95 --max-model-len 16384 --pipeline-parall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 🐛 Describe the bug start vllm openai server: ``` export VLLM_ATTENTION_BACKEND=FLASH_ATTN && vllm serve /models/Qwen2.5-7B-Instruct --served-model-name helium --disable-log-requests --gpu-memory-utilization 0.95 --max-m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
