# vllm-project/vllm#30295: [Installation]: download wheel by commit：not found

| 字段 | 值 |
| --- | --- |
| Issue | [#30295](https://github.com/vllm-project/vllm/issues/30295) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: download wheel by commit：not found

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh wget https://wheels.vllm.ai/dc839ad03d31104c8ebcb0b8f5a75021f1796760/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl ``` not found ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: download wheel by commit：not found installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh wget https://wheels.vllm.ai/dc8
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: und ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: download wheel by commit：not found installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh wget https://wheels.vllm.ai/dc83...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
