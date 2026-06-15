# vllm-project/vllm#7143: [New Model]: Mantis

| 字段 | 值 |
| --- | --- |
| Issue | [#7143](https://github.com/vllm-project/vllm/issues/7143) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Mantis

### Issue 正文摘录

### The model to consider. TIGER-Lab/Mantis-8B-siglip-llama3 https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3 ### The closest model vllm already supports. llava next ### What's your difficulty of supporting the model you want? Siglip model support

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Mantis new-model;unstale ### The model to consider. TIGER-Lab/Mantis-8B-siglip-llama3 https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3 ### The closest model vllm already supports. llava next ### Wha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Mantis new-model;unstale ### The model to consider. TIGER-Lab/Mantis-8B-siglip-llama3 https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3 ### The closest model vllm already supports. llava next ### Wha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
