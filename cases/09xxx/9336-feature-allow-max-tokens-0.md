# vllm-project/vllm#9336: [Feature]: Allow max_tokens = 0

| 字段 | 值 |
| --- | --- |
| Issue | [#9336](https://github.com/vllm-project/vllm/issues/9336) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow max_tokens = 0

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like vllm to support sampling parameters with `max_tokens=0`. This would be great to have in a scenario where the log probs of the input prompt are of interest exclusively (using the `prompt_logprobs` parameter). High-level usecases for this are e.g.: * Debugging and analysis * Model comparison * Prompt optimization ### Alternatives _No response_ ### Additional context I gave it a quick try by adjusting [this line](https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py#L367) from ```python if self.max_tokens is not None and self.max_tokens < 1: ``` to ```python if self.max_tokens is not None and self.max_tokens < 0: ``` which seems to work for my use case. In case there are no super complex additional implications by such a change, I'd be happy to raise a PR for this feature request myself. I yet went with this feature request issue ticket in the first place to get your feedback and perspective on this. Looking forward to your response - thanks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pa...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er). High-level usecases for this are e.g.: * Debugging and analysis * Model comparison * Prompt optimization ### Alternatives _No response_ ### Additional context I gave it a quick try by adjusting [this line](https://...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Allow max_tokens = 0 feature request ### 🚀 The feature, motivation and pitch I would like vllm to support sampling parameters with `max_tokens=0`. This would be great to have in a scenario where the log probs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
