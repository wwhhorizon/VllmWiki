# vllm-project/vllm#38203: [Bug]: M2.5 tool call result is badcase, deploy 1p1d with nixl connector, P and D use DP8-EP-TP1

| 字段 | 值 |
| --- | --- |
| Issue | [#38203](https://github.com/vllm-project/vllm/issues/38203) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: M2.5 tool call result is badcase, deploy 1p1d with nixl connector, P and D use DP8-EP-TP1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug M2.5 model on Vllm-v0.18, 1P1D, DP8-EP-TP1, send tool call case to api, but result have badcase of repeat and tool call args is null TP4 not have this problem badcase1: ```bash { "choices": [ { "finish_reason": "length", "index": 0, "logprobs": null, "message": { "annotations": null, "audio": null, "content": "", "function_call": null, "reasoning": "用户 \n invoked婿_messages_messages_user. user .messages_user \n \n Asia/Tokyo \n \n ", "refusal": null, "role": "assistant", "tool_calls": [ { "function": { "arguments": "", "name": "get_weather" }, "id": "chatcmpl-tool-8da5ed89077793ef", "type": "function" } ] }, "stop_reason": null, "token_ids": null } ], "created": 1774511041, "id": "chatcmpl-5415357f-94fb-416e-ad75-cf3ad57064c0", "kv_transfer_params": null, "model": "MiniMax-M2.5", "object": "chat.completion", "prompt_logprobs": null, "prompt_token_ids": null, "service_tier": null, "system_fingerprint": null, "usage": { "completion_tokens": 26, "prompt_tokens": 242, "prompt_tokens_details": null, "total_tokens": 268 }, "input": { "model": "ep-minimax-m2.5-7e3713", "max_tokens": 1024, "messages": [ { "role": "user", "content": "What...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --tensor-parallel-size 1 \ --enable-expert-parallel \ --data-parallel-start-rank 0 \ --data-parallel-size-local 8 \ --data-parallel-address ${DATA_PARALLEL_ADDRESS} \ --data-parallel-r
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --data-parallel-rpc-port 55555 \ --data-parallel-backend mp \ --kv-transfer-config '{"kv_connector": "NixlConnector","kv_role": "kv_both"}' \ --distributed-executor-backend mp \ --host 0.0.0.0 \ --
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: EP-TP1 bug ### Your current environment ### 🐛 Describe the bug M2.5 model on Vllm-v0.18, 1P1D, DP8-EP-TP1, send tool call case to api, but result have badcase of repeat and tool call args is null TP4 not have this probl...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
