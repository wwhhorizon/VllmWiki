# vllm-project/vllm#427: NCCL Error 5: invalid usage

| 字段 | 值 |
| --- | --- |
| Issue | [#427](https://github.com/vllm-project/vllm/issues/427) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NCCL Error 5: invalid usage

### Issue 正文摘录

multi-GPU offline inference And When I try to run multi-GPU offline inference, it returns an error: the actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors. The actor never ran - it was cancelled before it started running. Unhandled exception: St13runtime_error. what(): NCCL Error 5: invalid usage the detail error log: cat /tmp/ray/session_latest/logs/python-core-worker-02e363d59eb469c6fe7c4719cfdd04158e231ad34605def092aacdb1_42067.log [2023-07-11 15:20:05,144 I 42067 42067] core_worker_process.cc:107: Constructing CoreWorkerProcess. pid: 42067 [2023-07-11 15:20:05,145 I 42067 42067] io_service_pool.cc:35: IOServicePool is running with 1 io_service. [2023-07-11 15:20:05,147 I 42067 42067] grpc_server.cc:140: worker server started, listening on port 43292. [2023-07-11 15:20:05,151 I 42067 42067] core_worker.cc:217: Initializing worker at a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 7-11 15:20:41,788 E 42067 42067] logging.cc:104: Stack trace: /home/sysdocker/miniconda2/envs/fashchat_env/lib/python3.8/site-packages/ray/_raylet.so(+0xdc551a) [0x7f7f16a1d51a] ray::operator () /home/sysdocker/minicond...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 253] core_worker.cc:553: Event stats: Global stats: 12 total (8 active) Queueing time: mean = 5.740 us, max = 49.684 us, min = 6.046 us, total = 68.876 us Execution time: mean = 11.391 us, total = 136.696 us Event stats...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: CCL Error 5: invalid usage the detail error log: cat /tmp/ray/session_latest/logs/python-core-worker-02e363d59eb469c6fe7c4719cfdd04158e231ad34605def092aacdb1_42067.log [2023-07-11 15:20:05,144 I 42067 42067] core_worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: iconda2/envs/fashchat_env/lib/python3.8/site-packages/torch/lib/libtorch_cuda.so(_ZN4c10d16ProcessGroupNCCL14allreduce_implERSt6vectorIN2at6TensorESaIS3_EERKNS_16AllreduceOptionsE+0x21) [0x7f4f27ae9e31] c10d::ProcessGro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: b/libtorch_python.so(+0x3b7040) [0x7f4f65f48040] pybind11::cpp_function::dispatcher() ray::Worker.__init__(PyCFunction_Call+0x52) [0x4f5652] PyCFunction_Call ray::Worker.__init__(_PyObject_MakeTpCall+0x3bb) [0x4e0c8b] _...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
