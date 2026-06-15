# vllm-project/vllm#29565: [Bug]: Shared-Memory MessageQueue Uses Unsafe pickle.loads, Leading to Deserialization RCE

| 字段 | 值 |
| --- | --- |
| Issue | [#29565](https://github.com/vllm-project/vllm/issues/29565) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Shared-Memory MessageQueue Uses Unsafe pickle.loads, Leading to Deserialization RCE

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug In `vllm/distributed/device_communicators/shm_broadcast.py`, the `MessageQueue` uses `pickle.dumps()` when enqueueing messages and `pickle.loads()` when dequeueing messages: - `MessageQueue.enqueue()` → uses `pickle.dumps(obj, protocol=HIGHEST_PROTOCOL)` - `MessageQueue.dequeue()` → uses `pickle.loads(all_buffers[0], buffers=all_buffers[1:])` - remote readers also receive payloads via ZeroMQ (`send_multipart` / `recv`) Because `pickle.loads` executes arbitrary Python instructions through `__reduce__` / `__setstate__` mechanisms, this design introduces a **remote code execution (RCE)** risk *whenever IPC data can be influenced by an attacker*. Any malicious process (local or remote) that can write into the shared memory buffer or send multipart messages to the vLLM communication socket can trigger arbitrary code execution in the vLLM runtime. This vulnerability is analogous to known issues in other ML frameworks where model or state files use unsafe pickle loading. ## PoC The following PoC simulates an attacker injecting a malicious pickle message into the shared memory channel. This demonstrates that MessageQueue.dequeue() will...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: E)** risk *whenever IPC data can be influenced by an attacker*. Any malicious process (local or remote) that can write into the shared memory buffer or send multipart messages to the vLLM communication socket can trigge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bitrary Python instructions through `__reduce__` / `__setstate__` mechanisms, this design introduces a **remote code execution (RCE)** risk *whenever IPC data can be influenced by an attacker*. Any malicious process (lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vulnerability is analogous to known issues in other ML frameworks where model or state files use unsafe pickle loading. ## PoC The following PoC simulates an attacker injecting a malicious pickle message into the shared...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Shared-Memory MessageQueue Uses Unsafe pickle.loads, Leading to Deserialization RCE bug ### Your current environment / ### 🐛 Describe the bug In `vllm/distributed/device_communicators/shm_broadcast.py`, the `Mess...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
