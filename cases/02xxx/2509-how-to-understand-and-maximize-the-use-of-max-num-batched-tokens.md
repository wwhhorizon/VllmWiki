# vllm-project/vllm#2509: How to Understand and Maximize the Use of max_num_batched_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#2509](https://github.com/vllm-project/vllm/issues/2509) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to Understand and Maximize the Use of max_num_batched_tokens

### Issue 正文摘录

I am currently running the Yi34B model on four A10 (24G) GPUs, utilizing AWQ 4-bit quantization. My goal is to deploy the model in a production environment, maximizing memory utilization and throughput without overwhelming the system with high loads. Through repeated experiments, I've found that setting `max_num_batched_tokens` seems to be the only way to meet my requirements. When I set max_num_batched_tokens=50000, the GPU blocks are 758, and after model loaded, each GPU only utilizes about half of its available VRAM. If I increase this value further, the model fails to load. ``` { "swap_space": 4, "tensor_parallel_size": 4, "max_num_batched_tokens": 50000 } ``` When I set max_num_batched_tokens=20480, the GPU blocks are 4485. That's confusing and I wander the exact meaning of `max_num_batched_tokens`. I'm seeking advice on how to balance maximizing throughput while ensuring the stability of the model under these circumstances. What would be the best approach to achieve this? I'm using the latest version v0.2.7

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: imizing throughput while ensuring the stability of the model under these circumstances. What would be the best approach to achieve this? I'm using the latest version v0.2.7
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the model in a production environment, maximizing memory utilization and throughput without overwhelming the system with high loads. Through repeated experiments, I've found that setting `max_num_batched_tokens` seems t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ntly running the Yi34B model on four A10 (24G) GPUs, utilizing AWQ 4-bit quantization. My goal is to deploy the model in a production environment, maximizing memory utilization and throughput without overwhelming the sy...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: meet my requirements. When I set max_num_batched_tokens=50000, the GPU blocks are 758, and after model loaded, each GPU only utilizes about half of its available VRAM. If I increase this value further, the model fails t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: imize the Use of max_num_batched_tokens I am currently running the Yi34B model on four A10 (24G) GPUs, utilizing AWQ 4-bit quantization. My goal is to deploy the model in a production environment, maximizing memory util...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
