# vllm-project/vllm#30805: [docker] kv_connectors (lmcache) not installed on arm64 release images

| 字段 | 值 |
| --- | --- |
| Issue | [#30805](https://github.com/vllm-project/vllm/issues/30805) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [docker] kv_connectors (lmcache) not installed on arm64 release images

### Issue 正文摘录

lmcache is silently failing to install on arm64 silently release images because: 1. lmcache has no pre-built arm64 wheels on PyPI (only x86_64) 2. Building from source requires `CUDA_HOME` to be set, which it isn't in the `vllm-base` stage See the logs of the `Build release image (arm64)` stage https://buildkite.com/vllm/release/builds/11213/steps/canvas?sid=019b24b0-0ca0-47d6-a5fc-b787b5476233

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [docker] kv_connectors (lmcache) not installed on arm64 release images installation;stale lmcache is silently failing to install on arm64 silently release images because: 1. lmcache has no pre-built arm64 wheels on PyPI
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t arm64 wheels on PyPI (only x86_64) 2. Building from source requires `CUDA_HOME` to be set, which it isn't in the `vllm-base` stage See the logs of the `Build release image (arm64)` stage https://buildkite.com/vllm/rel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: _connectors (lmcache) not installed on arm64 release images installation;stale lmcache is silently failing to install on arm64 silently release images because: 1. lmcache has no pre-built arm64 wheels on PyPI (only x86_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
