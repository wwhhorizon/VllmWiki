# vllm-project/vllm#23969: [Bug]: v1 xformers + sliding window not working

| 字段 | 值 |
| --- | --- |
| Issue | [#23969](https://github.com/vllm-project/vllm/issues/23969) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 xformers + sliding window not working

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug I think nothing in the pass to `xops.memory_efficient_attention_forward` at https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.py#L422 tells xformers that sliding window is being used when it is turned on. The attn bias is the same regardless of whether it is sliding window or not: https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.py#L243 Sliding window in xformers only works for the prompt as the unified_attention pathway is chosen where it is passed through: https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.py#L376 & when blocks get removed: https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/core/kv_cache_manager.py#L243 but this is not per token sliding but rather per block sliding. For v0, there was this: https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/attention/backends/xformers.py#L723 Please lmk if I'm missing something cc @WoosukKwon ### B...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ect/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.py#L422 tells xformers that sliding window is being used when it is turned on. The attn bias is the same regardless of whether i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug I think nothing in the pass to `xops.memory_efficient_attention_forward` at https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: c35b719e3dcac2587ac1/vllm/v1/attention/backends/xformers.py#L376 & when blocks get removed: https://github.com/vllm-project/vllm/blob/5674a40366bae4cfc862c35b719e3dcac2587ac1/vllm/v1/core/kv_cache_manager.py#L243 but th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v1 xformers + sliding window not working bug;stale ### Your current environment / ### 🐛 Describe the bug I think nothing in the pass to `xops.memory_efficient_attention_forward` at https://github.com/vllm-project...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
