# vllm-project/vllm#8359: [Feature]: Conditional Prompt Inclusion in `generate` Function for Streaming Efficiency

| 字段 | 值 |
| --- | --- |
| Issue | [#8359](https://github.com/vllm-project/vllm/issues/8359) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Conditional Prompt Inclusion in `generate` Function for Streaming Efficiency

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Title: Conditional Prompt Inclusion in `generate` Function for Streaming Efficiency **Feature Proposal:** This feature introduces a new parameter, `is_return_prompt`, to the `generate` function in `vllm/entrypoints/api_server.py`. The parameter allows users to conditionally include the prompt in the generated response, addressing inefficiencies observed in streaming scenarios. **Motivation and Pitch:** In the current implementation, the `generate` function always includes the prompt in its response, whether streaming is enabled or not. This results in inefficiencies, especially in streaming mode, where the prompt is repeatedly included with each token update. This behavior can be redundant and slow down the processing, as users typically do not need to see the prompt after it has been provided to the LLM. **Proposal:** The proposed feature will add an `is_return_prompt` parameter to the `generate` function. When `is_return_prompt` is set to `False` (the default), the prompt will not be included in the response. When set to `True`, the prompt will be included as part of the output. This will make the streaming process more efficient and r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Prompt Inclusion in `generate` Function for Streaming Efficiency feature request;stale ### 🚀 The feature, motivation and pitch ### Title: Conditional Prompt Inclusion in `generate` Function for Streaming Efficiency **Fe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ]: Conditional Prompt Inclusion in `generate` Function for Streaming Efficiency feature request;stale ### 🚀 The feature, motivation and pitch ### Title: Conditional Prompt Inclusion in `generate` Function for Streaming...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enerate` function, especially in scenarios involving continuous or large-scale text generation. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rameter to the `generate` function. When `is_return_prompt` is set to `False` (the default), the prompt will not be included in the response. When set to `True`, the prompt will be included as part of the output. This w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
