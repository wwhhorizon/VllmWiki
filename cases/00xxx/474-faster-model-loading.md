# vllm-project/vllm#474: Faster model loading

| 字段 | 值 |
| --- | --- |
| Issue | [#474](https://github.com/vllm-project/vllm/issues/474) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Faster model loading

### Issue 正文摘录

Model loading for vLLM is rather slow. Can we skip parameter initialization to speed up loading model like "low_cpu_mem_usage=True" in HF.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Faster model loading feature request Model loading for vLLM is rather slow. Can we skip parameter initialization to speed up loading model like "low_cpu_mem_usage=True" in HF.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Faster model loading feature request Model loading for vLLM is rather slow. Can we skip parameter initialization to speed up loading model like "low_cpu_mem_usage=True" in HF.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
