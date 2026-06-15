# vllm-project/vllm#32136: [Bug]: When DP head node crash but headless node can't automatic stop

| 字段 | 值 |
| --- | --- |
| Issue | [#32136](https://github.com/vllm-project/vllm/issues/32136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When DP head node crash but headless node can't automatic stop

### Issue 正文摘录

### Your current environment Use nightly image. ### 🐛 Describe the bug When I run deepseek v3.2 using TP2+DP16, the vllm on the headless node cannot exit automatically. After the vllm on the head node exits, the headless node will continuously print error logs and cannot recover automatically. Furthermore, even if the head dp service is restarted, the headless service cannot be automatically restored. ``` [rank30]:[W111 00:54:10.905768298 TCPStore.cpp:125] [c10d] recvValue failed on SocketImpl(fd=99, addr=[::ffff:172.16.21.245]:38760, remote=[::ffff:172.16.11.34]:42643): Failed to recv, got 0 bytes. Connection was likely closed. Did the remote server shutdown or crash? Exception raised from recvBytes at /pytorch/torch/csrc/distributed/c10d/Utils.hpp:682 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocator >) + 0x80 (0x7fdc5697cb80 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #1: + 0x5ffc5d1 (0x7fdc3992f5d1 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #2: + 0x5ffd9cd (0x7fdc399309cd in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #3:...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: dbdd49fc88 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: + 0xdc253 (0x7fdc5774a253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: + 0x94ac3 (0x7fdc57933ac3 in /usr/lib/x86_64-l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 1, as it's simpler to implement and doesn't introduce many problems. To reproduce the issue: 1. Start a DP head process. 2. Start another headless process. 3. After both processes start successfully, manually stop the D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: When DP head node crash but headless node can't automatic stop bug;stale ### Your current environment Use nightly image. ### 🐛 Describe the bug When I run deepseek v3.2 using TP2+DP16, the vllm on the headless nod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
