# vllm-project/vllm#17199: [Feature]: Inflight BNB quantization for Mixtral models

| 字段 | 值 |
| --- | --- |
| Issue | [#17199](https://github.com/vllm-project/vllm/issues/17199) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Inflight BNB quantization for Mixtral models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to be able to use in-flight BNB quantization of Mixtral models like `mistralai/Mixtral-8x7B-Instruct-v0.1` with `--quantization bitsandbytes`. It currently doesn't work on vllm 0.8.4. ### Alternatives _No response_ ### Additional context Since https://github.com/vllm-project/vllm/pull/2673 a hacky workaround has been implemented to be able to use quantization with Mixtral models [here](https://github.com/vllm-project/vllm/blob/v0.8.4/vllm/model_executor/model_loader/utils.py#L88-L97) `bitsandbytes` is not part of the list of mixtral-supported quantization methods, so vllm falls back to the `QuantMixtralForCausalLM` (`MixtralForCausalLM` from `mixtral_quant.py`) implementation which doesn't rely on fused moe. But weights loading with BitsAndBytes later fails [here](https://github.com/vllm-project/vllm/blob/v0.8.4/vllm/model_executor/model_loader/loader.py#L1131) with ``` AttributeError: Model MixtralForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. ``` `MixtralForCausalLM` from `mixtral_quant.py` does indeed not have the `packed_modules_mapping` attribute. I tried two things: - adding...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Inflight BNB quantization for Mixtral models feature request;stale ### 🚀 The feature, motivation and pitch I would like to be able to use in-flight BNB quantization of Mixtral models like `mistralai/Mixtral-8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Inflight BNB quantization for Mixtral models feature request;stale ### 🚀 The feature, motivation and pitch I would like to be able to use in-flight BNB quantization of Mixtral models like `mistralai/Mixtral-8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: yer ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: salLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. ``` `MixtralForCausalLM` from `mixtral_quant.py` does indeed not have the `packed_modules_mapping` attribute. I tried two things:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Inflight BNB quantization for Mixtral models feature request;stale ### 🚀 The feature, motivation and pitch I would like to be able to use in-flight BNB quantization of Mixtral models like `mistralai/Mixtral-8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
