# vllm-project/vllm#14604: [Usage]: Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens per block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#14604](https://github.com/vllm-project/vllm/issues/14604) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens per block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks

### Issue 正文摘录

I have a question about "Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens per block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks". So, will adjusting the layout order of each dimension improve memory access? Is there still no difference? Or will the performance decrease? Thanks for your reply. @zhuohan123 @WoosukKwon @suquark @merrymercy

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks usage;stale I have a question about "Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens pe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Usage]: Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens per block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks usage;stale I have a quest...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , # of tokens per block, # of heads, hidden dimension per K/V head) when building physical KV Cache Blocks usage;stale I have a question about "Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of bloc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: den dimension per K/V head) when building physical KV Cache Blocks usage;stale I have a question about "Why does vllm choose a layout of (# of transfomer layers, 2(K/V), # of blocks, # of tokens per block, # of heads, h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
