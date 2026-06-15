# vllm-project/vllm#9315: [help wanted]: write tests for python-only development 

| 字段 | 值 |
| --- | --- |
| Issue | [#9315](https://github.com/vllm-project/vllm/issues/9315) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [help wanted]: write tests for python-only development 

### Issue 正文摘录

### Anything you want to discuss about vllm. we need to write some tests for python-only development (see https://docs.vllm.ai/en/latest/getting_started/installation.html#python-only-build-without-compilation for details). we can: - git clone the repo; - install the wheel - change some code - test the change - uninstall the python-only installation - check if we can install wheels again ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hon-only development (see https://docs.vllm.ai/en/latest/getting_started/installation.html#python-only-build-without-compilation for details). we can: - git clone the repo; - install the wheel - change some code - test...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ain ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [help wanted]: write tests for python-only development stale ### Anything you want to discuss about vllm. we need to write some tests for python-only development (see https://docs.vllm.ai/en/latest/getting_started/insta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [help wanted]: write tests for python-only development stale ### Anything you want to discuss about vllm. we need to write some tests for python-only development (see https://docs.vllm.ai/en/latest/getting_started/insta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
