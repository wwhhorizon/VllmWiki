# vllm-project/vllm#21694: [Bug]: Local attention chunking edge case when num_blocks == 1?

| 字段 | 值 |
| --- | --- |
| Issue | [#21694](https://github.com/vllm-project/vllm/issues/21694) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Local attention chunking edge case when num_blocks == 1?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### issue In #21692, I'm adding some test cases for [make_local_attention_virtual_batches](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/utils.py#L271C5-L271C41) used for creating 'virtual' branches for local attn. I noticed that when I choose `q_seq_lens` and `kv_seq_lens` inputs such that no. of local blocks is 1, and attention chunk size 0 1 2 3 4 q_toks v _____________ 0 | 1 ``` Instead, shouldn't this be: ``` k_toks > 0 1 2 3 4 q_toks v _____________ 0 | 1 1 1 1 ``` such that the returned `kv_seq_lens` is [4] instead of [1]? ### repro To repro locally, you can check out https://github.com/vllm-project/vllm/pull/21692 and add the following test case: ``` LocalAttentionTestData( batch_spec=BatchSpec( query_lens=[1], seq_lens=[5], ), attn_chunk_size=4, block_size=2, expected_q_seqlens=[1], expected_k_seqlens=[1], expected_local_block_table=[ [2, 2], ]), ``` ### fix I have a possible fix #21693 but not sure if this is expected. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pag...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: atches](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/utils.py#L271C5-L271C41) used for creating 'virtual' branches for local attn. I noticed that when I choose `q_seq_lens` and `kv_seq_lens`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Local attention chunking edge case when num_blocks == 1? bug ### Your current environment ### 🐛 Describe the bug ### issue In #21692, I'm adding some test cases for [make_local_attention_virtual_batches](https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: onment ### 🐛 Describe the bug ### issue In #21692, I'm adding some test cases for [make_local_attention_virtual_batches](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/utils.py#L271C5-L271C41)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
