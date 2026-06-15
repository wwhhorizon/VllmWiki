# vllm-project/vllm#14764: [RFC]: Schema for checking input shapes for multi-modal models

| 字段 | 值 |
| --- | --- |
| Issue | [#14764](https://github.com/vllm-project/vllm/issues/14764) |
| 状态 | closed |
| 标签 | good first issue;feature request;RFC;multi-modality |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Schema for checking input shapes for multi-modal models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we use `_parse_and_validate_*_input` to validate the multi-modal inputs. However, only minimal checks are being made, with some models only checking the type of the inputs. It is easy for the actual shape of the inputs to not match what is being documented in classes like `*ImagePixelInputs`, confusing model developers and maintainers. To avoid this, I propose adding a base class `TensorSchema` to validate the model inputs. For example: Original code: ```py class Phi3VImagePixelInputs(TypedDict): type: Literal["pixel_values"] data: Union[torch.Tensor, List[torch.Tensor]] """Shape: `(batch_size * num_images, 1 + num_patches, num_channels, height, width)`""" image_sizes: torch.Tensor """Shape: `(batch_size * num_images, 2)`""" ``` The idea: ```py class Phi3VImagePixelInputs(TensorSchema): """ Dimensions: - b: Batch size (number of prompts) - n: Number of images - p: Number of patches - h: Height of each patch - w: Width of each patch """ type: Literal["pixel_values"] = "pixel_values" data: Annotated[Union[torch.Tensor, List[torch.Tensor]], TensorShape("bn", "p", 3, "h", "w")] image_sizes: Annotated[Union[torch.Tensor, List[torch.Ten...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Schema for checking input shapes for multi-modal models good first issue;feature request;RFC;multi-modality ### 🚀 The feature, motivation and pitch Currently, we use `_parse_and_validate_*_input` to validate the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: HF ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: h tensor field with `typing_extensions.Annotated` and use the additional metadata to perform validation. - Can switch to `typing.Annotated` once we drop support for Python 3.9 - Dimensions that are constants can be chec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: or checking input shapes for multi-modal models good first issue;feature request;RFC;multi-modality ### 🚀 The feature, motivation and pitch Currently, we use `_parse_and_validate_*_input` to validate the multi-modal inp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
