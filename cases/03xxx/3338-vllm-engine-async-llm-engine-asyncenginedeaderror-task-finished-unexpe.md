# vllm-project/vllm#3338: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause.

| 字段 | 值 |
| --- | --- |
| Issue | [#3338](https://github.com/vllm-project/vllm/issues/3338) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause.

### Issue 正文摘录

afol-apiserver-72b-1 | (RayWorkerVllm pid=3779) [E ProcessGroupNCCL.cpp:475] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=16487777, OpType=ALLREDUCE, NumelIn=195911680, NumelOut=19591168 0, Timeout(ms)=1800000) ran for 1800203 milliseconds before timing out. afol-apiserver-72b-1 | (RayWorkerVllm pid=3779) [E ProcessGroupNCCL.cpp:475] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=9388506, OpType=BROADCAST, NumelIn=1, NumelOut=1, Timeout(ms)=18 00000) ran for 1800222 milliseconds before timing out. afol-apiserver-72b-1 | [E ProcessGroupNCCL.cpp:475] [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=9388514, OpType=BROADCAST, NumelIn=1, NumelOut=1, Timeout(ms)=1800000) ran for 1800872 mi lliseconds before timing out. afol-apiserver-72b-1 | [E ProcessGroupNCCL.cpp:489] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data. afol-apiserver-72b-1 | [E ProcessGroupNCCL.cpp:495] To avoid data inconsistency, we are taking the entire process down. afol-apiserver-72b-1 | [E ProcessGroupNCCL.cpp:916] [Rank 0] NCCL watc...

## 现有链接修复摘要

#5173 bug fixed: cuda out of memory lead to 'AsyncEngineDeadError: Background loop has errored already.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: afol-apiserver-72b-1 | all_outputs = await asyncio.gather(*coros) afol-apiserver-72b-1 | File "/usr/lib/python3.10/concur
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: numba.core.typeconv._typeconv, numba._helperlib, numba._dynfunc, numba._dispatcher, numba.core.runtime._nrt_python, numba.np.ufunc._internal, numba.experimental.jitclass._box, markupsafe._speedups, cupy_backends.cuda.ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 72b-1 | File "/workspace/vllm/worker/worker.py", line 209, in execute_model afol-apiserver-72b-1 | broadcast_tensor_dict(data, src=0) afol-apiserver-72b-1 | File "/workspace/vllm/model_executor/parallel_utils/communicat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ase open an issue on Github. See stack trace above for the actual cause. stale afol-apiserver-72b-1 | (RayWorkerVllm pid=3779) [E ProcessGroupNCCL.cpp:475] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: a.pinned_memory, cupy_backends.cuda.libs.curand, cupy_backends.cuda.libs.profiler, cupy.cuda.common, cupy.cuda.cub, cupy_backends.cuda.libs.nvtx, cupy.cuda.thrust, cupy._core._dtype, cupy._core._scalar, cupy._core._acce...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5173](https://github.com/vllm-project/vllm/pull/5173) | closes_keyword | 0.95 | bug fixed: cuda out of memory lead to 'AsyncEngineDeadError: Background loop has errored already. | FIX #3338 FIX #4879 FIX #5784 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
