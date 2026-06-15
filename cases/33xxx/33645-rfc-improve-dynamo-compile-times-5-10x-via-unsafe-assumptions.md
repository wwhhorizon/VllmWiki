# vllm-project/vllm#33645: [RFC]: Improve Dynamo compile times 5-10x via unsafe assumptions

| 字段 | 值 |
| --- | --- |
| Issue | [#33645](https://github.com/vllm-project/vllm/issues/33645) |
| 状态 | open |
| 标签 | RFC;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Improve Dynamo compile times 5-10x via unsafe assumptions

### Issue 正文摘录

### Motivation. Dynamo graph capture is around half of the total compilation time (for llama3.1 70B and glm-4.7-fp8 after https://github.com/vllm-project/vllm/pull/33641). I think this proposal can make the Dynamo graph capture time 5-10x faster (or more). ### Proposed Change. - Most vLLM decoder forward passes are the same Transformer block repeated N times. - Today, Dynamo traces through the N Transformer blocks to capture a forward graph. - We add a new decorator (maybe needs PyTorch changes), called "unsafe_dynamo_once". - When Dynamo sees an nn.Module with `unsafe_dynamo_once`, it will only trace through it the first time it sees a module, and for all subsequent times, it will just assume that the trace it acquired the first time is correct and copy-paste the original trace N times. - We go around auditing models in vLLM and adding `unsafe_dynamo_once` decorators where appropriate. That is, we must declare that the Transformer block each model uses is actually safe to Dynamo trace once and repeat multiple times. This is obviously unsafe. But I think that after a vLLM model has been released, the model source code itself doesn't change. Only the kernels really change. So it se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Dynamo graph capture is around half of the total compilation time (for llama3.1 70B and glm-4.7-fp8 after https://github.com/vllm-project/vllm/pull/33641). I think this proposal can make the Dynamo graph capture time 5-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rove Dynamo compile times 5-10x via unsafe assumptions RFC;torch.compile;stale ### Motivation. Dynamo graph capture is around half of the total compilation time (for llama3.1 70B and glm-4.7-fp8 after https://github.com...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Improve Dynamo compile times 5-10x via unsafe assumptions RFC;torch.compile;stale ### Motivation. Dynamo graph capture is around half of the total compilation time (for llama3.1 70B and glm-4.7-fp8 after https://...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: around half of the total compilation time (for llama3.1 70B and glm-4.7-fp8 after https://github.com/vllm-project/vllm/pull/33641). I think this proposal can make the Dynamo graph capture time 5-10x faster (or more). ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
