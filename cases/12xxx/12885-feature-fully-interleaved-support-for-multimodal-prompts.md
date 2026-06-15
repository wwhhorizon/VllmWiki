# vllm-project/vllm#12885: [Feature]: Fully interleaved support for multimodal prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#12885](https://github.com/vllm-project/vllm/issues/12885) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Fully interleaved support for multimodal prompts

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello! Firstly, thank you for such a wonderful library. I am currently developing a custom prompt auto-optimization tool that requires support for multimodal multi-turn conversations. As part of the optimization prompt for teacher model, there will be a section containing examples of student model request processing. The structure of these examples will look something like this: ``` ## Example N ## __ = ... __ = Predicted answer: Ground truth answer: Conclusion: ``` Here: * Each message can be of any role (system, user, assistant) * Variables can represent either text or image data From my understanding of the code [here](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L676) image tokens are currently appended to the beginning of the text prompt ```python def _get_full_multimodal_text_prompt(placeholder_counts: Dict[str, int], text_prompt: str) -> str: """Combine multimodal prompts for a multimodal language model.""" ... ... return "\n".join(missing_placeholders + [text_prompt]) ``` This approach stacks all image tokens together at the start of the prompt, which could potentially impact the performance of the te...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Fully interleaved support for multimodal prompts feature request;unstale ### 🚀 The feature, motivation and pitch Hello! Firstly, thank you for such a wonderful library. I am currently developing a custom prom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Fully interleaved support for multimodal prompts feature request;unstale ### 🚀 The feature, motivation and pitch Hello! Firstly, thank you for such a wonderful library. I am currently developing a custom prom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de, but I am uncertain whether these changes are compatible with all VLM architectures or if they might affect subsequent processing stages: ```python IMAGE_PLACEHOLDER = " " .............. def _get_full_multimodal_text...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: timodal_text_prompt_interleave(placeholder_counts, texts) if interleave else _full_multimodal_text_prompt_simple(placeholder_counts, "\n".join(texts)) ) def _full_multimodal_text_prompt_simple(placeholder_counts: Dict[s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
