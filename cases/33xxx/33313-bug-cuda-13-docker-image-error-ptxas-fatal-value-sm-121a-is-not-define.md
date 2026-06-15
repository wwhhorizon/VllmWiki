# vllm-project/vllm#33313: [Bug]: cuda 13 docker image  error  "ptxas fatal   : Value 'sm_121a' is not defined for option 'gpu-name'"

| 字段 | 值 |
| --- | --- |
| Issue | [#33313](https://github.com/vllm-project/vllm/issues/33313) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cuda 13 docker image  error  "ptxas fatal   : Value 'sm_121a' is not defined for option 'gpu-name'"

### Issue 正文摘录

for docker image vllm/vllm-openai:v0.14.1-cu130 at Dg x-spark Triton rises ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name' which is closed bug https://github.com/triton-lang/triton/issues/8539

## 现有链接修复摘要

#34822 [Bugfix] Add is_blackwell_class() for SM121/GB10 DGX Spark support

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: cuda 13 docker image error "ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name'" bug;stale for docker image vllm/vllm-openai:v0.14.1-cu130 at Dg x-spark Triton rises ptxas fatal : Value 'sm_121a'
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: cuda 13 docker image error "ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name'" bug;stale for docker image vllm/vllm-openai:v0.14.1-cu130 at Dg x-spark Triton rises ptxas fatal : Value 'sm_121a' i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ug;stale for docker image vllm/vllm-openai:v0.14.1-cu130 at Dg x-spark Triton rises ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name' which is closed bug https://github.com/triton-lang/triton/issues/853...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: txas fatal : Value 'sm_121a' is not defined for option 'gpu-name'" bug;stale for docker image vllm/vllm-openai:v0.14.1-cu130 at Dg x-spark Triton rises ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name'...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34822](https://github.com/vllm-project/vllm/pull/34822) | mentioned | 0.6 | [Bugfix] Add is_blackwell_class() for SM121/GB10 DGX Spark support | ecific paths - Get non-Blackwell backend priorities Related: #31740, #33313 ### Changes 1. **`vllm/platforms/interface.py`**: Add `is_blackwell_capability()` `@staticmethod` (take… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
