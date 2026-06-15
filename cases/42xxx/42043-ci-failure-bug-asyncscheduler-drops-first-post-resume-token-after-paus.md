# vllm-project/vllm#42043: [CI Failure][Bug] AsyncScheduler drops first post-resume token after pause_generation(mode="keep") + clear_cache

| 字段 | 值 |
| --- | --- |
| Issue | [#42043](https://github.com/vllm-project/vllm/issues/42043) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][Bug] AsyncScheduler drops first post-resume token after pause_generation(mode="keep") + clear_cache

### Issue 正文摘录

### Summary Under async scheduling, `pause_generation(mode="keep")` with the default `clear_cache=True` causes `AsyncScheduler` to silently drop the first valid post-resume token. The remaining tokens line up shifted by one. Production blast radius is small (RLHF training absorbs the loss into normal noise), but it's deterministic and incorrect. ### Reproduction [Distributed Tests (2 GPUs)(H100)](https://buildkite.com/vllm/ci/builds/65099#019e062d-3022-433d-926e-e15f52dfb524) running `examples/rl/rlhf_async_new_apis.py` started failing 0/13 prompts when #41421 flipped `VLLM_USE_RAY_V2_EXECUTOR_BACKEND` default to `1`. `RayExecutorV2` inherits async scheduling from `MultiprocExecutor`, which exposes a long-latent bug. #42042 disables `async_scheduling` in the example as a workaround. ### Root cause `Scheduler.reset_prefix_cache(reset_running_requests=True)` ([scheduler.py:1813-1819](https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/scheduler.py#L1813-L1819)) unconditionally sets `request.discard_latest_async_tokens = True` for each preempted running request. `AsyncScheduler._update_request_with_output` ([async_scheduler.py:37-44](https://github.com/vllm-project/vllm...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [CI Failure][Bug] AsyncScheduler drops first post-resume token after pause_generation(mode="keep") + clear_cache ### Summary Under async scheduling, `pause_generation(mode="keep")` with the default `clear_cache=True` ca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][Bug] AsyncScheduler drops first post-resume token after pause_generation(mode="keep") + clear_cache ### Summary Under async scheduling, `pause_generation(mode="keep")` with the default `clear_cache=True` cau
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: The remaining tokens line up shifted by one. Production blast radius is small (RLHF training absorbs the loss into normal noise), but it's deterministic and incorrect. ### Reproduction [Distributed Tests (2 GPUs)(H100)]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: us is small (RLHF training absorbs the loss into normal noise), but it's deterministic and incorrect. ### Reproduction [Distributed Tests (2 GPUs)(H100)](https://buildkite.com/vllm/ci/builds/65099#019e062d-3022-433d-926...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: arted failing 0/13 prompts when #41421 flipped `VLLM_USE_RAY_V2_EXECUTOR_BACKEND` default to `1`. `RayExecutorV2` inherits async scheduling from `MultiprocExecutor`, which exposes a long-latent bug. #42042 disables `asy...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
