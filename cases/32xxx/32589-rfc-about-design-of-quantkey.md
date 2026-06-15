# vllm-project/vllm#32589: [RFC]: About design of QuantKey

| 字段 | 值 |
| --- | --- |
| Issue | [#32589](https://github.com/vllm-project/vllm/issues/32589) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: About design of QuantKey

### Issue 正文摘录

### Motivation. According to current design, the quant_scheme(per_tensor/per_channel/per_token...) is determined by `GroupShape` like [this](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/quant_utils.py#L42) There might be two problems: 1. The `GroupShape` only defines row and col, what about tensors with more than two dimensions, like weight of Conv? 2. The quant_scheme is implicitly hidden in `GroupShape`, which might not be necessary. Explicitly specifying quant_scheme in `QuantKey` would be easier to understand for users, and letting quant_scheme determine scale_shape or `GroupShape` would be more reasonable ### Proposed Change. 1. Define `QuantSchemeEnum` ```python from enum import Enum class QuantSchemeEnum(Enum): PER_TENSOR = "per_tensor" PER_CHANNEL = "per_channel" PER_TOKEN = "per_token" ``` 2. Insert `QuantSchemeEnum` in `QuantKey` ```python @dataclass(frozen=True) class QuantKey: """ Class for identifying the type of quantization. dtype: quantized data type scale: scale descriptor scale2: second-level scale descriptor symmetric: symmetric if True, asymmetric if False """ dtype: torch.dtype scale: ScaleDesc scale2: ScaleDesc...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: About design of QuantKey RFC;stale ### Motivation. According to current design, the quant_scheme(per_tensor/per_channel/per_token...) is determined by `GroupShape` like [this](https://github.com/vllm-project/vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: re than two dimensions, like weight of Conv? 2. The quant_scheme is implicitly hidden in `GroupShape`, which might not be necessary. Explicitly specifying quant_scheme in `QuantKey` would be easier to understand for use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: l scale descriptor symmetric: symmetric if True, asymmetric if False """ dtype: torch.dtype scale: ScaleDesc scale2: ScaleDesc | None = None symmetric: bool = True quant_scheme: QuantSchemeEnum | None = None ``` 3. When...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: upShape` like [this](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/quant_utils.py#L42) There might be two problems: 1. The `GroupShape` only defines row and col, what about...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
