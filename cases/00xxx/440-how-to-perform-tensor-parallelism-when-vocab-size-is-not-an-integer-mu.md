# vllm-project/vllm#440: How to perform tensor parallelism when `vocab_size` is not an integer multiple of `world_size`?

| 字段 | 值 |
| --- | --- |
| Issue | [#440](https://github.com/vllm-project/vllm/issues/440) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to perform tensor parallelism when `vocab_size` is not an integer multiple of `world_size`?

### Issue 正文摘录

When I try to load a bloom-based model to an 8-GPUs server, I met the following error: ``` AssertionError: 250682 is not divisible by 8 ``` It seems the following check will be performed before tensor parallelism: https://github.com/vllm-project/vllm/blob/c894836108732d0cbb6fce15aeda8de1218a380d/vllm/model_executor/parallel_utils/tensor_parallel/utils.py#L66-L70 I check the model's `config.json` and found its `vocab_size` is 250682. Obviously it cannot pass the check above. So how could I perform tensor parallelism when `vocab_size` is not an integer multiple of `world_size`?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ot an integer multiple of `world_size`? When I try to load a bloom-based model to an 8-GPUs server, I met the following error: ``` AssertionError: 250682 is not divisible by 8 ``` It seems the following check will be pe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How to perform tensor parallelism when `vocab_size` is not an integer multiple of `world_size`? When I try to load a bloom-based model to an 8-GPUs server, I met the following error: ``` AssertionError: 250682 is not di...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: size` is not an integer multiple of `world_size`? When I try to load a bloom-based model to an 8-GPUs server, I met the following error: ``` AssertionError: 250682 is not divisible by 8 ``` It seems the following check...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
