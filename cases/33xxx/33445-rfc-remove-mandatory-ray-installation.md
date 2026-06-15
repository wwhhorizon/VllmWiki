# vllm-project/vllm#33445: [RFC] Remove mandatory ray installation

| 字段 | 值 |
| --- | --- |
| Issue | [#33445](https://github.com/vllm-project/vllm/issues/33445) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Remove mandatory ray installation

### Issue 正文摘录

>Requesting changes as this is a breaking change. We should add a deprecation warning for a couple of releases before removing the optional dependency, since it breaks `--distributed-executor-backend ray` >Let's additionally discuss the deprecation in an RFC first + with the community _Originally posted by @tlrmchlsmth in https://github.com/vllm-project/vllm/pull/33351#pullrequestreview-3725573443_ vLLM v1 PP can run via the multiprocessing backend; Ray is only required when users explicitly choose the Ray executor backend. Keeping Ray as a default dependency on CUDA/ROCm causes confusion and unnecessarily pulls Ray into environments that don’t use it.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC] Remove mandatory ray installation >Requesting changes as this is a breaking change. We should add a deprecation warning for a couple of releases before removing the optional dependency, since it breaks `--distribu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tion in an RFC first + with the community _Originally posted by @tlrmchlsmth in https://github.com/vllm-project/vllm/pull/33351#pullrequestreview-3725573443_ vLLM v1 PP can run via the multiprocessing backend; Ray is on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: emoving the optional dependency, since it breaks `--distributed-executor-backend ray` >Let's additionally discuss the deprecation in an RFC first + with the community _Originally posted by @tlrmchlsmth in https://github...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC] Remove mandatory ray installation >Requesting changes as this is a breaking change. We should add a deprecation warning for a couple of releases before removing the optional dependency, since it breaks `--distribu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
