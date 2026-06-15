# vllm-project/vllm#1297: Low VRAM batch processing mode

| 字段 | 值 |
| --- | --- |
| Issue | [#1297](https://github.com/vllm-project/vllm/issues/1297) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Low VRAM batch processing mode

### Issue 正文摘录

This is a research topic and idea to make low VRAM GPUs usable for running large models in batch processing setups, where latency don't matter that much. For example running a 70B model on a 3080Ti with only 12GB of VRAM (ctransformers, 8-bit GGUF) is possible if only 12 layers are loaded on the GPU and the rest are running on the CPU. Doing so leaves the GPU largely underutilized, as the nvtop output clearly shows: ![image](https://github.com/vllm-project/vllm/assets/1848514/51e172bb-ae8f-4de3-8a6b-c4ee17bffa8c) We could run the whole model on the GPU by loading only 10 layers at a time (to free up space for the KV cache and other overhead) and running a wide batch of sequences (like 4096) through the layers loaded. Repeat until all layers are processed. We could also think about this mode as time multiplexing the same GPU over multiple pipeline steps. It would need loading all the weights into VRAM once for every batch of prompt tokens processed or every new token generated, but this cost would be amortized over all the sequences processed at the same time. Loading of the weights would ideally happen from CPU RAM, but may also happen from disk swap on fast NVMe should the CPU RA...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Low VRAM batch processing mode feature request This is a research topic and idea to make low VRAM GPUs usable for running large models in batch processing setups, where latency don't matter that much. For example runnin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: on the GPU by loading only 10 layers at a time (to free up space for the KV cache and other overhead) and running a wide batch of sequences (like 4096) through the layers loaded. Repeat until all layers are processed. W...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a research topic and idea to make low VRAM GPUs usable for running large models in batch processing setups, where latency don't matter that much. For example running a 70B model on a 3080Ti with only 12GB of VRAM (ctran...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Low VRAM batch processing mode feature request This is a research topic and idea to make low VRAM GPUs usable for running large models in batch processing setups, where latency don't matter that much. For example runnin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: M GPUs usable for running large models in batch processing setups, where latency don't matter that much. For example running a 70B model on a 3080Ti with only 12GB of VRAM (ctransformers, 8-bit GGUF) is possible if only...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
