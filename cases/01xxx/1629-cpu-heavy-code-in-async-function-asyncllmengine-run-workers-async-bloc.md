# vllm-project/vllm#1629: CPU heavy code in async function _AsyncLLMEngine._run_workers_async blocks the event loop

| 字段 | 值 |
| --- | --- |
| Issue | [#1629](https://github.com/vllm-project/vllm/issues/1629) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> CPU heavy code in async function _AsyncLLMEngine._run_workers_async blocks the event loop

### Issue 正文摘录

The function _AsyncLLMEngine._run_workers_async executes a function on the workers via `getattr(worker, method)` which is cpu bound and blocks the event loop and requests with fastapi for example can not be optimally served. More specifically, the `_queue` in the created stream object in the following line accumulates a lot of tokens even when reading them as soon as possible leading to the first half of the tokens appearing on the screen one by one and the last half of tokens appearing all almost at the same time once vllm is done handling the request and the event loop is unblocked. https://github.com/vllm-project/vllm/blob/0d578228ca220c120bb73316c1d35d078a5bd7b1/vllm/engine/async_llm_engine.py#L386 I created a [pull request](https://github.com/vllm-project/vllm/pull/1628) to fix this issue by executing the worker functions in a ThreadPoolExecutor.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: etattr(worker, method)` which is cpu bound and blocks the event loop and requests with fastapi for example can not be optimally served. More specifically, the `_queue` in the created stream object in the following line...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d requests with fastapi for example can not be optimally served. More specifically, the `_queue` in the created stream object in the following line accumulates a lot of tokens even when reading them as soon as possible...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: CPU heavy code in async function _AsyncLLMEngine._run_workers_async blocks the event loop The function _AsyncLLMEngine._run_workers_async executes a function on the workers via `getattr(worker, method)` which is cpu bou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
