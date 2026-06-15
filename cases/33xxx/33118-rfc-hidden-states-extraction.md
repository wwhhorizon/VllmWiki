# vllm-project/vllm#33118: [RFC]: Hidden States Extraction

| 字段 | 值 |
| --- | --- |
| Issue | [#33118](https://github.com/vllm-project/vllm/issues/33118) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Hidden States Extraction

### Issue 正文摘录

### Motivation. Goal: Implement a solution for getting hidden states from any model layer out of vLLM in a performant way. Speculative decoding algorithms such as Eagle3 and DFlash take “verifier” model hidden states (from multiple layers) as input. Therefore, training these “draft” models requires a dataset of hidden states, with corresponding tokens. Currently vLLM provides no official approach to extracting these hidden states. In addition, access to hidden states enables research work in RL ([example](https://github.com/hf618/VERL)) and quantization domains. Existing solutions to this problem typically fall into one of the following categories. 1. Use transformers for hidden states generation. This has two major disadvantages: It loses all of vllm’s performance optimizations, large model/distributed support, etc. and it opens a whole class of potential bugs caused by minor mismatches between transformer and vllm hidden states. 2. Heavy modification and patching of vllm to enable this feature. Solutions typically require manually setting up core vllm components and accessing internal apis. This produces a large maintenance burden as vllm internals are updated. It also means man...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ing hidden states from any model layer out of vLLM in a performant way. Speculative decoding algorithms such as Eagle3 and DFlash take “verifier” model hidden states (from multiple layers) as input. Therefore, training...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tivation. Goal: Implement a solution for getting hidden states from any model layer out of vLLM in a performant way. Speculative decoding algorithms such as Eagle3 and DFlash take “verifier” model hidden states (from mu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng these hidden states. In addition, access to hidden states enables research work in RL ([example](https://github.com/hf618/VERL)) and quantization domains. Existing solutions to this problem typically fall into one of...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: rence). 2. There is an extensible public api KV Connector for extracting kv cache data out of vllm with existing implementations for storing to disk, offloading to cpu memory, disagg P/D, etc. 3. Hidden states map to to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: dden states - Efficient transfer of hidden states between processes (non-blocking) ### Proposed Change. Our proposed solution is based on a few key insights: 1. There is already a system (aux_hidden_states) for plumbing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
