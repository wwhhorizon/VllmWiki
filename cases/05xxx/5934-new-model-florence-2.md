# vllm-project/vllm#5934: [New Model]: Florence-2

| 字段 | 值 |
| --- | --- |
| Issue | [#5934](https://github.com/vllm-project/vllm/issues/5934) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Florence-2

### Issue 正文摘录

### The model to consider. https://huggingface.co/microsoft/Florence-2-base ### The closest model vllm already supports. phi-3v , its a vlm ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Florence-2 new-model;unstale ### The model to consider. https://huggingface.co/microsoft/Florence-2-base ### The closest model vllm already supports. phi-3v , its a vlm ### What's your difficulty of support...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Florence-2 new-model;unstale ### The model to consider. https://huggingface.co/microsoft/Florence-2-base ### The closest model vllm already supports. phi-3v , its a vlm ### What's your difficulty of support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
