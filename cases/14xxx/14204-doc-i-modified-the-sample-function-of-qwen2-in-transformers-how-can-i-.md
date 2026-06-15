# vllm-project/vllm#14204: [Doc]: I modified the _sample function of qwen2 in transformers. How can I quickly make it compatible with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#14204](https://github.com/vllm-project/vllm/issues/14204) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: I modified the _sample function of qwen2 in transformers. How can I quickly make it compatible with vllm?

### Issue 正文摘录

### 📚 The doc issue I modified the _sample function of qwen2 in transformers. How can I quickly make it compatible with vllm? There is a simple example: ```python class Qwen2ForCausalLM(GenerationMixin,Qwen2PreTrainedModel): def generate(***): self._sample(***) def _sample(***): outputs = self.model(**inputs) logits = outputs.logits ### do something for logits to get next token embeds, there is a simple example next_token = torch.argmax(logits, dim=-1) ``` ### Suggest a potential alternative/fix Such as ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: I modified the _sample function of qwen2 in transformers. How can I quickly make it compatible with vllm? documentation;stale ### 📚 The doc issue I modified the _sample function of qwen2 in transformers. How can...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: as ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nsformers. How can I quickly make it compatible with vllm? documentation;stale ### 📚 The doc issue I modified the _sample function of qwen2 in transformers. How can I quickly make it compatible with vllm? There is a sim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
