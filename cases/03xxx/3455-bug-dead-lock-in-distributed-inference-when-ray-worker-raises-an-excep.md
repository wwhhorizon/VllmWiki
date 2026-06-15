# vllm-project/vllm#3455: [Bug]: Dead lock in distributed inference when ray worker raises an exception

| 字段 | 值 |
| --- | --- |
| Issue | [#3455](https://github.com/vllm-project/vllm/issues/3455) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dead lock in distributed inference when ray worker raises an exception

### Issue 正文摘录

### Your current environment Any distributed inference tasks with ray currently suffer from this issue. ### 🐛 Describe the bug ## Basic background of `ray` `ray` provides an easy-to-use asynchronous execution framework: ```python def f(): print(1) import ray ray.init() marked_function = ray.remote(f) # mark `f` as a remote function that can be asynchronously executed handle = marked_function.remote() # schedule a worker to asynchronously execute the function, immediately return a handle result = ray.get(handle) # synchronously wait for the worker to finish and return the result ``` The way it deals with `Exception` is noteworthy, see comments in the below: ```python def f(): print(1) raise RuntimeError("test") # the following line will not be executed print(2) import ray ray.init() marked_function = ray.remote(f) # mark `f` as a remote function that can be asynchronously executed handle = marked_function.remote() # schedule a worker to asynchronously execute the function, immediately return a handle # ... do other work in the meantime ... # the main process will not be notified if the worker fails # only when we call `ray.get` will we be notified of the error result = ray.get(hand...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -use asynchronous execution framework: ```python def f(): print(1) import ray ray.init() marked_function = ray.remote(f) # mark `f` as a remote function that can be asynchronously executed handle = marked_function.remot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ad lock in distributed inference when ray worker raises an exception bug;stale ### Your current environment Any distributed inference tasks with ray currently suffer from this issue. ### 🐛 Describe the bug ## Basic back...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ncoment this line to see a deadlock dist.init_process_group( backend="gloo", init_method=distributed_init_method, world_size=world_size, rank=rank, ) tensor = torch.zeros(1) dist.all_reduce(tensor, op=dist.ReduceOp.SUM)...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ibuted inference, i.e. creating process group to collaborate. A minimal reproducible example looks like this: ```python import torch import torch.distributed as dist def f(rank, world_size, distributed_init_method): # r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cause deadlock. In my case, my GPU driver has some problem, and `torch.cuda.set_device` raises an exception, causing the deadlock. ## Solution to be discussed Any suggestion to fix this is welcome. Might be related: htt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
