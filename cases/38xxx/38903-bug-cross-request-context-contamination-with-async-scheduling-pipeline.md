# vllm-project/vllm#38903: [Bug]: Cross-request context contamination with async scheduling + pipeline parallelism on multi-node

| 字段 | 值 |
| --- | --- |
| Issue | [#38903](https://github.com/vllm-project/vllm/issues/38903) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cross-request context contamination with async scheduling + pipeline parallelism on multi-node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary When running vLLM with **pipeline parallelism (PP > 1) and async scheduling enabled on a multi-node setup**, responses from one user's request can contain **chunks of another user's context**. This is a cross-request data leakage issue — not a hallucination or nondeterminism problem. The leaked content includes identifiable information (e.g., local file paths containing usernames) that is private to other concurrent users, confirming actual data contamination. The issue can be **avoided by disabling async scheduling** (`--no-async-scheduling`), and **does not occur on v0.15.1 or earlier**. ### Reproduction conditions **Affected configuration:** - Multi-node: 2 nodes, 8 GPUs each - `--pipeline-parallel-size 2` - `--tensor-parallel-size 8` - `--distributed-executor-backend mp` - Async scheduling enabled (default in v0.16.0+) - 2+ concurrent users sending requests continuously (~30 minutes) **Not affected when:** - `--no-async-scheduling` is specified - vLLM v0.15.1 or v0.14.0 is used - Single-node setup ### Models tested Both models below exhibit the issue under the affected configuration: - `moonshotai/Kimi-K2.5` - `za...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ser's context**. This is a cross-request data leakage issue — not a hallucination or nondeterminism problem. The leaked content includes identifiable information (e.g., local file paths containing usernames) that is pri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -request context contamination with async scheduling + pipeline parallelism on multi-node bug ### Your current environment ### 🐛 Describe the bug ### Summary When running vLLM with **pipeline parallelism (PP > 1) and as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on or nondeterminism problem. The leaked content includes identifiable information (e.g., local file paths containing usernames) that is private to other concurrent users, confirming actual data contamination. The issue...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Cross-request context contamination with async scheduling + pipeline parallelism on multi-node bug ### Your current environment ### 🐛 Describe the bug ### Summary When running vLLM with **pipeline parallelism (PP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -parallel-size 2` - `--tensor-parallel-size 8` - `--distributed-executor-backend mp` - Async scheduling enabled (default in v0.16.0+) - 2+ concurrent users sending requests continuously (~30 minutes) **Not affected when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
