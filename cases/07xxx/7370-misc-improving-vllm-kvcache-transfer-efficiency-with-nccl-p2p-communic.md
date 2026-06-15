# vllm-project/vllm#7370: [Misc]:  Improving VLLM KVCACHE Transfer Efficiency with NCCL P2P Communication

| 字段 | 值 |
| --- | --- |
| Issue | [#7370](https://github.com/vllm-project/vllm/issues/7370) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]:  Improving VLLM KVCACHE Transfer Efficiency with NCCL P2P Communication

### Issue 正文摘录

### Anything you want to discuss about vllm. I hope to utilize the NCCL point-to-point communication protocol (P2P) to transfer the VLLM KVCACHE from the prefill node to the decode node for decoupled inference. Since the KVCACHE in VLLM is stored as a list of tensors, I need to send approximately 16,384 block slices every time I transmit 128 blocks. The non-contiguous distribution of these slices in GPU memory leads to low efficiency in the cyclic transmission, preventing optimal utilization of the communication bandwidth. Therefore, I am considering concatenating these slices into a single large tensor for transmission. On the receiving end, the node would split this large tensor and write the data back to the corresponding positions based on the slice indices. However, this process is quite time-consuming due to the involvement of up to 16,384 slices. I would like to know if CUDA operations can be utilized to parallelize this process in order to improve performance. Additionally, does this decoupled KVCACHE transfer method have any design flaws? Do you have any better suggestions?

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: VLLM is stored as a list of tensors, I need to send approximately 16,384 block slices every time I transmit 128 blocks. The non-contiguous distribution of these slices in GPU memory leads to low efficiency in the cyclic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nsors, I need to send approximately 16,384 block slices every time I transmit 128 blocks. The non-contiguous distribution of these slices in GPU memory leads to low efficiency in the cyclic transmission, preventing opti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: point communication protocol (P2P) to transfer the VLLM KVCACHE from the prefill node to the decode node for decoupled inference. Since the KVCACHE in VLLM is stored as a list of tensors, I need to send approximately 16...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Misc]: Improving VLLM KVCACHE Transfer Efficiency with NCCL P2P Communication ### Anything you want to discuss about vllm. I hope to utilize the NCCL point-to-point communication protocol (P2P) to transfer the VLLM KVC...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: transmit 128 blocks. The non-contiguous distribution of these slices in GPU memory leads to low efficiency in the cyclic transmission, preventing optimal utilization of the communication bandwidth. Therefore, I am consi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
