# vllm-project/vllm#3942: [Usage]: Token level reuse for kv cache

| 字段 | 值 |
| --- | --- |
| Issue | [#3942](https://github.com/vllm-project/vllm/issues/3942) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Token level reuse for kv cache

### Issue 正文摘录

### Your current environment vllm=0.4.0 ### How would you like to use vllm I have many prompts with the same prefix, and have reused the blocks using enable_prefix, but still have problems for more efficient reusing: Different requests with enable_prefix=True are only reusing blocks as I understand it. For example, when len(prompt_1)=35 len(prompt_2)=36 block_size=32 I can only reuse the block which the first 32 tokens are located, but not the kv cache for the 33rd-34th tokens, and this process is accompanied by a block swapping process between GPU and CPU. So I would like to ask if token-level reuse is feasible, like my 33rd and 34thtoken. Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sed the blocks using enable_prefix, but still have problems for more efficient reusing: Different requests with enable_prefix=True are only reusing blocks as I understand it. For example, when len(prompt_1)=35 len(promp...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Token level reuse for kv cache usage ### Your current environment vllm=0.4.0 ### How would you like to use vllm I have many prompts with the same prefix, and have reused the blocks using enable_prefix, but stil...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: use vllm I have many prompts with the same prefix, and have reused the blocks using enable_prefix, but still have problems for more efficient reusing: Different requests with enable_prefix=True are only reusing blocks a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: le_prefix, but still have problems for more efficient reusing: Different requests with enable_prefix=True are only reusing blocks as I understand it. For example, when len(prompt_1)=35 len(prompt_2)=36 block_size=32 I c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
