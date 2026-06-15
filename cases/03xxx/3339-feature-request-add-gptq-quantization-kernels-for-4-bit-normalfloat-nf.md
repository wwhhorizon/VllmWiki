# vllm-project/vllm#3339: [Feature Request] Add GPTQ quantization kernels for 4-bit NormalFloat (NF4) use cases.

| 字段 | 值 |
| --- | --- |
| Issue | [#3339](https://github.com/vllm-project/vllm/issues/3339) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Add GPTQ quantization kernels for 4-bit NormalFloat (NF4) use cases.

### Issue 正文摘录

Earlier, there was an awesome PR https://github.com/vllm-project/vllm/pull/2330 on supporting for 2/3/8-bit GPTQ Quantization Models. Would it be possible to integrate 4-bit NormalFloat (NF4)?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature Request] Add GPTQ quantization kernels for 4-bit NormalFloat (NF4) use cases. stale Earlier, there was an awesome PR https://github.com/vllm-project/vllm/pull/2330 on supporting for 2/3/8-bit GPTQ Quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature Request] Add GPTQ quantization kernels for 4-bit NormalFloat (NF4) use cases. stale Earlier, there was an awesome PR https://github.com/vllm-project/vllm/pull/2330 on supporting for 2/3/8-bit GPTQ Quantization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm-project/vllm/pull/2330 on supporting for 2/3/8-bit GPTQ Quantization Models. Would it be possible to integrate 4-bit NormalFloat (NF4)?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
