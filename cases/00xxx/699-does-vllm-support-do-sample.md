# vllm-project/vllm#699: Does vllm support do_sample?

| 字段 | 值 |
| --- | --- |
| Issue | [#699](https://github.com/vllm-project/vllm/issues/699) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vllm support do_sample?

### Issue 正文摘录

Hi, For hugginface, it support various sample strategy: https://huggingface.co/docs/transformers/main/main_classes/text_generation greedy decoding by calling [greedy_search()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.greedy_search) if num_beams=1 and do_sample=False contrastive search by calling [contrastive_search()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.contrastive_search) if penalty_alpha>0. and top_k>1 multinomial sampling by calling [sample()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.sample) if num_beams=1 and do_sample=True beam-search decoding by calling [beam_search()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.beam_search) if num_beams>1 and do_sample=False beam-search multinomial sampling by calling [beam_sample()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.beam_sample) if num_beams>1 and do_sample=True Since vllm already support beam search with b...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Does vllm support do_sample? feature request;unstale Hi, For hugginface, it support various sample strategy: https://huggingface.co/docs/transformers/main/main_classes/text_generation greedy decoding by calling [greedy_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /main/main_classes/text_generation greedy decoding by calling [greedy_search()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.greedy_search) if num_beams=1 an...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ansformers.GenerationMixin.greedy_search) if num_beams=1 and do_sample=False contrastive search by calling [contrastive_search()](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: unstale Hi, For hugginface, it support various sample strategy: https://huggingface.co/docs/transformers/main/main_classes/text_generation greedy decoding by calling [greedy_search()](https://huggingface.co/docs/transfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
