# vllm-project/vllm#11838: [Misc]: Wondering why we checkout from a specific commit of Triton

| 字段 | 值 |
| --- | --- |
| Issue | [#11838](https://github.com/vllm-project/vllm/issues/11838) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | kernel;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Wondering why we checkout from a specific commit of Triton

### Issue 正文摘录

### Anything you want to discuss about vllm. I reviewed the Dockerfile and documentation and noticed that we are building Triton from the commit `e192dba224c673671ae70f73842fc693ca279a45`. Is there a specific reason for using this commit? I ask because, based on my experience, Triton's kernel performance on AMD GPUs is better with vlllm Docker at that commit compared to the newest release. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Misc]: Wondering why we checkout from a specific commit of Triton stale ### Anything you want to discuss about vllm. I reviewed the Dockerfile and documentation and noticed that we are building Triton from the commit `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc]: Wondering why we checkout from a specific commit of Triton stale ### Anything you want to discuss about vllm. I reviewed the Dockerfile and documentation and noticed that we are building Triton from the commit `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Wondering why we checkout from a specific commit of Triton stale ### Anything you want to discuss about vllm. I reviewed the Dockerfile and documentation and noticed that we are building Triton from the commit `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;hardware_porting kernel;triton Anything you want to discuss abou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
