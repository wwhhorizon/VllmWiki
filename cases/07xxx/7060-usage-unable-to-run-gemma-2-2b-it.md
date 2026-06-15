# vllm-project/vllm#7060: [Usage]: Unable to run `gemma-2-2b-it`

| 字段 | 值 |
| --- | --- |
| Issue | [#7060](https://github.com/vllm-project/vllm/issues/7060) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unable to run `gemma-2-2b-it`

### Issue 正文摘录

### The model to consider. https://huggingface.co/google/gemma-2-2b-it ### The closest model vllm already supports. https://huggingface.co/google/gemma-2-9b-it ### What's your difficulty of supporting the model you want? Faster inference

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Unable to run `gemma-2-2b-it` usage;stale ### The model to consider. https://huggingface.co/google/gemma-2-2b-it ### The closest model vllm already supports. https://huggingface.co/google/gemma-2-9b-it ### What...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Unable to run `gemma-2-2b-it` usage;stale ### The model to consider. https://huggingface.co/google/gemma-2-2b-it ### The closest model vllm already supports. https://huggingface.co/google/gemma-2-9b-it ### What...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Unable to run `gemma-2-2b-it` usage;stale ### The model to consider. https://huggingface.co/google/gemma-2-2b-it ### The closest model vllm already supports. https://huggingface.co/google/gemma-2-9b-it ### What...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
