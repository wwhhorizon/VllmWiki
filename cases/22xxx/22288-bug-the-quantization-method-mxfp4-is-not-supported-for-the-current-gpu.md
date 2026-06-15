# vllm-project/vllm#22288: [Bug]: The quantization method mxfp4 is not supported for the current GPU SM75

| 字段 | 值 |
| --- | --- |
| Issue | [#22288](https://github.com/vllm-project/vllm/issues/22288) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The quantization method mxfp4 is not supported for the current GPU SM75

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ollama run gpt-oss:120b is ok, but vllm runs fail. if mxfp4 not support sm75, why ollama can run very well ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: The quantization method mxfp4 is not supported for the current GPU SM75 bug;stale ### Your current environment ### 🐛 Describe the bug ollama run gpt-oss:120b is ok, but vllm runs fail. if mxfp4 not support sm75,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Bug]: The quantization method mxfp4 is not supported for the current GPU SM75 bug;stale ### Your current environment ### 🐛 Describe the bug ollama run gpt-oss:120b is ok, but vllm runs fail. if mxfp4 not support sm75, w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: SM75 bug;stale ### Your current environment ### 🐛 Describe the bug ollama run gpt-oss:120b is ok, but vllm runs fail. if mxfp4 not support sm75, why ollama can run very well ### Before submitting a new issue... - [x] Ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: quantization method mxfp4 is not supported for the current GPU SM75 bug;stale ### Your current environment ### 🐛 Describe the bug ollama run gpt-oss:120b is ok, but vllm runs fail. if mxfp4 not support sm75, why ollama...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
