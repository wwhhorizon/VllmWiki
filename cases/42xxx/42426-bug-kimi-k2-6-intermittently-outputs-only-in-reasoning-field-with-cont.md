# vllm-project/vllm#42426: [Bug]: Kimi-K2.6 intermittently outputs only "!!!!!!!!!!" in reasoning field with content null

| 字段 | 值 |
| --- | --- |
| Issue | [#42426](https://github.com/vllm-project/vllm/issues/42426) |
| 状态 | open |
| 标签 | bug |
| 评论 | 69; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.6 intermittently outputs only "!!!!!!!!!!" in reasoning field with content null

### Issue 正文摘录

### Your current environment ### Your current environment * Model: moonshotai/Kimi-K2.6 and redhatai/Kimi-K2.6-NVFP4 * Parsers: --reasoning-parser kimi_k2 --tool-call-parser kimi_k2 * vLLM image tested: v0.20.0 and v0.18.1 * GPUs: 8xB200 ### 🐛 Describe the bug ### Description We are seeing intermittent bad generations from both `moonshotai/Kimi-K2.6` as well as `RedHatAI/Kimi-K2.6-NVFP4` served with vLLM. The response has `content: null`, while the reasoning field contains only repeated exclamation marks, e.g. `"!!!!!!!!!!"`. This looks very similar to the Kimi-K2.5 issue discussed in #36763, especially this comment about FA4 NaNs at KV length >= 8192: https://github.com/vllm-project/vllm/issues/36763#issuecomment-4170658649 The issue is not always immediate. In one deployment we saw it after the service had been running for a few days. We are still trying to isolate whether this is caused by FA4 MLA prefill, NVFP4 GEMM/MoE kernels, long-running state, or a specific traffic pattern. But it seems like this appears when the model has either been running for a while and/or high traffic with large contexts. When the model enters this bad state, requesting logprobs exposes NaNs in the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: w days. We are still trying to isolate whether this is caused by FA4 MLA prefill, NVFP4 GEMM/MoE kernels, long-running state, or a specific traffic pattern. But it seems like this appears when the model has either been...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: current environment * Model: moonshotai/Kimi-K2.6 and redhatai/Kimi-K2.6-NVFP4 * Parsers: --reasoning-parser kimi_k2 --tool-call-parser kimi_k2 * vLLM image tested: v0.20.0 and v0.18.1 * GPUs: 8xB200 ### 🐛 Describe the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l-call-parser kimi_k2 * vLLM image tested: v0.20.0 and v0.18.1 * GPUs: 8xB200 ### 🐛 Describe the bug ### Description We are seeing intermittent bad generations from both `moonshotai/Kimi-K2.6` as well as `RedHatAI/Kimi-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: still trying to isolate whether this is caused by FA4 MLA prefill, NVFP4 GEMM/MoE kernels, long-running state, or a specific traffic pattern. But it seems like this appears when the model has either been running for a w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e are still trying to isolate whether this is caused by FA4 MLA prefill, FLASHINFER_MLA decode, NVFP4 GEMM/MoE kernels, long-running state, high-concurrency scheduling, or a specific traffic pattern. ### Before submitti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
