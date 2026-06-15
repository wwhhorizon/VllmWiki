# vllm-project/vllm#38603: [Bug]: Streaming last chunk contains non-empty tool_calls with empty fields "type" causing type validation error 

| 字段 | 值 |
| --- | --- |
| Issue | [#38603](https://github.com/vllm-project/vllm/issues/38603) |
| 状态 | open |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming last chunk contains non-empty tool_calls with empty fields "type" causing type validation error 

### Issue 正文摘录

### Your current environment Environment vLLM version: v0.17.0.rc1 (with vLLM ascend plugin) Model: Qwen3.5-397B w8a8 Hardware: Atlas800I A2 * 2 Deployment: vllm serve with tool calling enabled vllm serve /data/Qwen3__5-397B-A17B-w8a8-mtp –host 0.0.0.0 –port 8005 –headless –data-parallel-size 2 –data-parallel-size-local 1 –data-parallel-start-rank 1 –data-parallel-address $node0_ip –data-parallel-rpc-port 13389 –seed 1024 –tensor-parallel-size 8 –served-model-name qwen3.5 –max-num-seqs 16 –max-model-len 196608 –max-num-batched-tokens 8096 –reasoning-parser qwen3 –enable-auto-tool-choice –tool-call-parser qwen3_coder –enable-expert-parallel –trust-remote-code –async-scheduling –gpu-memory-utilization 0.9 –no-enable-prefix-caching –speculative-config ‘{“method”: “qwen3_5_mtp”, “num_speculative_tokens”: 3, “enforce_eager”: true}’ –compilation-config ‘{“cudagraph_mode”:“FULL_DECODE_ONLY”}’ –additional-config ‘{“enable_cpu_binding”:true, “multistream_overlap_shared_expert”: true}’ ### 🐛 Describe the bug Problem When streaming tool calls, the last chunk (with finish_reason: "tool_calls") contains a non-empty tool_calls array where all fields are empty strings. This causes client-side ty...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: onment Environment vLLM version: v0.17.0.rc1 (with vLLM ascend plugin) Model: Qwen3.5-397B w8a8 Hardware: Atlas800I A2 * 2 Deployment: vllm serve with tool calling enabled vllm serve /data/Qwen3__5-397B-A17B-w8a8-mtp –h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m_speculative_tokens”: 3, “enforce_eager”: true}’ –compilation-config ‘{“cudagraph_mode”:“FULL_DECODE_ONLY”}’ –additional-config ‘{“enable_cpu_binding”:true, “multistream_overlap_shared_expert”: true}’ ### 🐛 Describe th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: –async-scheduling –gpu-memory-utilization 0.9 –no-enable-prefix-caching –speculative-config ‘{“method”: “qwen3_5_mtp”, “num_speculative_tokens”: 3, “enforce_eager”: true}’ –compilation-config ‘{“cudagraph_mode”:“FULL_DE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mpty strings. This causes client-side type validation to fail with AI_TypeValidationError. [["id":"chatcmpl-9f27290b4e514e18bbbc1f026380a951","model":"qwen3.5","object":"chat.completion.chunk","created":1774600400,"choi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ype validation error bug ### Your current environment Environment vLLM version: v0.17.0.rc1 (with vLLM ascend plugin) Model: Qwen3.5-397B w8a8 Hardware: Atlas800I A2 * 2 Deployment: vllm serve with tool calling enabled...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
