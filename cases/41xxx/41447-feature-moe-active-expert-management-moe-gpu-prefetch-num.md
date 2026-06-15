# vllm-project/vllm#41447: [Feature]: MoE Active Expert Management --moe-gpu-prefetch <num>

| 字段 | 值 |
| --- | --- |
| Issue | [#41447](https://github.com/vllm-project/vllm/issues/41447) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MoE Active Expert Management --moe-gpu-prefetch <num>

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## 🚀 The feature, motivation and pitch I would like to propose a new feature for vLLM to improve memory efficiency and scalability for sparse Mixture-of-Experts (MoE) models: **`--moe-gpu-prefetch `** This feature introduces **expert-level GPU memory management**, allowing only a limited number of experts to reside on GPU while the rest are offloaded to CPU memory. --- ### Motivation Modern MoE models (e.g., Gemma, Mixtral-style architectures) contain a large number of experts per layer (e.g., 128), but only a small subset (e.g., top-8) are activated per token. Current approaches to handle GPU memory constraints include: * Full model residency on GPU (high memory requirement) * Layer-level CPU offload (coarse-grained and inefficient) These approaches do not align well with the fundamental property of MoE: > Activation is sparse at the expert level, not at the layer level. As a result: * GPU memory is wasted on inactive experts * Data movement is excessive when offloading entire layers * Large MoE models cannot efficiently run on limited GPU setups --- ### Proposed feature ```bash --moe-gpu-prefetch ``` Where ` ` defines the number of expert...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Feature]: MoE Active Expert Management --moe-gpu-prefetch <num> feature request ### 🚀 The feature, motivation and pitch ## 🚀 The feature, motivation and pitch I would like to propose a new feature for vLLM to improve m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: els: **`--moe-gpu-prefetch `** This feature introduces **expert-level GPU memory management**, allowing only a limited number of experts to reside on GPU while the rest are offloaded to CPU memory. --- ### Motivation Mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: contains: * shared layers * router * a fixed number of ` ` expert slots * During inference: * If a routed expert is already on GPU → execute directly * If not → load it from CPU into GPU (evicting another expert if need...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ory. --- ### Motivation Modern MoE models (e.g., Gemma, Mixtral-style architectures) contain a large number of experts per layer (e.g., 128), but only a small subset (e.g., top-8) are activated per token. Current approa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ve memory efficiency and scalability for sparse Mixture-of-Experts (MoE) models: **`--moe-gpu-prefetch `** This feature introduces **expert-level GPU memory management**, allowing only a limited number of experts to res...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
