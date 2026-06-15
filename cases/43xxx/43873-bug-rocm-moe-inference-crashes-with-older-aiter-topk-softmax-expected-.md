# vllm-project/vllm#43873: [Bug]: [ROCm] MoE inference crashes with older aiter: topk_softmax() expected at most 5 argument(s) but received 7

| 字段 | 值 |
| --- | --- |
| Issue | [#43873](https://github.com/vllm-project/vllm/issues/43873) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [ROCm] MoE inference crashes with older aiter: topk_softmax() expected at most 5 argument(s) but received 7

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - ROCm, `VLLM_ROCM_USE_AITER_MOE=1` - aiter 5-arg `topk_softmax` - vLLM main after PR #39280 ### Affected models MoE model whose router uses `scoring_func="softmax"` and reaches `FusedTopKRouter` — i.e. no grouped top-k, no `e_score_correction_bias`. Confirmed affected: - `mistralai/Mixtral-8x7B-Instruct-v0.1` — `FusedMoE` default `scoring_func="softmax"`, no `e_score_correction_bias`, no expert groups ### What happened MoE models that use `scoring_func="softmax"` routing and are served on ROCm with the aiter fused-MoE path enabled crash on the first forward pass (during memory profiling) with: ``` RuntimeError: aiter::topk_softmax() expected at most 5 argument(s) but received 7 argument(s). Declaration: aiter::topk_softmax(Tensor(a0!) topk_weights, Tensor(a1!) topk_indices, Tensor(a2!) token_expert_indices, Tensor(a3!) gating_output, bool need_renorm) -> () ``` ### Traceback ``` Traceback (most recent call last): File ".../vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop output = func(*args, **kwargs) File ".../vllm/v1/worker/gpu_worker.py", line 396, in determine_available_memory self.model...

## 现有链接修复摘要

#39280 [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Bug]: [ROCm] MoE inference crashes with older aiter: topk_softmax() expected at most 5 argument(s) but received 7 bug;rocm ### Your current environment ### 🐛 Describe the bug ### Environment - ROCm, `VLLM_ROCM_USE_AITE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: [ROCm] MoE inference crashes with older aiter: topk_softmax() expected at most 5 argument(s) but received 7 bug;rocm ### Your current environment ### 🐛 Describe the bug ### Environment - ROCm, `VLLM_ROCM_USE_AITE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `topk_softmax_supports_fused_sigmoid()` to detect at runtime whether the installed aiter supports the 7-arg form, and `fuse_sigmoid_in_kernel()` to gate the FSE dispatch path. But `_rocm_aiter_topk_softmax_impl` itself...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [ROCm] MoE inference crashes with older aiter: topk_softmax() expected at most 5 argument(s) but received 7 bug;rocm ### Your current environment ### 🐛 Describe the bug ### Environment - ROCm, `VLLM_ROCM_USE_AITE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: er fused-MoE path enabled crash on the first forward pass (during memory profiling) with: ``` RuntimeError: aiter::topk_softmax() expected at most 5 argument(s) but received 7 argument(s). Declaration: aiter::topk_softm...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39280](https://github.com/vllm-project/vllm/pull/39280) | mentioned | 0.45 | [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next | r(a3!) gating_output, bool need_renorm) -> () ``` ### root cause pr #39280 extended `_rocm_aiter_topk_softmax_impl` to unconditionally pass 7 args to `aiter.topk_softmax`, includi… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
