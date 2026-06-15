# vllm-project/vllm#29591: [Bug] RuntimeError: Cannot re-initialize CUDA in forked subprocess when using lmcache/kv_cache_sharing_lmcache_v1

| 字段 | 值 |
| --- | --- |
| Issue | [#29591](https://github.com/vllm-project/vllm/issues/29591) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] RuntimeError: Cannot re-initialize CUDA in forked subprocess when using lmcache/kv_cache_sharing_lmcache_v1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug environment： 1）Nvidia A100 2）vLLM v0.11.0 3）Python 3.12.11 python3 ./kv_cache_sharing_lmcache_v1.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] RuntimeError: Cannot re-initialize CUDA in forked subprocess when using lmcache/kv_cache_sharing_lmcache_v1 bug;stale ### Your current environment ### 🐛 Describe the bug environment： 1）Nvidia A100 2）vLLM v0.11.0 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: asked questions. development attention_kv_cache attention;cuda crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in forked subprocess when using lmcache/kv_cache_sharing_lmcache_v1 bug;stale ### Your current environment ### 🐛 Describe the bug environment： 1）Nvidia A100 2）vLLM v0.11.0 3）Python 3.12.11 python3 ./kv_cache_sharing_lmc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache attention;cuda crash env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
