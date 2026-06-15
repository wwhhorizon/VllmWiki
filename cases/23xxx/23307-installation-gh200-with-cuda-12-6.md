# vllm-project/vllm#23307: [Installation]: GH200 with cuda 12.6

| 字段 | 值 |
| --- | --- |
| Issue | [#23307](https://github.com/vllm-project/vllm/issues/23307) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: GH200 with cuda 12.6

### Issue 正文摘录

### Your current environment Hi there, I wonder for an aarch64 machine, is it possible to install vllm with pytorch 2.6.0+cuda12.6, as I do not have cuda 12.8 in my machine and I cannot successfully install it. Or, must we have cuda 12.8 for aarch 64 machine? Do we have other options? I cannot find it. Any kinds of help will be really appreciated. ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: GH200 with cuda 12.6 installation;stale ### Your current environment Hi there, I wonder for an aarch64 machine, is it possible to install vllm with pytorch 2.6.0+cuda12.6, as I do not have cuda 12.8 in my
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: GH200 with cuda 12.6 installation;stale ### Your current environment Hi there, I wonder for an aarch64 machine, is it possible to install vllm with pytorch 2.6.0+cuda12.6, as I do not have cuda 12.8 in m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: GH200 with cuda 12.6 installation;stale ### Your current environment Hi there, I wonder for an aarch64 machine, is it possible to install vllm with pytorch 2.6.0+cuda12.6, as I do not have cuda 12.8 in m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
