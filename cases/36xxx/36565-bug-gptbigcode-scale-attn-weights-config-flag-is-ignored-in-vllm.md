# vllm-project/vllm#36565: [Bug]: GPTBigCode scale_attn_weights config flag is ignored in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#36565](https://github.com/vllm-project/vllm/issues/36565) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPTBigCode scale_attn_weights config flag is ignored in vLLM

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug Hi, following up on the discussion in #35402. I noticed that the current implementation of GPTBigCode in vLLM appears to ignore the scale_attn_weights configuration option. In vllm/model_executor/models/gpt_bigcode.py, the attention scaling is always applied as 1 / sqrt(head_dim): https://github.com/vllm-project/vllm/blob/e5ff140216272c529261b02b6fd13fc480713735/vllm/model_executor/models/gpt_bigcode.py#L75 However, in the HuggingFace Transformers implementation, this scaling depends on the scale_attn_weights flag in the config: ``` self.scale_attn_weights = config.scale_attn_weights self.scaling = self.head_dim**-0.5 if config.scale_attn_weights else 1.0 ``` As a result, models that rely on scale_attn_weights=False may produce different logits compared with Transformers. It might be worth checking whether the GPTBigCode implementation in vLLM should respect the scale_attn_weights config to maintain behavior parity with Transformers. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPTBigCode scale_attn_weights config flag is ignored in vLLM bug ### Your current environment None ### 🐛 Describe the bug Hi, following up on the discussion in #35402. I noticed that the current implementation of...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: GPTBigCode scale_attn_weights config flag is ignored in vLLM bug ### Your current environment None ### 🐛 Describe the bug Hi, following up on the discussion in #35402. I noticed that the current implementation of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: self.scaling = self.head_dim**-0.5 if config.scale_attn_weights else 1.0 ``` As a result, models that rely on scale_attn_weights=False may produce different logits compared with Transformers. It might be worth checking...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
