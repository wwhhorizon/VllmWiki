# vllm-project/vllm#1039: How many batch size can be computed in A100 40GB GPU ?

| 字段 | 值 |
| --- | --- |
| Issue | [#1039](https://github.com/vllm-project/vllm/issues/1039) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 | throughput |
| Operator 关键词 | attention |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> How many batch size can be computed in A100 40GB GPU ?

### Issue 正文摘录

Hello, I want to check how many batched sentences can be computed in a single a100 40GB GPU. I uses the example file (benchmark_latency.py) and only changed the number of batch, input/output length. In my environment condition, i used OPT-13B (fp16), block size (32) input (64), output (1024) and change the number of batch from 1 to 128. I thought that since there is 40GB available, up to **16 batches** would be possible -> OPT-13B weight size (26GB)+KV size (16*5120*2*40*(64+1024)*2B/2^30)=39.28GB But i checked that the maximum number of batch size is 64, it more 4 times than that of throughput (GPU blocks: 459, CPU blocks: 163). No matter how the pagedattention can reduce the memory waste, I can't understand why the maximum batch size is 64. Is it related to the swap function ?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nces can be computed in a single a100 40GB GPU. I uses the example file (benchmark_latency.py) and only changed the number of batch, input/output length. In my environment condition, i used OPT-13B (fp16), block size (3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: input/output length. In my environment condition, i used OPT-13B (fp16), block size (32) input (64), output (1024) and change the number of batch from 1 to 128. I thought that since there is 40GB available, up to **16 b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: to the swap function ? performance attention_kv_cache attention slowdown dtype;memory_layout;shape Hello, I want to check how many batched sentences can be computed in a single a100 40GB GPU.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How many batch size can be computed in A100 40GB GPU ? Hello, I want to check how many batched sentences can be computed in a single a100 40GB GPU. I uses the example file (benchmark_latency.py) and only changed the num...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
