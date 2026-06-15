# vllm-project/vllm#40846: [RFC]: Rust front-end

| 字段 | 值 |
| --- | --- |
| Issue | [#40846](https://github.com/vllm-project/vllm/issues/40846) |
| 状态 | open |
| 标签 | RFC;rust |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Rust front-end

### Issue 正文摘录

### Motivation vLLM has always had a strong python bias to make it accessible to a wide range of contributors, and to exploit ML libraries including pytorch, triton, etc. Historically, we have managed the inherent performance downsides of python, which include garbage collection and restricted parallelism due to the GIL. The measures taken include resorting to multiprocessing for CPU parallelism, which includes the capability to scale out the API server process. As GPU latency continues to fall, request concurrency grows, and large-scale deployments become the norm, the CPU parts of the system have again become a bottleneck in many situations. This is often seen in the front-end process where the asyncio event loop can’t keep up. Further, our front-end python code has become increasingly complex and fragile as it has evolved organically. With the advent of coding agents, the python vs rust contributor accessibility issue is minimized. It seems the time is right to explore a rust-based alternative to the python front-end process: - It will allow us to eliminate the local api server process scale-out pattern which imposes some awkward limitations and is the source of significant com...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ny situations. This is often seen in the front-end process where the asyncio event loop can’t keep up. Further, our front-end python code has become increasingly complex and fragile as it has evolved organically. With t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ides of python, which include garbage collection and restricted parallelism due to the GIL. The measures taken include resorting to multiprocessing for CPU parallelism, which includes the capability to scale out the API...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ich includes the capability to scale out the API server process. As GPU latency continues to fall, request concurrency grows, and large-scale deployments become the norm, the CPU parts of the system have again become a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s used exactly as before. ## Performance Benchmarks All benchmarks: Qwen3-0.6B, DP=4 on 4x GB200 GPUs, vllm 0.19.0, request_rate=inf. Results shown at concurrency=1024. asc = `--api-server-count`. These is obviously not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: de range of contributors, and to exploit ML libraries including pytorch, triton, etc. Historically, we have managed the inherent performance downsides of python, which include garbage collection and restricted paralleli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
