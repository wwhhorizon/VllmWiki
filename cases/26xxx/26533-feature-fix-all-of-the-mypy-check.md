# vllm-project/vllm#26533: [Feature]: Fix all of the mypy check

| 字段 | 值 |
| --- | --- |
| Issue | [#26533](https://github.com/vllm-project/vllm/issues/26533) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Fix all of the mypy check

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks for the context from @hmellor ! A following up issue for https://github.com/vllm-project/vllm/pull/26448 Now in `vllm-source/tools/pre_commit/mypy.py`, several directories are checked with `mypy` in isolation with import following skipped: ```bash SEPARATE_GROUPS = [ "tests", # v0 related "vllm/attention", "vllm/compilation", "vllm/engine", "vllm/inputs", "vllm/lora", "vllm/model_executor", "vllm/plugins", "vllm/worker", # v1 related "vllm/v1/attention", "vllm/v1/executor", "vllm/v1/kv_offload", "vllm/v1/metrics", "vllm/v1/pool", "vllm/v1/sample", "vllm/v1/spec_decode", "vllm/v1/structured_output", ] ``` V0 related is not that important since we will deprecate all of them soon, but v1 is strongly needed. This won't break pre-commit CI because all the files in each directory are checked, so no imports need following. However, if you only edit one file locally, the `pre-commit` check will only run on that file and the imports will not be followed. This may cause the pre-commit check to fail locally. We can gradually fix all of the `SEPARATE_GROUPS` to `FILES` to solve the issue throughly ## Instructions Move code like `"vllm/v1/executor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /mypy.py`, several directories are checked with `mypy` in isolation with import following skipped: ```bash SEPARATE_GROUPS = [ "tests", # v0 related "vllm/attention", "vllm/compilation", "vllm/engine", "vllm/inputs", "v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Fix all of the mypy check feature request ### 🚀 The feature, motivation and pitch Thanks for the context from @hmellor ! A following up issue for https://github.com/vllm-project/vllm/pull/26448 Now in `vllm-s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: related "vllm/v1/attention", "vllm/v1/executor", "vllm/v1/kv_offload", "vllm/v1/metrics", "vllm/v1/pool", "vllm/v1/sample", "vllm/v1/spec_decode", "vllm/v1/structured_output", ] ``` V0 related is not that important sinc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ation", "vllm/engine", "vllm/inputs", "vllm/lora", "vllm/model_executor", "vllm/plugins", "vllm/worker", # v1 related "vllm/v1/attention", "vllm/v1/executor", "vllm/v1/kv_offload", "vllm/v1/metrics", "vllm/v1/pool", "vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: olation with import following skipped: ```bash SEPARATE_GROUPS = [ "tests", # v0 related "vllm/attention", "vllm/compilation", "vllm/engine", "vllm/inputs", "vllm/lora", "vllm/model_executor", "vllm/plugins", "vllm/work...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
