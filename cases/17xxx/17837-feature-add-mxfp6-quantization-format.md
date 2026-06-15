# vllm-project/vllm#17837: [Feature]: Add MXFP6 Quantization Format

| 字段 | 值 |
| --- | --- |
| Issue | [#17837](https://github.com/vllm-project/vllm/issues/17837) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add MXFP6 Quantization Format

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We request the addition of a new data format, MXFP6, within the quantization functionality of vLLM. The rationale for this request is that the MXFP6 format offers potentially better precision compared to existing quantization formats, which could lead to improved model performance or quality while maintaining computational efficiency benefits of quantization. https://www.qualcomm.com/developer/blog/2024/01/qualcomm-cloud-ai-100-accelerates-large-language-model-inference-2x-using-microscaling-mx ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add MXFP6 Quantization Format feature request;stale ### 🚀 The feature, motivation and pitch We request the addition of a new data format, MXFP6, within the quantization functionality of vLLM. The rationale fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add MXFP6 Quantization Format feature request;stale ### 🚀 The feature, motivation and pitch We request the addition of a new data format, MXFP6, within the quantization functionality of vLLM. The rationale fo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nale for this request is that the MXFP6 format offers potentially better precision compared to existing quantization formats, which could lead to improved model performance or quality while maintaining computational eff...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e for this request is that the MXFP6 format offers potentially better precision compared to existing quantization formats, which could lead to improved model performance or quality while maintaining computational effici...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Add MXFP6 Quantization Format feature request;stale ### 🚀 The feature, motivation and pitch We request the addition of a new data format, MXFP6, within the quantization functionality of vLLM. The rationale fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
