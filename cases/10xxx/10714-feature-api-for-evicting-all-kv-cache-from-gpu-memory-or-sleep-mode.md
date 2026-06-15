# vllm-project/vllm#10714: [Feature]: API for evicting all KV cache from GPU memory (or `sleep mode`)

| 字段 | 值 |
| --- | --- |
| Issue | [#10714](https://github.com/vllm-project/vllm/issues/10714) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: API for evicting all KV cache from GPU memory (or `sleep mode`)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It will be great if we have an API to support evicting all KV cache from GPU memory. By mentioning `sleep mode`, I mean, if there are some technical considerations, it's OK to make the vLLM unavailable for inference during this period, until we manually switch back to work by another separate API call. Ideally, the GPU memory usage during this period should be minimal, but the time for it to return back to normal should still be very fast. ### Alternatives Another alternative is to support changing `--gpu-memory-utilization` dynamically. ### Additional context This feature would be a great help for use cases such that, during some periods of the day, the requests for inference are none. We would like to use this period for the GPU to do other GPU computing jobs. Killing the vLLM inference engine would, of course, be a choice here, but it will be a great overhead when the user requests come in again, and we need to bring the vLLM engine back to work, especially if the model is very large and checkpoints loading takes minutes to complete. As a result, it would be a great addition for vLLM if vLLM supports the `sleep mode` (such as evicting all...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: API for evicting all KV cache from GPU memory (or `sleep mode`) feature request;stale ### 🚀 The feature, motivation and pitch It will be great if we have an API to support evicting all KV cache from GPU memor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: API for evicting all KV cache from GPU memory (or `sleep mode`) feature request;stale ### 🚀 The feature, motivation and pitch It will be great if we have an API to support evicting all KV cache from GPU memory. By menti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ts come in again, and we need to bring the vLLM engine back to work, especially if the model is very large and checkpoints loading takes minutes to complete. As a result, it would be a great addition for vLLM if vLLM su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: in, and we need to bring the vLLM engine back to work, especially if the model is very large and checkpoints loading takes minutes to complete. As a result, it would be a great addition for vLLM if vLLM supports the `sl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
