# vllm-project/vllm#1729: Download model from GCP storage bucket instead of huggingface

| 字段 | 值 |
| --- | --- |
| Issue | [#1729](https://github.com/vllm-project/vllm/issues/1729) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Download model from GCP storage bucket instead of huggingface

### Issue 正文摘录

Is there any way to specify model location from gcp storage bucket instead of huggingface repo? (--model)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Download model from GCP storage bucket instead of huggingface Is there any way to specify model location from gcp storage bucket instead of huggingface repo? (--model)
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el from GCP storage bucket instead of huggingface Is there any way to specify model location from gcp storage bucket instead of huggingface repo? (--model)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
