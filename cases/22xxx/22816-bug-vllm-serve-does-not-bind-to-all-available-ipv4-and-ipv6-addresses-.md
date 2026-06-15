# vllm-project/vllm#22816: [Bug]: vllm serve does not bind to all available ipv4 and ipv6 addresses when --host is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#22816](https://github.com/vllm-project/vllm/issues/22816) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm serve does not bind to all available ipv4 and ipv6 addresses when --host is empty

### Issue 正文摘录

### Your current environment At HEAD ### 🐛 Describe the bug In environments with a dual stack configuration (such as a Kubernetes pod on a [standard dual-stack enabled cluster](https://kubernetes.io/docs/concepts/services-networking/dual-stack/), like GKE), the `--host` empty option only binds `vllm serve` to the first address. This is due to [create_server_socket](https://github.com/vllm-project/vllm/blob/bdc8f9fce64cc876d18de6c019a1e78cae8c2189/vllm/entrypoints/openai/api_server.py#L1763-L1764) which only creates a single socket, whereas `asyncio.create_server()` will [return an list of addresses when `None` is passed as the `host`](https://github.com/python/cpython/blob/70730ad0414e4661d2e94710d865edf1f7f164a1/Lib/asyncio/base_events.py#L1575) (the "node" in the underlying C getaddrinfo) and bind one socket to each address. Generally the expected default behavior of a server program when binding to "all addresses" as represented by the empty hostname is to bind to all addresses as returned by getaddrinfo, which would include all valid IPv4/IPv6 names in a multi-homed (to allow more ports) or dual-stack environment. To be consistent with this expectation, `create_server_socket`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _server.py#L1763-L1764) which only creates a single socket, whereas `asyncio.create_server()` will [return an list of addresses when `None` is passed as the `host`](https://github.com/python/cpython/blob/70730ad0414e466...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rn. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ment At HEAD ### 🐛 Describe the bug In environments with a dual stack configuration (such as a Kubernetes pod on a [standard dual-stack enabled cluster](https://kubernetes.io/docs/concepts/services-networking/dual-stack...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t bind to all available ipv4 and ipv6 addresses when --host is empty bug;stale ### Your current environment At HEAD ### 🐛 Describe the bug In environments with a dual stack configuration (such as a Kubernetes pod on a [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
