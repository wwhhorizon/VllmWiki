# vllm-project/vllm#367: Tensor Parallelism vs Data Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#367](https://github.com/vllm-project/vllm/issues/367) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tensor Parallelism vs Data Parallelism

### Issue 正文摘录

Hi, thanks! I use vllm to inference the llama-7B model on single gpu, and tensor-parallel on 2-gpus and 4-gpus, we found that it is 10 times faster than HF on a single GPU, but using tensor parallelism, there is no significant increase in token throughput.We understand that through data parallelism, the memory can be expanded and the batch of processing samples can be increased.But the communication between graphics cards may reduce the speed. If 2-gpus is used, there should be an acceleration of 1.5✖️. But now the throughput has basically remained unchanged. Is it because our GPU KV cache usage is full, or there are other reasons. Looking forward to your reply! ​

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Parallelism vs Data Parallelism Hi, thanks! I use vllm to inference the llama-7B model on single gpu, and tensor-parallel on 2-gpus and 4-gpus, we found that it is 10 times faster than HF on a single GPU, but using tens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Tensor Parallelism vs Data Parallelism Hi, thanks! I use vllm to inference the llama-7B model on single gpu, and tensor-parallel on 2-gpus and 4-gpus, we found that it is 10 times faster than HF on a single GPU, but usi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: w the throughput has basically remained unchanged. Is it because our GPU KV cache usage is full, or there are other reasons. Looking forward to your reply! ​
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: but using tensor parallelism, there is no significant increase in token throughput.We understand that through data parallelism, the memory can be expanded and the batch of processing samples can be increased.But the com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
