# vllm-project/vllm#29389: [Bug]: race condition in shm_broadcast.py

| 字段 | 值 |
| --- | --- |
| Issue | [#29389](https://github.com/vllm-project/vllm/issues/29389) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: race condition in shm_broadcast.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Problem `ShmRingBuffer` is a lock-free queue, the implementation of which https://github.com/vllm-project/vllm/blob/12c007e288bf5c0ae3bd438036fbafbad88e706b/vllm/distributed/device_communicators/shm_broadcast.py#L98-L153 relies on the fact that when a flag is written to, signalling a valid state, the associated data is also in a valid state. To illustrate the point, consider the program ```python shm = shared_memory.SharedMemory(..., size=128) # set shm to 0 # process 1 shm[0] = 1 shm[64] = 1 # process 2 while shm[64] != 1: pass print(shm[0]) ``` `ShmRingBuffer` requires that `print(shm[0])` always prints `1`. **There is no guarantee this is true**. For this to be true, 1. The Python language/implementation must provide a memory model, which it doesn't. Loosely speaking, a memory model is a set of guarantees on how source code maps to hardware instructions. 2. Even if we assume the source code maps "as intended" to hardware instructions, the hardware must ensure that process 2 must observe the writes to `shm[0]` and `shm[64]` in the same order as process 1. An example of 2 breaking down is given in [`race_condition.cpp`](https:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: race condition in shm_broadcast.py bug;stale ### Your current environment ### 🐛 Describe the bug # Problem `ShmRingBuffer` is a lock-free queue, the implementation of which https://github.com/vllm-project/vllm/bl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: In order of recommendation: 1. Remove `ShmRingBuffer` and always use the fallback `self.local_socket.send(serialized_obj)`. This is the simplest. 2. Use a well-tested lock-free queue implementation and don't write our o...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and crashes vLLM sporadically. Such a crash would be near impossible to reproduce and debug. # Solutions In order of recommendation: 1. Remove `ShmRingBuffer` and always use the fallback `self.local_socket.send(serializ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e fact that when a flag is written to, signalling a valid state, the associated data is also in a valid state. To illustrate the point, consider the program ```python shm = shared_memory.SharedMemory(..., size=128) # se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hould document extensively the proof of its correctness across different architectures. Python provides no tools for lock-free programming, making it impossible to write. CC @youkaichao @nvpohanh ### Before submitting a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
