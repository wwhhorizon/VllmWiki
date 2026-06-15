# vllm-project/vllm#23203: [Feature]: Support gpt-oss mxfp4 on compute capability 7.5

| 字段 | 值 |
| --- | --- |
| Issue | [#23203](https://github.com/vllm-project/vllm/issues/23203) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support gpt-oss mxfp4 on compute capability 7.5

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `transformers` v4.55.2 includes support for mxfp4 on compute capability 7.5: https://github.com/huggingface/transformers/pull/39940 However, vllm currently requires compute capability 8.0 to enable mxfp4: https://github.com/vllm-project/vllm/blob/e61bac87eefdcee02f524b8379b310a276fd73f4/vllm/model_executor/layers/quantization/mxfp4.py#L75-L76 I believe it should now be possible to relax this requirement to 7.5, allowing gpt-oss to run on older GPUs (e.g. a Nvidia T4) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Support gpt-oss mxfp4 on compute capability 7.5 feature request;stale ### 🚀 The feature, motivation and pitch `transformers` v4.55.2 includes support for mxfp4 on compute capability 7.5: https://github.com/hu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support gpt-oss mxfp4 on compute capability 7.5 feature request;stale ### 🚀 The feature, motivation and pitch `transformers` v4.55.2 includes support for mxfp4 on compute capability 7.5: https://github.com/hu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support gpt-oss mxfp4 on compute capability 7.5 feature request;stale ### 🚀 The feature, motivation and pitch `transformers` v4.55.2 includes support for mxfp4 on compute capability 7.5: https://github.com/hu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support gpt-oss mxfp4 on compute capability 7.5 feature request;stale ### 🚀 The feature, motivation and pitch `transformers` v4.55.2 includes support for mxfp4 on compute capability 7.5: https://github.com/hu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
