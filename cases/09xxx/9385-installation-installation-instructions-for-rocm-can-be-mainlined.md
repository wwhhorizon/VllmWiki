# vllm-project/vllm#9385: [Installation]: Installation instructions for ROCm can be mainlined

| 字段 | 值 |
| --- | --- |
| Issue | [#9385](https://github.com/vllm-project/vllm/issues/9385) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installation instructions for ROCm can be mainlined

### Issue 正文摘录

### Your current environment N/A ### How you are installing vllm https://docs.vllm.ai/en/stable/getting_started/amd-installation.html option 2 The problem is that it says to checkout a very specific commit of triton. Triton just published a new version of 3.1 that has AMD support mainlined but the dependency in the vllm pip package still tries to install 3.0. If someone tells me how I can update the dependency on 3.1 we can simplify the AMD instructions I think. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Installation instructions for ROCm can be mainlined installation;stale ### Your current environment N/A ### How you are installing vllm https://docs.vllm.ai/en/stable/getting_started/amd-installation.ht
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Installation instructions for ROCm can be mainlined installation;stale ### Your current environment N/A ### How you are installing vllm https://docs.vllm.ai/en/stable/getting_started/amd-installation.htm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion 2 The problem is that it says to checkout a very specific commit of triton. Triton just published a new version of 3.1 that has AMD support mainlined but the dependency in the vllm pip package still tries to install...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ation]: Installation instructions for ROCm can be mainlined installation;stale ### Your current environment N/A ### How you are installing vllm https://docs.vllm.ai/en/stable/getting_started/amd-installation.html option...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting triton Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
