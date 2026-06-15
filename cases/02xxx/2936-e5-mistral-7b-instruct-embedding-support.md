# vllm-project/vllm#2936: E5-mistral-7b-instruct embedding support

| 字段 | 值 |
| --- | --- |
| Issue | [#2936](https://github.com/vllm-project/vllm/issues/2936) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> E5-mistral-7b-instruct embedding support

### Issue 正文摘录

Hi :) I noticed in the [roadmap](https://github.com/vllm-project/vllm/issues/2681) that embedding support is intended, and was wondering whether it includes llms such as mistral as well. Specifically, [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruct) has the added benefit of including only the adapter in the HF repo. so in this case we could deploy a single pod for both inference as well as truly SOTA embedding without added costs. I assume it would be easier to implement since decoder only architectures are already supported. I think [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruct) the tweak should be to add a function LLMEngine that would take the last hidden state rather than sample on the output yes? if so, i could try and add the pr myself please let me know if theres anything i could do to help.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cludes llms such as mistral as well. Specifically, [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruct) has the added benefit of including only the adapter in the HF repo. so in th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and was wondering whether it includes llms such as mistral as well. Specifically, [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruct) has the added benefit of including only the a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: dded costs. I assume it would be easier to implement since decoder only architectures are already supported. I think [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruct) the tweak...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing without added costs. I assume it would be easier to implement since decoder only architectures are already supported. I think [e5_mistral](https://huggingface.co/intfloat/e5-mistral-7b-instruct#e5-mistral-7b-instruc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
