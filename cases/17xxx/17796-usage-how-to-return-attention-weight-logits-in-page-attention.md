# vllm-project/vllm#17796: [Usage]: how to return attention_weight logits in page_attention

| 字段 | 值 |
| --- | --- |
| Issue | [#17796](https://github.com/vllm-project/vllm/issues/17796) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to return attention_weight logits in page_attention

### Issue 正文摘录

### Your current environment I want to return attention_weight logits in page_attention, origin code is this: ```template __device__ void paged_attention_kernel( ... // Other side args. const scalar_t* __restrict__ out, // [num_seqs, num_heads, max_num_partitions, head_size] const scalar_t* __restrict__ q, // [num_seqs, num_heads, head_size] const scalar_t* __restrict__ k_cache, // [num_blocks, num_kv_heads, head_size/x, block_size, x] const scalar_t* __restrict__ v_cache, // [num_blocks, num_kv_heads, head_size, block_size] ... // Other side args. ) ``` The code I am considering changing is as follows: ``` template __device__ void paged_attention_kernel( ... // Other side args. const scalar_t* __restrict__ out, // [num_seqs, num_heads, max_num_partitions, head_size] scalar_t* __restrict__ attention_weights, const scalar_t* __restrict__ q, // [num_seqs, num_heads, head_size] const scalar_t* __restrict__ k_cache, // [num_blocks, num_kv_heads, head_size/x, block_size, x] const scalar_t* __restrict__ v_cache, // [num_blocks, num_kv_heads, head_size, block_size] ... // Other side args. ) const float inv_sum = __fdividef(1.f, exp_sum + 1e-6f); for (int i = thread_idx; i < num_tokens; i...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s, num_heads, head_size] const scalar_t* __restrict__ k_cache, // [num_blocks, num_kv_heads, head_size/x, block_size, x] const scalar_t* __restrict__ v_cache, // [num_blocks, num_kv_heads, head_size, block_size] ... //...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to return attention_weight logits in page_attention usage;stale ### Your current environment I want to return attention_weight logits in page_attention, origin code is this: ```template __device__ void page...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
