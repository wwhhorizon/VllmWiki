# vllm-project/vllm#30193: [Bug]: Behavioral Difference in hidden_states[-1] between vLLM and Transformers for Qwen3VLForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#30193](https://github.com/vllm-project/vllm/issues/30193) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Behavioral Difference in hidden_states[-1] between vLLM and Transformers for Qwen3VLForConditionalGeneration

### Issue 正文摘录

### Your current environment - vLLM Version: 0.11.2 - Transformers Version: 4.57 - Model: Qwen3VLForConditionalGeneration ### 🐛 Describe the bug I have observed an inconsistency in the output of the forward method for the `Qwen3VLForConditionalGeneration` class between vLLM (version 0.11.2) and Transformers (version 4.57). In the Transformers library, the last hidden state (`outputs.hidden_states[0, -1, :]`) returned is before the final layer normalization. However, in vLLM, the returned hidden_states appears to be after the normalization is applied. Is this discrepancy an unintended bug, or is there a configuration option in vLLM to control this output behavior (e.g., to return the pre-norm hidden states)? I don't have minimal demo, but I change the origin code to test. Because the`forward` method of `Qwen3VLForConditionalGeneration` has the following code: ```python hidden_states = self.language_model.model( input_ids=input_ids, positions=positions, intermediate_tensors=intermediate_tensors, inputs_embeds=inputs_embeds, # args for deepstack deepstack_input_embeds=deepstack_input_embeds, ) ``` The type of `self.language_model.model` is `Qwen3LLMModel`. I introduced an environment...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vioral Difference in hidden_states[-1] between vLLM and Transformers for Qwen3VLForConditionalGeneration bug ### Your current environment - vLLM Version: 0.11.2 - Transformers Version: 4.57 - Model: Qwen3VLForConditiona...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Qwen3VLForConditionalGeneration bug ### Your current environment - vLLM Version: 0.11.2 - Transformers Version: 4.57 - Model: Qwen3VLForConditionalGeneration ### 🐛 Describe the bug I have observed an inconsistency in th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: den states)? I don't have minimal demo, but I change the origin code to test. Because the`forward` method of `Qwen3VLForConditionalGeneration` has the following code: ```python hidden_states = self.language_model.model(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
