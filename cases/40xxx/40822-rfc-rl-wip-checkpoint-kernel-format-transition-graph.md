# vllm-project/vllm#40822: [RFC]: [RL - WIP] Checkpoint -> Kernel Format transition graph

| 字段 | 值 |
| --- | --- |
| Issue | [#40822](https://github.com/vllm-project/vllm/issues/40822) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [RL - WIP] Checkpoint -> Kernel Format transition graph

### Issue 正文摘录

# Motivation. ### Why? With growing size of models, inference becoming faster, one thing is stagnating. Weight transfer in RL workloads is usually done with a single NCCL broadcast where every rank loads the full model weights through an iterator and does the whole post-processing logic itself. This is wasteful and also can become a bottleneck. This requires creating a global process group, requires a lot of synchronization and utilizes at most 1 NIC (50GB/s). A lot of work has been done on using RDMA-like transport for weight reloading. This process is (almost) synchronization free and utilizes direct memory writes/reads from remote GPU memory, through IB/EFA/etc. This can significantly speedup the transfer, as there is no synchronization involved, trainers exchange metadata with inference and then either trainers push, or inference engines pull the required weights from its corresponding memory addresses. The issue here becomes the knowledge of how the weights are laid out in inference/trainer memory. ### Checkpoint x Kernel format Currently, weights get loaded from disk from a `HF`-like checkpoint, go through processing and end up in a so-called `kernel format`. This format is...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: [RL - WIP] Checkpoint -> Kernel Format transition graph RFC # Motivation. ### Why? With growing size of models, inference becoming faster, one thing is stagnating. Weight transfer in RL workloads is usually done...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: eights exist during the engine life-time. Some notable examples being - quantized into FP8, scales rearranged into TMA friendly format - `qkv`/`gate_up` fusion - `ColumnLinear` for TP This itself seems okay, but the iss...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: the transfer, as there is no synchronization involved, trainers exchange metadata with inference and then either trainers push, or inference engines pull the required weights from its corresponding memory addresses. The...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ay you want to inference GLM5 FP8. Depending on if you end up using `DeepGemm` FP8 MoE or `Cutlass` FP8 MoE, your gate-up projection might end up like `w1w3` or `w3w1` - and this is just a single example, there is way m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: erence GLM5 FP8. Depending on if you end up using `DeepGemm` FP8 MoE or `Cutlass` FP8 MoE, your gate-up projection might end up like `w1w3` or `w3w1` - and this is just a single example, there is way more of them that I...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
