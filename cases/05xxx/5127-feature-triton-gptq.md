# vllm-project/vllm#5127: [Feature]: Triton GPTQ

| 字段 | 值 |
| --- | --- |
| Issue | [#5127](https://github.com/vllm-project/vllm/issues/5127) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | quantization;triton |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Triton GPTQ

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 1. Hope to support the implementation of triton gptq, similar to tgi ( https://github.com/huggingface/text-generation-inference) 2. There are some differences between the implementation of this PR (https://github.com/huggingface/text-generation-inference/pull/1370/files ) and the implementation of gptq in vllm. It seems that the performance of gptq int4 is better in the range [4,50] for **m** on rocm. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: he implementation of gptq in vllm. It seems that the performance of gptq int4 is better in the range [4,50] for **m** on rocm. ### Alternatives _No response_ ### Additional context _No response_ performance frontend_api...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Triton GPTQ feature request;stale ### 🚀 The feature, motivation and pitch 1. Hope to support the implementation of triton gptq, similar to tgi ( https://github.com/huggingface/text-generation-inference) 2. Th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Triton GPTQ feature request;stale ### 🚀 The feature, motivation and pitch 1. Hope to support the implementation of triton gptq, similar to tgi ( https://github.com/huggingface/text-generation-inference) 2. Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the performance of gptq int4 is better in the range [4,50] for **m** on rocm. ### Alternatives _No response_ ### Additional context _No response_ performance frontend_api;hardware_porting;quantization quantization;trito...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t the implementation of triton gptq, similar to tgi ( https://github.com/huggingface/text-generation-inference) 2. There are some differences between the implementation of this PR (https://github.com/huggingface/text-ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
