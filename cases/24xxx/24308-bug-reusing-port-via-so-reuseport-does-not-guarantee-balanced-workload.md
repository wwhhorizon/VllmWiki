# vllm-project/vllm#24308: [Bug]: Reusing port via `SO_REUSEPORT` does not guarantee balanced workload

| 字段 | 值 |
| --- | --- |
| Issue | [#24308](https://github.com/vllm-project/vllm/issues/24308) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Reusing port via `SO_REUSEPORT` does not guarantee balanced workload

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug The newer vLLM could run multiple api servers + engine clients to parallelize request processing. It is implemented by reusing port by multiple processes: https://github.com/vllm-project/vllm/blob/e599e2c65ee32abcc986733ab0a55becea158bb4/vllm/entrypoints/openai/api_server.py#L1856-L1866 However, due to the low-level mechanism of socket, this implementation could not guarantee the workload is balanced for all processes. (Especially for requests from same source) I perform a comparison between vLLM's implementation and my own implementation: Use NGINX as a load balancer and multiple api server workers listen to different ports. Under vLLM's implementation, I find only 3-4 processes handle almost all requests while other processes are spare. This may lead to blocking when there are too many concurrent requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s/openai/api_server.py#L1856-L1866 However, due to the low-level mechanism of socket, this implementation could not guarantee the workload is balanced for all processes. (Especially for requests from same source) I perf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Reusing port via `SO_REUSEPORT` does not guarantee balanced workload bug;stale ### Your current environment N/A ### 🐛 Describe the bug The newer vLLM could run multiple api servers + engine clients to parallelize reques...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion could not guarantee the workload is balanced for all processes. (Especially for requests from same source) I perform a comparison between vLLM's implementation and my own implementation: Use NGINX as a load balancer...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: le almost all requests while other processes are spare. This may lead to blocking when there are too many concurrent requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
