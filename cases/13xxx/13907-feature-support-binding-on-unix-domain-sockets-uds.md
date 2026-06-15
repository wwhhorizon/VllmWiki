# vllm-project/vllm#13907: [Feature]: support binding on Unix Domain Sockets (UDS)

| 字段 | 值 |
| --- | --- |
| Issue | [#13907](https://github.com/vllm-project/vllm/issues/13907) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support binding on Unix Domain Sockets (UDS)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The vLLM OpenAI-Compatible Server should allow binding on a Unix Domain Socket. This would be more efficient in case you run vLLM behind a reverse proxy on the same machine, compared to using TCP on localhost. Additionally, UDS' are protected by regular unix permissions, meaning other users on the same machine can't connect, given the right permissions. This is useful to lock down access. In my case it would also solve the problem of having to find a "free port" when launching multiple instances of vLLM on the same machine, since you can think of an arbitrary socket name. ### Alternatives _No response_ ### Additional context vLLM uses Uvicorn, which supports unix sockets. https://www.uvicorn.org/settings/#socket-binding > `--uds ` - Bind to a UNIX domain socket, for example --uds /tmp/uvicorn.sock. Useful if you want to run Uvicorn behind a reverse proxy. However, this option is not exposed in `vllm serve`. It would be great to have! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/)...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support binding on Unix Domain Sockets (UDS) feature request;unstale ### 🚀 The feature, motivation and pitch The vLLM OpenAI-Compatible Server should allow binding on a Unix Domain Socket. This would be more...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ver should allow binding on a Unix Domain Socket. This would be more efficient in case you run vLLM behind a reverse proxy on the same machine, compared to using TCP on localhost. Additionally, UDS' are protected by reg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
