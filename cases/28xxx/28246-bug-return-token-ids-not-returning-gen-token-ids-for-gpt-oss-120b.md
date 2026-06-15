# vllm-project/vllm#28246: [Bug]: Return Token Ids not returning Gen Token Ids for GPT-OSS-120b

| 字段 | 值 |
| --- | --- |
| Issue | [#28246](https://github.com/vllm-project/vllm/issues/28246) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Return Token Ids not returning Gen Token Ids for GPT-OSS-120b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When passing in return_token_ids flag to v1/chat/completions endpoint for GPTOSS-120b, only prompt_token_ids are returned and not token_ids. We have not seen this happen with any other model except GPTOSS-120b ``` curl --location 'http://localhost:8015/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "gpt-oss-120b", "messages": [{"content": "Hello!", "role": "user"}], "temperature": 0, "return_token_ids": true }' ``` `{"id":"chatcmpl-a19161b8131141e2a79495025adb40eb","object":"chat.completion","created":1762462711,"model":"gpt-oss-120b","choices":[{"index":0,"message":{"role":"assistant","content":"Hello! How can I help you today?","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":"The user says \"Hello!\" We should respond politely. No special instructions. Just greet back."},"logprobs":null,"finish_reason":"stop","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":71,"total_tokens":109,"completion_tokens":38,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":[20...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ing_content":"The user says \"Hello!\" We should respond politely. No special instructions. Just greet back."},"logprobs":null,"finish_reason":"stop","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m-gpt-oss-120b \ --gpus '"device=4,5"' \ --shm-size=16g \ -e TORCH_CUDA_ARCH_LIST="9.0" \ -v /mlf1-shared/user/gpt-oss-120b:/opt/model \ -p ${PORT}:${PORT} \ vllm/vllm-openai:latest\ --model /opt/model \ --served-model-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Return Token Ids not returning Gen Token Ids for GPT-OSS-120b bug;stale ### Your current environment ### 🐛 Describe the bug When passing in return_token_ids flag to v1/chat/completions endpoint for GPTOSS-120b, o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Return Token Ids not returning Gen Token Ids for GPT-OSS-120b bug;stale ### Your current environment ### 🐛 Describe the bug When passing in return_token_ids flag to v1/chat/completions endpoint for GPTOSS-120b, o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er/gpt-oss-120b:/opt/model \ -p ${PORT}:${PORT} \ vllm/vllm-openai:latest\ --model /opt/model \ --served-model-name "${SERVED_MODEL_NAME}" \ --tensor-parallel-size "${TP_SIZE}" \ --gpu-memory-utilization "${GPU_UTIL}" \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
