# vllm-project/vllm#4496: [Bug]: The first token generated after prefill occupies the GPU memory but virtual block

| 字段 | 值 |
| --- | --- |
| Issue | [#4496](https://github.com/vllm-project/vllm/issues/4496) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The first token generated after prefill occupies the GPU memory but virtual block

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After prefilling, the Transformer generates the first token, which has its own QKV and occupies actual physical GPU memory, correct? I set the block_size to 16, num_gpu_blocks_override to 6, and submit 3 requests. All the requests' prompts are None, and prompt_token_ids are [0, 1, ..., 15, 16], totaling 17 tokens. After a step(), I use engine.scheduler.block_manager.get_num_free_gpu_blocks() to obtain the number of free blocks, which shows that there are no free blocks (0). Does this mean that tokens 0 to 15 are allocated on block 0 and token 16 is allocated on block 1? In another test, the requests' prompt_token_ids are [0, 1, ..., 15], totaling 16 tokens, with the same settings as before. After a step(), are there 3 free blocks? So, does the new token generated after prefilling not occupy a block?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: The first token generated after prefill occupies the GPU memory but virtual block bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After prefilling,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: The first token generated after prefill occupies the GPU memory but virtual block bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After prefilling,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: first token generated after prefill occupies the GPU memory but virtual block bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After prefilling, the Transfo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e allocated on block 0 and token 16 is allocated on block 1? In another test, the requests' prompt_token_ids are [0, 1, ..., 15], totaling 16 tokens, with the same settings as before. After a step(), are there 3 free bl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
