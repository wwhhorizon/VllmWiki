# vllm-project/vllm#14151: [Bug]: Structured output requests can hang the server

| 字段 | 值 |
| --- | --- |
| Issue | [#14151](https://github.com/vllm-project/vllm/issues/14151) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Structured output requests can hang the server

### Issue 正文摘录

### Your current environment This isn't version specific, the use of a `ThreadPoolExecutor` to build grammars for structured output has been around since the original `outlines` integration ### 🐛 Describe the bug To build structured output (guided decoding) processors in vLLM, we currently either: - Execute the non-async grammar creation right in the event loop, or - Use a ThreadPoolExectuor to run the grammar creation in a separate thread However, there are cases where a user may pass in a json schema for structured output that will cause grammar compilation to take a really long time. One such case reported with outlines is here: https://github.com/dottxt-ai/outlines-core/issues/180, and we've had many reports from products with >1k line json schemas input as guided decoding parameters that exhibit this behavior. The problem is that we don't have a way to cancel the construction of these grammars when the api request times out or is cancelled. Specifically when using the threadpool, the task that is waiting on the future from the pool will correctly cancel when the client disconnects but the thread that's doing the work in the pool will continue spinning. This causes a situation...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: he server bug;structured-output ### Your current environment This isn't version specific, the use of a `ThreadPoolExecutor` to build grammars for structured output has been around since the original `outlines` integrati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Structured output requests can hang the server bug;structured-output ### Your current environment This isn't version specific, the use of a `ThreadPoolExecutor` to build grammars for structured output has been ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: regarding the structured output work for V1: https://vllm-dev.slack.com/archives/C07QQ8DAXMK/p1741024399466749 This might be worth fixing in V0 as well, depending on how fast we can actually get V1 out ### Before submit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
