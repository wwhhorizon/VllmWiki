# vllm-project/vllm#5590: [Bug]: The "sorted(gpu_ids)" operation in ray_gpu_executor.py causes an incorrect order of GPU IDs When using the NVIDIA HGX A100 (16-GPU) platform for model inference. 

| 字段 | 值 |
| --- | --- |
| Issue | [#5590](https://github.com/vllm-project/vllm/issues/5590) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The "sorted(gpu_ids)" operation in ray_gpu_executor.py causes an incorrect order of GPU IDs When using the NVIDIA HGX A100 (16-GPU) platform for model inference. 

### Issue 正文摘录

### Your current environment Unable to obtain environmental information at the moment. ### 🐛 Describe the bug In the code vllm/executor/ray_gpu_executor.py:line 142, if the number of GPUs on a node exceeds 10 (such as NVIDIA HGX A100 with 16-GPU), the result of sorted(gpu_ids) would be 0,10,11,12,13,14,15,2,3,4,5,6,7,8,9, instead of 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15. This results in an NCCL Error, because the order of GPUs in the Ray Executor (lexicographical order) is inconsistent with the order of GPUs in NCCL (actual numerical order). The correct way should be node_gpus[node_id] = sorted(gpu_ids, key=lambda x: int(x))

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ographical order) is inconsistent with the order of GPUs in NCCL (actual numerical order). The correct way should be node_gpus[node_id] = sorted(gpu_ids, key=lambda x: int(x))
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ct order of GPU IDs When using the NVIDIA HGX A100 (16-GPU) platform for model inference. bug ### Your current environment Unable to obtain environmental information at the moment. ### 🐛 Describe the bug In the code vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ecutor.py causes an incorrect order of GPU IDs When using the NVIDIA HGX A100 (16-GPU) platform for model inference. bug ### Your current environment Unable to obtain environmental information at the moment. ### 🐛 Descr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
