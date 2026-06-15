# vllm-project/vllm#3302: Question regarding GPU memory allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#3302](https://github.com/vllm-project/vllm/issues/3302) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question regarding GPU memory allocation

### Issue 正文摘录

The startup parameter is： python -m vllm.entrypoints.gemma_7b_it \ --model "./gemma_7b_it" \ --port 7501 \ --gpu-memory-utilization 1 \ --max-num-seqs 1024 \ --tensor-parallel-size 4 \ --dtype half \ --trust-remote-code The memory consumption is about 8G on 4xT4 When I set the --max-num-seqs parameter to 100，The memory consumption is about 15G on 4xT4 Why is --max-num-seqs smaller but GPU memory consumption higher？

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: U memory allocation The startup parameter is： python -m vllm.entrypoints.gemma_7b_it \ --model "./gemma_7b_it" \ --port 7501 \ --gpu-memory-utilization 1 \ --max-num-seqs 1024 \ --tensor-parallel-size 4 \ --dtype half \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: \ --max-num-seqs 1024 \ --tensor-parallel-size 4 \ --dtype half \ --trust-remote-code The memory consumption is about 8G on 4xT4 When I set the --max-num-seqs parameter to 100，The memory consumption is about 15G on 4xT4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to 100，The memory consumption is about 15G on 4xT4 Why is --max-num-seqs smaller but GPU memory consumption higher？
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Question regarding GPU memory allocation The startup parameter is： python -m vllm.entrypoints.gemma_7b_it \ --model "./gemma_7b_it" \ --port 7501 \ --gpu-memory-utilization 1 \ --max-num-seqs 1024 \ --tenso
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: U memory allocation The startup parameter is： python -m vllm.entrypoints.gemma_7b_it \ --model "./gemma_7b_it" \ --port 7501 \ --gpu-memory-utilization 1 \ --max-num-seqs 1024 \ --tensor-parallel-size 4 \ --dtype half \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
