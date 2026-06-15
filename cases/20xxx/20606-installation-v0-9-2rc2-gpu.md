# vllm-project/vllm#20606: [Installation]: v0.9.2rc2占用更高的gpu显存

| 字段 | 值 |
| --- | --- |
| Issue | [#20606](https://github.com/vllm-project/vllm/issues/20606) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: v0.9.2rc2占用更高的gpu显存

### Issue 正文摘录

### Your current environment 运行qwen3的嵌入和重排模型，发现v0.9.2rc2占用更高的gpu显存，有没有优化的方法？ ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: v0.9.2rc2占用更高的gpu显存 installation;stale ### Your current environment 运行qwen3的嵌入和重排模型，发现v0.9.2rc2占用更高的gpu显存，有没有优化的方法？ ### How you are installing vllm _No response_ ### Before submitting a new issue... -
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : v0.9.2rc2占用更高的gpu显存 installation;stale ### Your current environment 运行qwen3的嵌入和重排模型，发现v0.9.2rc2占用更高的gpu显存，有没有优化的方法？ ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure yo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: v0.9.2rc2占用更高的gpu显存 installation;stale ### Your current environment 运行qwen3的嵌入和重排模型，发现v0.9.2rc2占用更高的gpu显存，有没有优化的方法？ ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
