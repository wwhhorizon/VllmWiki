# vllm-project/vllm#36849: [Bug]: GPT-OSS-20B /v1/chat/completions streaming crashes with tool_call_parser=openai (IndexError in chat_completion_stream_generator)

| 字段 | 值 |
| --- | --- |
| Issue | [#36849](https://github.com/vllm-project/vllm/issues/36849) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-20B /v1/chat/completions streaming crashes with tool_call_parser=openai (IndexError in chat_completion_stream_generator)

### Issue 正文摘录

### My current environment ### 🐛 Describe the bug ## GPT-OSS-20B /v1/chat/completions streaming crashes with tool_call_parser=openai (IndexError in chat_completion_stream_generator) I’m seeing a reproducible crash with `openai/gpt-oss-20b` on vLLM `0.17.1` when using the OpenAI-compatible **chat completions** endpoint with **streaming** and **tool parsing enabled**. The failure happens in `chat_completion_stream_generator` with: `IndexError: list index out of range` The relevant traceback is: (APIServer pid=1) ERROR [serving.py:1390] Error in chat completion stream generator. (APIServer pid=1) ERROR [serving.py:1390] Traceback (most recent call last): (APIServer pid=1) ERROR [serving.py:1390] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/serving.py", line 1262, in chat_completion_stream_generator (APIServer pid=1) ERROR [serving.py:1390] args = tool_parser.prev_tool_call_arr[index].get( (APIServer pid=1) ERROR [serving.py:1390] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^ (APIServer pid=1) ERROR [serving.py:1390] IndexError: list index out of range --- ## What I’m running **Model** - openai/gpt-oss-20b **vLLM** - 0.17.1 **Important server args / no...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: i" - enable_auto_tool_choice: true - reasoning_parser: "openai_gptoss" - quantization: "mxfp4" - kv_cache_dtype: "fp8_e4m3" - tensor_parallel_size: 2 - distributed_executor_backend: "mp" - max_model_len: 100000 - enable...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ai (IndexError in chat_completion_stream_generator) I’m seeing a reproducible crash with `openai/gpt-oss-20b` on vLLM `0.17.1` when using the OpenAI-compatible **chat completions** endpoint with **streaming** and **tool...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: GPT-OSS-20B /v1/chat/completions streaming crashes with tool_call_parser=openai (IndexError in chat_completion_stream_generator) bug ### My current environment ### 🐛 Describe the bug ## GPT-OSS-20B /v1/chat/compl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: prefix-caching-hash-algo: "sha256_cbor" disable-uvicorn-access-log: true cudagraph-capture-sizes: [1,2,4,8,16,32,64,128,256,512,1024] compilation_config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: " - max_model_len: 100000 - enable_prefix_caching: true - enable_chunked_prefill: true - async_scheduling: true - stream_interval: 20 Server log confirms the relevant config and behavior: non-default args: {'enable_auto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
