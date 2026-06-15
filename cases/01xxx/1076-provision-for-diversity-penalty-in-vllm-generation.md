# vllm-project/vllm#1076: Provision for `diversity_penalty` in vLLM generation?

| 字段 | 值 |
| --- | --- |
| Issue | [#1076](https://github.com/vllm-project/vllm/issues/1076) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Provision for `diversity_penalty` in vLLM generation?

### Issue 正文摘录

Is there a way to reproduce results to huggingface's generation with the parameter `diversity_penalty` present [here](https://huggingface.co/docs/transformers/v4.33.2/en/main_classes/text_generation#transformers.GenerationConfig.diversity_penalty). `diversity_penalty` helps to generate diversity in the output when using `beam_search`. The current implementation of vLLM doesn't allow for this and returns similar outputs across all of its beams. Is there a method to replicate something similar with vLLM?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sity_penalty` in vLLM generation? Is there a way to reproduce results to huggingface's generation with the parameter `diversity_penalty` present [here](https://huggingface.co/docs/transformers/v4.33.2/en/main_classes/te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Provision for `diversity_penalty` in vLLM generation? Is there a way to reproduce results to huggingface's generation with the parameter `diversity_penalty` present [here](https://huggingface.co/docs/transformers/v4.33....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty_penalty` helps to generate diversity in the output when using `beam_search`. The current implementation of vLLM doesn't allow for this and returns similar outputs across all of its beams. Is there a method to replica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
