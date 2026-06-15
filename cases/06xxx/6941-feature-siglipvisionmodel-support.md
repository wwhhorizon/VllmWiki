# vllm-project/vllm#6941: [Feature]: SiglipVisionModel Support

| 字段 | 值 |
| --- | --- |
| Issue | [#6941](https://github.com/vllm-project/vllm/issues/6941) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: SiglipVisionModel Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Paligemma uses SiglipVisionModel from the transformers library, which can be ported to the vLLM. As CLIPVisionModel is supported for VLMs, the SiglipVisionModel can be supported too. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: SiglipVisionModel Support feature request ### 🚀 The feature, motivation and pitch Paligemma uses SiglipVisionModel from the transformers library, which can be ported to the vLLM. As CLIPVisionModel is support...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: del Support feature request ### 🚀 The feature, motivation and pitch Paligemma uses SiglipVisionModel from the transformers library, which can be ported to the vLLM. As CLIPVisionModel is supported for VLMs, the SiglipVi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: SiglipVisionModel Support feature request ### 🚀 The feature, motivation and pitch Paligemma uses SiglipVisionModel from the transformers library, which can be ported to the vLLM. As CLIPVisionModel is support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
