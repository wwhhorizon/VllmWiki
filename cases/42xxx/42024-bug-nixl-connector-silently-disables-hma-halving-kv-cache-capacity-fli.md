# vllm-project/vllm#42024: [Bug]: NIXL connector silently disables HMA, halving KV cache capacity — flip default to HMA=on even with connectors

| 字段 | 值 |
| --- | --- |
| Issue | [#42024](https://github.com/vllm-project/vllm/issues/42024) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;operator |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NIXL connector silently disables HMA, halving KV cache capacity — flip default to HMA=on even with connectors

### Issue 正文摘录

### Your current environment - GPU: RTX 6000 Pro (reproduced); expected to affect all GPU types - Model: openai/gpt-oss-120b (hybrid architecture with sliding window layers) - vLLM version: 0.18.x (current) - OS/Container: Standard vLLM container image ### 🐛 Describe the bug ## Summary Enabling the NIXL connector (`NixlConnector`) for prefill/decode KV transfer silently disables the Hybrid Memory Allocator (HMA). This causes all transformer layers to be treated as full attention, roughly doubling per-layer KV cache footprint and cutting effective KV cache capacity in half. There is no warning at startup that names the connector as the cause. **Severity:** High — affects all P/D disaggregation deployments using `NixlConnector`. **Component:** KV cache / NIXL connector / Hybrid Memory Allocator ## Steps to Reproduce ### 1. Run with NIXL connector (TP=2) ```bash vllm serve \ --host 0.0.0.0 --port 8000 \ --model openai/gpt-oss-120b \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 2 \ --no-enable-prefix-caching \ --load-format dummy \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` ### 2. Run without NIXL connector (TP=2, same config otherwise) `...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: [Bug]: NIXL connector silently disables HMA, halving KV cache capacity — flip default to HMA=on even with connectors bug ### Your current environment - GPU: RTX 6000 Pro (reproduced); expected to affect all GPU types -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt - GPU: RTX 6000 Pro (reproduced); expected to affect all GPU types - Model: openai/gpt-oss-120b (hybrid architecture with sliding window layers) - vLLM version: 0.18.x (current) - OS/Container: Standard vLLM containe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e the bug ## Summary Enabling the NIXL connector (`NixlConnector`) for prefill/decode KV transfer silently disables the Hybrid Memory Allocator (HMA). This causes all transformer layers to be treated as full attention,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: NIXL connector silently disables HMA, halving KV cache capacity — flip default to HMA=on even with connectors bug ### Your current environment - GPU: RTX 6000 Pro (reproduced); expected to affect all GPU types -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to HMA=on even with connectors bug ### Your current environment - GPU: RTX 6000 Pro (reproduced); expected to affect all GPU types - Model: openai/gpt-oss-120b (hybrid architecture with sliding window layers) - vLLM ver...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
