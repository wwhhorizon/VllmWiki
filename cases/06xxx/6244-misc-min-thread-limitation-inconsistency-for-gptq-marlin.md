# vllm-project/vllm#6244: [Misc]: Min thread limitation inconsistency for gptq_marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#6244](https://github.com/vllm-project/vllm/issues/6244) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Min thread limitation inconsistency for gptq_marlin

### Issue 正文摘录

### Anything you want to discuss about vllm. For gptq_marlin, `min_thread_n=64 min_thread_k=64` is required in [https://github.com/vllm-project/vllm/blob/70c232f85a9e83421a4d9ca95e6384364271f2bc/csrc/quantization/gptq_marlin/gptq_marlin.cuh#L22-L23](url), while `min_thread_n=64 min_thread_k=128` is required in [https://github.com/vllm-project/vllm/blob/70c232f85a9e83421a4d9ca95e6384364271f2bc/vllm/model_executor/layers/quantization/utils/marlin_utils.py#L21-L22](url). Why the limitation is different?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: com/vllm-project/vllm/blob/70c232f85a9e83421a4d9ca95e6384364271f2bc/csrc/quantization/gptq_marlin/gptq_marlin.cuh#L22-L23](url), while `min_thread_n=64 min_thread_k=128` is required in [https://github.com/vllm-project/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/70c232f85a9e83421a4d9ca95e6384364271f2bc/vllm/model_executor/layers/quantization/utils/marlin_utils.py#L21-L22](url). Why the limitation is different?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Min thread limitation inconsistency for gptq_marlin stale ### Anything you want to discuss about vllm. For gptq_marlin, `min_thread_n=64 min_thread_k=64` is required in [https://github.com/vllm-project/vllm/blob...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
