# vllm-project/vllm#6479: [New Model]: Codestral Mamba

| 字段 | 值 |
| --- | --- |
| Issue | [#6479](https://github.com/vllm-project/vllm/issues/6479) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Codestral Mamba

### Issue 正文摘录

### The model to consider. Mamba Codestral: https://huggingface.co/mistralai/mamba-codestral-7B-v0.1 Highlights: - SOTA 7B code model - theoretically unlimited context length; tested up to 256k - inference is linear-complexity with respect to sequence length, compared to transformers which is quadratic-complexity ### The closest model vllm already supports. Jamba seems to be the closest model, since it is Mamba-based: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/jamba.py ### What's your difficulty of supporting the model you want? Mamba is a non-transformer architecture, but there is already a mamba-based model supported, so it's unclear how difficult it would be to support.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Codestral Mamba new-model;unstale ### The model to consider. Mamba Codestral: https://huggingface.co/mistralai/mamba-codestral-7B-v0.1 Highlights: - SOTA 7B code model - theoretically unlimited context leng...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: difficulty of supporting the model you want? Mamba is a non-transformer architecture, but there is already a mamba-based model supported, so it's unclear how difficult it would be to support.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Codestral Mamba new-model;unstale ### The model to consider. Mamba Codestral: https://huggingface.co/mistralai/mamba-codestral-7B-v0.1 Highlights: - SOTA 7B code model - theoretically unlimited context leng...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ghlights: - SOTA 7B code model - theoretically unlimited context length; tested up to 256k - inference is linear-complexity with respect to sequence length, compared to transformers which is quadratic-complexity ### The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
