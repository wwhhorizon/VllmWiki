# vllm-project/vllm#44123: [Bug]: Negative max_num_scheduled_tokens bypasses validation (guard gated behind speculative decoding) → bare AssertionError in the scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#44123](https://github.com/vllm-project/vllm/issues/44123) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Negative max_num_scheduled_tokens bypasses validation (guard gated behind speculative decoding) → bare AssertionError in the scheduler

### Issue 正文摘录

### Your current environment Found by bounded model checking (ESBMC-Python - https://github.com/esbmc/esbmc) and confirmed with a behavioral reproduction on real vLLM config objects (below), in the same vein as #43521 / #43532 / #43842 / #43985. The reachability caveat is stated up front: this field is **not CLI-settable**, so this is a lower-severity, integrator-facing report rather than a `vllm serve` crash. ### 🐛 Describe the bug `SchedulerConfig.max_num_scheduled_tokens` accepts a negative value with no validation in the non-speculative-decoding path, and that negative value then becomes the scheduler's `token_budget`, tripping a bare `assert token_budget >= 0` deep inside `schedule()`. The defect is not a *missing* guard but a *gated* one — the validation exists, but only runs under speculative decoding. ### Root cause: the ` = 0 # bare AssertionError, no message ``` (and `assert total_num_scheduled_tokens ", sched.max_num_scheduled_tokens, "(no validation)") # 2. A real VllmConfig with speculative_config is None leaves the -1 intact # after __post_init__ -> _set_max_num_scheduled_tokens (the effective =", effective, "(propagates)") # 4. token_budget = effective (scheduler.py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rror in the scheduler bug ### Your current environment Found by bounded model checking (ESBMC-Python - https://github.com/esbmc/esbmc) and confirmed with a behavioral reproduction on real vLLM config objects (below), in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: egative max_num_scheduled_tokens bypasses validation (guard gated behind speculative decoding) → bare AssertionError in the scheduler bug ### Your current environment Found by bounded model checking (ESBMC-Python - http...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: sertionError) ``` Steps 1–2 are behavioral on real vLLM objects; step 3 evaluates the verbatim `scheduler.py:104` expression on the resolved config. (Instantiating the full `Scheduler`/`schedule()` additionally needs a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _config is None: True ; field == -1 (guard skipped) [3] scheduler.py:104 fallback -> effective = -1 (propagates) [4] token_budget = -1 -> assert token_budget >= 0 FAILS (bare AssertionError) ``` Steps 1–2 are behavioral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: field is **not CLI-settable**, so this is a lower-severity, integrator-facing report rather than a `vllm serve` crash. ### 🐛 Describe the bug `SchedulerConfig.max_num_scheduled_tokens` accepts a negative value with no v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
