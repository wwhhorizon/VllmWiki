# vllm-project/vllm#14281: [Usage]: How to bypass multimodal processor logic when inputs are already processed

| 字段 | 值 |
| --- | --- |
| Issue | [#14281](https://github.com/vllm-project/vllm/issues/14281) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to bypass multimodal processor logic when inputs are already processed

### Issue 正文摘录

### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom multimodal model to generate content from text/image/audio inputs. But, in most cases, the generate request contains processed content like this: ```python TokensPrompt( prompt_token_ids=[xxx], # tensor of token ids multi_modal_data={ "image": { "pixel_values": xxx, "image_grid_thw": xxx, }, "audio": { "audio_values": xxx, "audio_attention_masks": xxx, }, }, ) ``` The prompt token ids are already expanded with the feature size of the multimodal content. I'm trying to write a processor modified from qwen2_5_vl and don't know how to bypass processor (including prompt replacements). I have tested the code in batch size 1, but failed in larger batch size (with enable_chunked_prefill and enforce_eager True). The error occurs when decoding the second token and indicates that input_ids contains length of one image feature, but mm_inputs contains pixel_values of two images. I'm trying to find a way to completely bypass the processor when inputs are already processed. Some code reference: ```python def _field_config(hf_inputs: Mapping[str, torch.Tensor]): image_gr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to bypass multimodal processor logic when inputs are already processed usage ### Your current environment ```text vllm 0.7.3 transformers 4.49.0 ``` ### How would you like to use vllm I'm writing a custom m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e content from text/image/audio inputs. But, in most cases, the generate request contains processed content like this: ```python TokensPrompt( prompt_token_ids=[xxx], # tensor of token ids multi_modal_data={ "image": {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: processed. Some code reference: ```python def _field_config(hf_inputs: Mapping[str, torch.Tensor]): image_grid_thw = hf_inputs.get("image_grid_thw", torch.empty((0, 3))) image_grid_sizes = image_grid_thw.prod(-1) return...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 't know how to bypass processor (including prompt replacements). I have tested the code in batch size 1, but failed in larger batch size (with enable_chunked_prefill and enforce_eager True). The error occurs when decodi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
