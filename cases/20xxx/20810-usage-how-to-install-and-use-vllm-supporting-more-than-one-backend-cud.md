# vllm-project/vllm#20810: [Usage]: How to install and use vllm supporting more than one backend(CUDA and CPU)?

| 字段 | 值 |
| --- | --- |
| Issue | [#20810](https://github.com/vllm-project/vllm/issues/20810) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to install and use vllm supporting more than one backend(CUDA and CPU)?

### Issue 正文摘录

### Your current environment I don't think it matters. ### How would you like to use vllm I want to support both CUDA and CPU backends when installing vllm, and use some logic to decide whether to use CUDA or CPU for LLM inference at runtime. Is this possible at present? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: How to install and use vllm supporting more than one backend(CUDA and CPU)? usage;stale ### Your current environment I don't think it matters. ### How would you like to use vllm I want to support both CUDA and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: How to install and use vllm supporting more than one backend(CUDA and CPU)? usage;stale ### Your current environment I don't think it matters. ### How would you like to use vllm I want to support both CUDA and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: How to install and use vllm supporting more than one backend(CUDA and CPU)? usage;stale ### Your current environment I don't think it matters. ### How would you like to use vllm I want to support both CUDA and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: stall and use vllm supporting more than one backend(CUDA and CPU)? usage;stale ### Your current environment I don't think it matters. ### How would you like to use vllm I want to support both CUDA and CPU backends when...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development hardware_porting cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
