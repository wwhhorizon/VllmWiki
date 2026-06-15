# vllm-project/vllm#4743: [RFC]: Support specifying quant_config details in the LLM or Server entrypoints

| 字段 | 值 |
| --- | --- |
| Issue | [#4743](https://github.com/vllm-project/vllm/issues/4743) |
| 状态 | closed |
| 标签 | feature request;RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support specifying quant_config details in the LLM or Server entrypoints

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Background: With the recent support for `deepspeedfp` quantization introduced in https://github.com/vllm-project/vllm/pull/4652 and https://github.com/vllm-project/vllm/pull/4690, a new issue has emerged due to the nature of the runtime quantization implementation. This implementation allows users to load an unquantized model and enable the quantization argument to reduce the memory footprint required for loading the model. However, the main challenge lies in the fact that the `deepspeedfp` implementation has a parameter `num_bits` that supports quantizing the weights down to either 8 or 6 bits, with the default value set to 8. ### Problem Statement: Currently, if a user wants to apply `quantization="deepspeedfp"`, vLLM will only be able to quantize the model to `num_bits=8` since that is the default value. The only way to change this behavior is by providing a `quant_config.json` file that explicitly defines the desired value for `num_bits`. This limitation restricts users from easily customizing the quantization settings without modifying the configuration file. ### Proposed Solution: To address this issue, we propose adding a new argu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Support specifying quant_config details in the LLM or Server entrypoints feature request;RFC;stale ### 🚀 The feature, motivation and pitch ### Background: With the recent support for `deepspeedfp` quantization in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: specifying quant_config details in the LLM or Server entrypoints feature request;RFC;stale ### 🚀 The feature, motivation and pitch ### Background: With the recent support for `deepspeedfp` quantization introduced in htt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Support specifying quant_config details in the LLM or Server entrypoints feature request;RFC;stale ### 🚀 The feature, motivation and pitch ### Background: With the recent support for `deepspeedfp` quantization in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [RFC]: Support specifying quant_config details in the LLM or Server entrypoints feature request;RFC;stale ### 🚀 The feature, motivation and pitch ### Background: With the recent support for `deepspeedfp` quantization in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
