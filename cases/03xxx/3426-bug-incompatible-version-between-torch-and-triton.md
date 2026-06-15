# vllm-project/vllm#3426: [Bug]: Incompatible version between torch and triton

| 字段 | 值 |
| --- | --- |
| Issue | [#3426](https://github.com/vllm-project/vllm/issues/3426) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incompatible version between torch and triton

### Issue 正文摘录

### 🐛 Describe the bug ERROR: torch 2.1.2 has requirement triton==2.1.0; platform_system == "Linux" and platform_machine == "x86_64", but you'll have triton 2.2.0 which is incompatible.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Incompatible version between torch and triton bug;stale ### 🐛 Describe the bug ERROR: torch 2.1.2 has requirement triton==2.1.0; platform_system == "Linux" and platform_machine == "x86_64", but you'll have triton...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Incompatible version between torch and triton bug;stale ### 🐛 Describe the bug ERROR: torch 2.1.2 has requirement triton==2.1.0; platform_system == "Linux" and platform_machine == "x86_64", but you'll have triton...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Incompatible version between torch and triton bug;stale ### 🐛 Describe the bug ERROR: torch 2.1.2 has requirement triton==2.1.0; platform_system == "Linux" and platform_machine == "x86_64", but you'll have triton...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
