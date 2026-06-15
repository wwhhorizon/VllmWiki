# vllm-project/vllm#5912: [Feature]: Support for google/gemma-2-9b-it / gemma-2-27b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#5912](https://github.com/vllm-project/vllm/issues/5912) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for google/gemma-2-9b-it / gemma-2-27b-it

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be nice to have support for the new Gemma 2 models: https://huggingface.co/collections/google/gemma-2-release-667d6600fd5220e7b967f315 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support for google/gemma-2-9b-it / gemma-2-27b-it feature request ### 🚀 The feature, motivation and pitch It would be nice to have support for the new Gemma 2 models: https://huggingface.co/collections/google...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support for google/gemma-2-9b-it / gemma-2-27b-it feature request ### 🚀 The feature, motivation and pitch It would be nice to have support for the new Gemma 2 models: https://huggingface.co/collections/google...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for google/gemma-2-9b-it / gemma-2-27b-it feature request ### 🚀 The feature, motivation and pitch It would be nice to have support for the new Gemma 2 models: https://huggingface.co/collections/google...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
