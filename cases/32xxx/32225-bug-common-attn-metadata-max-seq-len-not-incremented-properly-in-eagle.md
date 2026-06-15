# vllm-project/vllm#32225: [Bug]: `common_attn_metadata.max_seq_len` not incremented properly in Eagle implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#32225](https://github.com/vllm-project/vllm/issues/32225) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `common_attn_metadata.max_seq_len` not incremented properly in Eagle implementation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In Eagle implementation of speculative decoding we increment `common_attn_metadata.seq_lens` by 1 everytime we speculate an additional token with the Eagle head, however, we don't increment `common_attn_metadata.max_seq_len` which may lead to incorrect metadata. This incorrect data may lead to issues in attention implementations that rely on `max_seq_len`. E.g. in the implementation of IPEX, `max_seq_len` is used to trim the `block_table` https://github.com/intel/intel-extension-for-pytorch/blob/7259fd81b92d77ee1da273a3bdba72d675b703a2/intel_extension_for_pytorch/transformers/models/xpu/fusions/mha_fusion.py#L596 the implementation for XPU trims the `block_table` according to `max_seq_len` so when the length of the sequence required an additional block for the cache XPU didn't see the new block since the `max_seq_len` wasn't updated. ### Solution A possible solution is to increment `max_seq_len` or finding the max after updating the `seq_lens` here: https://github.com/vllm-project/vllm/blob/a307ac073432d3f224c58a54d363fa93f6a659f4/vllm/v1/spec_decode/eagle.py#L466 As far as I could tell, there isn't anything relying on the curren...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: `common_attn_metadata.max_seq_len` not incremented properly in Eagle implementation bug ### Your current environment ### 🐛 Describe the bug In Eagle implementation of speculative decoding we increment `common_att...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rrent environment ### 🐛 Describe the bug In Eagle implementation of speculative decoding we increment `common_attn_metadata.seq_lens` by 1 everytime we speculate an additional token with the Eagle head, however, we don'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ett ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 92d77ee1da273a3bdba72d675b703a2/intel_extension_for_pytorch/transformers/models/xpu/fusions/mha_fusion.py#L596 the implementation for XPU trims the `block_table` according to `max_seq_len` so when the length of the sequ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
