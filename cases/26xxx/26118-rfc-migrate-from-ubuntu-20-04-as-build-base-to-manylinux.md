# vllm-project/vllm#26118: [RFC]: Migrate from Ubuntu 20.04 as Build Base to manylinux

| 字段 | 值 |
| --- | --- |
| Issue | [#26118](https://github.com/vllm-project/vllm/issues/26118) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Migrate from Ubuntu 20.04 as Build Base to manylinux

### Issue 正文摘录

### Motivation. Recently we are fighting CI fires as Python 3.12 is no longer is deadsnakes repository for focal 20.04. But we also cannot migrate to 22 due to glibc compat issue (found by @mgoin and @tlrmchlsmth). ### Proposed Change. I would say the choice of ubuntu as build base as largely been a historical artifact of how we started the base image. It's entirely ok to switch to manylinux if we can get the toolchain together functioning well. We should follow what PyTorch does, also pay attention to other accelerators (AMD, CPU, etc) along with ARM compatibility for Grace CPU. ### Feedback Period. 1wk ### CC List. @huydhn @seemethere @tlrmchlsmth @mgoin @DarkLight1337 @dougbtv @khluu ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: Migrate from Ubuntu 20.04 as Build Base to manylinux RFC;unstale ### Motivation. Recently we are fighting CI fires as Python 3.12 is no longer is deadsnakes repository for focal 20.04. But we also cannot migrate...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: not migrate to 22 due to glibc compat issue (found by @mgoin and @tlrmchlsmth). ### Proposed Change. I would say the choice of ubuntu as build base as largely been a historical artifact of how we started the base image....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Migrate from Ubuntu 20.04 as Build Base to manylinux RFC;unstale ### Motivation. Recently we are fighting CI fires as Python 3.12 is no longer is deadsnakes repository for focal 20.04. But we also cannot migrate...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build attention build_error env_dependency Motivati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
