# vllm-project/vllm#925: Invalid shape for attention bias when serving Bloom

| 字段 | 值 |
| --- | --- |
| Issue | [#925](https://github.com/vllm-project/vllm/issues/925) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Invalid shape for attention bias when serving Bloom

### Issue 正文摘录

This error appears when serving BloomChat `sambanovasystems/BLOOMChat` ``` ... File "/root/miniconda3/envs/LLM/lib/python3.10/site-packages/xformers/ops/fmha/common.py", line 120, in validate_inputs raise ValueError( ValueError: Invalid shape for attention bias: torch.Size([14, 10, 10]) (expected (1, 14, 10, 10)) query.shape: torch.Size([1, 10, 14, 128]) key.shape : torch.Size([1, 10, 14, 128]) value.shape: torch.Size([1, 10, 14, 128]) ``` It seems that the shape of attention bias different from the expected in xFormer, which in BloomChat loses the first dimension.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Invalid shape for attention bias when serving Bloom This error appears when serving BloomChat `sambanovasystems/BLOOMChat` ``` ... File "/root/miniconda3/envs/LLM/lib/python3.10/site-packages/xformers/ops/fmha/common.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
