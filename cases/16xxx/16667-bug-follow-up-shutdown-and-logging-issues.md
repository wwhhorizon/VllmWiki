# vllm-project/vllm#16667: [Bug]: Follow-up shutdown and logging issues

| 字段 | 值 |
| --- | --- |
| Issue | [#16667](https://github.com/vllm-project/vllm/issues/16667) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Follow-up shutdown and logging issues

### Issue 正文摘录

### 🐛 Describe the bug This issue is a parking lot for edge-cases related to shutdown and logging which will require additional changes in order to be handled correctly by vLLM v1, even after #11737 lands. The goal is that when vLLM shuts down - whether intentionally or due to an internal failure - the cause of shutdown should be logged with a useful level of detail, and the server's resources (especially GPU memory) should be freed. * Process monitor for engine core process. #11737 adds this for the TP workers but currently I don't think things will shut down cleanly if you kill the engine core proc without warning. * A bug not addressed by #11737 : when an `LLM` instance is created with multiprocessing disabled, deleting the `LLM` instance using `del` does not free the engine's weight memory on the GPU, resulting in OOM errors for subsequent tests. This appears to happen because the in-process engine core client does not free weight memory as part of shutdown. It may also be the case that the worker does have any logic for explicitly deleting the PyTorch model layers. In contrast, with multiprocessing enabled, GPU weight memory is freed when the worker process(es) get killed. *...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ror during utility call, error during abort, handle errors in IPC mechanisms ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom righ...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ed with a useful level of detail, and the server's resources (especially GPU memory) should be freed. * Process monitor for engine core process. #11737 adds this for the TP workers but currently I don't think things wil...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: be logged with a useful level of detail, and the server's resources (especially GPU memory) should be freed. * Process monitor for engine core process. #11737 adds this for the TP workers but currently I don't think thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: that the worker does have any logic for explicitly deleting the PyTorch model layers. In contrast, with multiprocessing enabled, GPU weight memory is freed when the worker process(es) get killed. * While #11737 mostly a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Follow-up shutdown and logging issues bug;stale ### 🐛 Describe the bug This issue is a parking lot for edge-cases related to shutdown and logging which will require additional changes in order to be handled corre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
