# vllm-project/vllm#21432: [Bug]: After online_serving disagg_example_p2p_nccl_xpyd.sh cleanup, there is a zombie process

| 字段 | 值 |
| --- | --- |
| Issue | [#21432](https://github.com/vllm-project/vllm/issues/21432) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After online_serving disagg_example_p2p_nccl_xpyd.sh cleanup, there is a zombie process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh ``` running: ``` root@huawei:/workspace# ps -ef UID PID PPID C STIME TTY TIME CMD root 1 0 0 01:00 pts/0 00:00:00 /bin/bash root 156 0 0 01:01 pts/1 00:00:00 bash root 87417 0 0 06:39 pts/2 00:00:00 bash root 87906 156 0 06:40 pts/1 00:00:00 bash disagg_example_p2p_nccl_xpyd.sh root 88121 87906 0 06:40 pts/1 00:00:00 python3 disagg_proxy_p2p_nccl_xpyd.py root 88122 87906 24 06:40 pts/1 00:00:17 /usr/bin/python /usr/local/bin/vllm serve /workspace/mo root 88123 87906 24 06:40 pts/1 00:00:17 /usr/bin/python /usr/local/bin/vllm serve /workspace/mo root 88124 87906 28 06:40 pts/1 00:00:20 /usr/bin/python /usr/local/bin/vllm serve /workspace/mo root 88125 87906 25 06:40 pts/1 00:00:17 /usr/bin/python /usr/local/bin/vllm serve /workspace/mo root 89254 88122 0 06:41 pts/1 00:00:00 /usr/bin/python -c from multiprocessing.resource_tracke root 89255 88122 99 06:41 pts/1 00:01:55 /usr/bin/python -c from multiprocessing.spawn import sp root 89364 88125 0 06:41 pts/1 00:00:00 /usr/bin/python -c from multiprocessing.resource_tracke root 89365 8...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e 311, in bind super().bind(addr) File "_zmq.py", line 917, in zmq.backend.cython._zmq.Socket.bind File "_zmq.py", line 179, in zmq.backend.cython._zmq._check_rc zmq.error.ZMQError: Address already in use (addr='tcp://0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 99 06:41 pts/1 00:01:55 /usr/bin/python -c from multiprocessing.spawn import sp root 89364 88125 0 06:41 pts/1 00:00:00 /usr/bin/python -c from multiprocessing.resource_tracke root 89365 88125 99 06:41 pts/1 00:01:47 /u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: /disagg_proxy_p2p_nccl_xpyd.py", line 85, in start_service_discovery router_socket.bind(f"tcp://{hostname}:{port}") File "/usr/local/lib/python3.12/dist-packages/zmq/sugar/socket.py", line 311, in bind super().bind(addr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
