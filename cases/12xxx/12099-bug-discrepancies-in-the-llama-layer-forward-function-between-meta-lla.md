# vllm-project/vllm#12099: [Bug]: Discrepancies in the llama layer forward function between meta-llama, transformers and vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#12099](https://github.com/vllm-project/vllm/issues/12099) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Discrepancies in the llama layer forward function between meta-llama, transformers and vLLM.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I noticed that there are discrepancies in the forward pass of the attention layer between `llama`, `transformers`, and `vllm` For example, in the `llama` [implementation](https://github.com/meta-llama/llama/blob/v2/llama/model.py#L406): ``` h = x + self.attention.forward( self.attention_norm(x), start_pos, freqs_cis, mask ) out = h + self.feed_forward.forward(self.ffn_norm(h)) return out ``` RMSnorm is applied to the input, then attention is applied, before doing the residual step. Finally, the output is passed through a fully connected step with another RMSnorm normalization, and there's another residual operator before returning it. In the `transformers` [implementation](https://github.com/huggingface/transformers/blob/v4.48.0/src/transformers/models/llama/modeling_llama.py#L327), we see a similar setup. ``` residual = hidden_states hidden_states = self.input_layernorm(hidden_states) # Self Attention hidden_states, self_attn_weights, present_key_value = self.self_attn( hidden_states=hidden_states, attention_mask=attention_mask, position_ids=position_ids, past_key_value=past_key_value,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Discrepancies in the llama layer forward function between meta-llama, transformers and vLLM. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I noticed that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Discrepancies in the llama layer forward function between meta-llama, transformers and vLLM. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I noticed that...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ma layer forward function between meta-llama, transformers and vLLM. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I noticed that there are discrepancies in the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
