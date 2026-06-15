# vllm-project/vllm#40926: [Bug]: V1 engine + MTP + GLM-5.1 (DSA + MoE + MLA) — workers hang under sustained traffic, sample_tokens RPC timeout, EngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#40926](https://github.com/vllm-project/vllm/issues/40926) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe |
| 症状 | crash;nondeterministic;oom |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: V1 engine + MTP + GLM-5.1 (DSA + MoE + MLA) — workers hang under sustained traffic, sample_tokens RPC timeout, EngineDeadError

### Issue 正文摘录

### 🐛 Describe the bug Under V1 engine + MTP speculative decoding + TP=8 + GLM-5.1-FP8 (`GlmMoeDsaForCausalLM`), workers hang under sustained production traffic. The scheduler is unable to advance — `step_counter=0` in the dump, requests stuck in flight — and after 30s the `sample_tokens` RPC times out, killing EngineCore. The container's outer process survives so vLLM internally restarts the engine (~12-17 min downtime), but this is a recurring failure pattern. This is the same bug `jsboige` diagnosed for `new-TonyWang` in [#35104](https://github.com/vllm-project/vllm/issues/35104#issuecomment-4308377748) — a different bug than what PR #40303 fixes (no `SystemError`, no `memory_fence` on the stack). new-TonyWang's report is buried in #35104 comments and has no standalone issue, so filing here. ### Stack trace ``` File ".../vllm/v1/engine/core.py", line 1205, in _process_engine_step outputs, model_executed = self.step_fn() File ".../vllm/v1/engine/core.py", line 523, in step_with_batch_queue model_output = future.result() ... File ".../vllm/v1/executor/multiproc_executor.py", line 388, in get_response raise TimeoutError(f"RPC call to {method} timed out.") from e TimeoutError: RPC...

## 现有链接修复摘要

#40303 [Bug] Fix shm_broadcast PyCFunction descriptor corruption under JIT loads

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: C timeout, EngineDeadError ### 🐛 Describe the bug Under V1 engine + MTP speculative decoding + TP=8 + GLM-5.1-FP8 (`GlmMoeDsaForCausalLM`), workers hang under sustained production traffic. The scheduler is unable to adv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: llm/pull/40303): no `SystemError`, `memory_fence` not on stack. - Not specific to autotune compiling kernels mid-request: disabling autotune extends MTTF 8× but doesn't eliminate the hang. - Not capacity-bound: only 2 i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ibe the bug Under V1 engine + MTP speculative decoding + TP=8 + GLM-5.1-FP8 (`GlmMoeDsaForCausalLM`), workers hang under sustained production traffic. The scheduler is unable to advance — `step_counter=0` in the dump, r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: equests=0, ...), spec_decoding_stats=None, ...) ``` ### Reproduction (deterministic given enough wall clock) | Setup | |---| | Image: built from v0.20.0 tag, `--target vllm-openai`, CUDA 13.0, Py 3.12, torch 2.11 | | Ha...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: equests=0, ...), spec_decoding_stats=None, ...) ``` ### Reproduction (deterministic given enough wall clock) | Setup | |---| | Image: built from v0.20.0 tag, `--target vllm-openai`, CUDA 13.0, Py 3.12, torch 2.11 | | Ha...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40303](https://github.com/vllm-project/vllm/pull/40303) | mentioned | 0.45 | [Bug] Fix shm_broadcast PyCFunction descriptor corruption under JIT loads | ssion we initially hit. - not the descriptor-corruption bug fixed by [#40303](https://github.com/vllm-project/vllm/pull/40303): no `systemerror`, `memory_fence` not on stack. - no… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
