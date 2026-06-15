# vllm-project/vllm#823: GPU memory requirement very high + tensor parallelization acts weird

| 字段 | 值 |
| --- | --- |
| Issue | [#823](https://github.com/vllm-project/vllm/issues/823) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU memory requirement very high + tensor parallelization acts weird

### Issue 正文摘录

I am using a system with 2 A100 GPUs to run Llama2-13b chat model on vLLMs. If I use tensor_parallel_size = 2, then the model takes up to 38GB on each GPU -- total 76GB. If I use tensor_parallel_size = 1, then the model takes up to 38GB on just one GPU. If I use huggingface pipeline, then the model in total takes around 26GB. Can anyone explain the reason for this discrepancy

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r parallelization acts weird I am using a system with 2 A100 GPUs to run Llama2-13b chat model on vLLMs. If I use tensor_parallel_size = 2, then the model takes up to 38GB on each GPU -- total 76GB. If I use tensor_para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: very high + tensor parallelization acts weird I am using a system with 2 A100 GPUs to run Llama2-13b chat model on vLLMs. If I use tensor_parallel_size = 2, then the model takes up to 38GB on each GPU -- total 76GB. If...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GPU memory requirement very high + tensor parallelization acts weird I am using a system with 2 A100 GPUs to run Llama2-13b chat model on vLLMs. If I use tensor_parallel_size = 2, then the model takes up to 38GB on each

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
