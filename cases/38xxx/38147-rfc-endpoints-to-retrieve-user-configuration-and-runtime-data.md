# vllm-project/vllm#38147: [RFC]: Endpoints to Retrieve User Configuration and Runtime Data

| 字段 | 值 |
| --- | --- |
| Issue | [#38147](https://github.com/vllm-project/vllm/issues/38147) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Endpoints to Retrieve User Configuration and Runtime Data

### Issue 正文摘录

# Motivation User configuration and runtime information available from the vLLM inference server can be used for the following use cases: - Prefix-cache aware routing - HMA-aware scheduling - DP endpoint management - Load tuning This information (KV cache sizes in tokens, attention groups, DP rank info) is computed at startup from vLLM config + model internals + profiling, and is not operator-expressed intent. It is currently being extracted from telemetry metrics which is not a standard and recommended practice to do. The motivation is therefore to provide the following endpoints in vLLM to retrieve the information instead: - `/config`: User configuration data - `/capabilities`: Static and constant runtime data # Design Design doc: https://docs.google.com/document/d/1_DMx72p3rS9AR6EZvtMk-dOooHPq8oMYZ3pFaYe4YXk/edit?tab=t.0 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. @tlrmchlsmth

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Endpoints to Retrieve User Configuration and Runtime Data feature request # Motivation User configuration and runtime information available from the vLLM inference server can be used for the following use cases:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: P rank info) is computed at startup from vLLM config + model internals + profiling, and is not operator-expressed intent. It is currently being extracted from telemetry metrics which is not a standard and recommended pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nce server can be used for the following use cases: - Prefix-cache aware routing - HMA-aware scheduling - DP endpoint management - Load tuning This information (KV cache sizes in tokens, attention groups, DP rank info)...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are scheduling - DP endpoint management - Load tuning This information (KV cache sizes in tokens, attention groups, DP rank info) is computed at startup from vLLM config + model internals + profiling, and is not operato...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
