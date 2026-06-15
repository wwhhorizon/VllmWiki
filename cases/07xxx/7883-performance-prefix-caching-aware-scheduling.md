# vllm-project/vllm#7883: [Performance]: Prefix-caching aware scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#7883](https://github.com/vllm-project/vllm/issues/7883) |
| 状态 | closed |
| 标签 | help wanted;performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Prefix-caching aware scheduling

### Issue 正文摘录

### Proposal to improve performance The current execution flow with prefix caching is as follows: 1. Scheduler takes the next prefill sequence: a. Calculate how many blocks it needs. b. Check whether we have sufficient number of blocks in the block manager. c. If so, determine the number of tokens to be prefilled in this batch (it is equal to the prompt length without chunked prefill, or at maximum the chunked size otherwise). d. Update the batch token budget by subtracting the tokens to be prefilled. e. Allocate all (regardless how many tokens to prefill in this batch) blocks. f. Match allocated block IDs with prefix cache, and list them in `computed_block_nums`. 2. Prepare input: a. Get the number of tokens to prefill for this sequence in this batch. b. Setup input token IDs and positions. c. If `computed_block_nums` is not none, then remove the cached tokens from input tokens, and adjust input positions, query length and context length accordingly. 3. Execute the model. The inefficiencies are then: 1. In Step 1.b, we now don't consider prefix caching. Taking a sequence with 16 blocks in prompt as an example, it now requires block manager to have 16 free blocks to be scheduled....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rmance The current execution flow with prefix caching is as follows: 1. Scheduler takes the next prefill sequence: a. Calculate how many blocks it needs. b. Check whether we have sufficient number of blocks in the block...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a. Calculate how many blocks it needs. b. Check whether we have sufficient number of blocks in the block manager. c. If so, determine the number of tokens to be prefilled in this batch (it is equal to the prompt length...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 23 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: to prefill in this batch) blocks. f. Match allocated block IDs with prefix cache, and list them in `computed_block_nums`. 2. Prepare input: a. Get the number of tokens to prefill for this sequence in this batch. b. Setu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 1. Scheduler takes the next prefill sequence: a. Calculate how many blocks it needs. b. Check whether we have sufficient number of blocks in the block manager. c. If so, determine the number of tokens to be prefilled in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
