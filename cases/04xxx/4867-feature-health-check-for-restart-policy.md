# vllm-project/vllm#4867: [Feature]: Health check for restart policy

| 字段 | 值 |
| --- | --- |
| Issue | [#4867](https://github.com/vllm-project/vllm/issues/4867) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Health check for restart policy

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A small change to get alot of reliability back.... We see vLLM crash or hang in various ways, e.g.: https://github.com/vllm-project/vllm/issues/4108 https://github.com/vllm-project/vllm/issues/4344 And manually managing that is a hassle. vLLM team could easily add a HEALTHCHECK line in the Dockerfile so tools like autoheal can function. https://hub.docker.com/r/willfarrell/autoheal/ https://docs.docker.com/reference/dockerfile/#healthcheck Would looks like: ``` HEALTHCHECK --interval=5m --timeout=10s curl -f http://localhost/health || exit 1 ``` This would allow one to use the other docker image to manage the vLLM images. ### Alternatives Manual labor ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Health check for restart policy feature request;stale ### 🚀 The feature, motivation and pitch A small change to get alot of reliability back.... We see vLLM crash or hang in various ways, e.g.: https://github...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: that is a hassle. vLLM team could easily add a HEALTHCHECK line in the Dockerfile so tools like autoheal can function. https://hub.docker.com/r/willfarrell/autoheal/ https://docs.docker.com/reference/dockerfile/#healthc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: policy feature request;stale ### 🚀 The feature, motivation and pitch A small change to get alot of reliability back.... We see vLLM crash or hang in various ways, e.g.: https://github.com/vllm-project/vllm/issues/4108 h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
