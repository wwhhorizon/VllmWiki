# vllm-project/vllm#35915: TPU: Override use_custom_op_collectives() in TpuPlatform

| 字段 | 值 |
| --- | --- |
| Issue | [#35915](https://github.com/vllm-project/vllm/issues/35915) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TPU: Override use_custom_op_collectives() in TpuPlatform

### Issue 正文摘录

## Summary The `use_custom_op_collectives()` platform method was added in #34760 to allow platforms to opt-in to using `torch.ops.vllm.*` custom ops for collective operations. CUDA and ROCm already override this method to return `True`. Currently, the TPU platform still relies on an explicit `current_platform.is_tpu()` check in `vllm/distributed/parallel_state.py` because `TpuPlatform` is defined externally in the `tpu_inference` package and does not yet override `use_custom_op_collectives()`. ## Request Override `use_custom_op_collectives()` to return `True` in `tpu_inference`'s `TpuPlatform` class, so the `is_tpu()` fallback check in `parallel_state.py` can be removed. Once this is done, the condition in `parallel_state.py` can be simplified from: ```python # TODO: Remove is_tpu() check once tpu_inference overrides # use_custom_op_collectives() to return True. self.use_custom_op_call = ( current_platform.is_tpu() or current_platform.use_custom_op_collectives() ) ``` to: ```python self.use_custom_op_call = current_platform.use_custom_op_collectives() ``` ## Context - PR #34760 added the `use_custom_op_collectives()` method - `TpuPlatform` lives in the external `tpu_inference` pac...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: opt-in to using `torch.ops.vllm.*` custom ops for collective operations. CUDA and ROCm already override this method to return `True`. Currently, the TPU platform still relies on an explicit `current_platform.is_tpu()` c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: TPU: Override use_custom_op_collectives() in TpuPlatform stale ## Summary The `use_custom_op_collectives()` platform method was added in #34760 to allow platforms to opt-in to using `torch.ops.vllm.*` custom ops for col...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: eturn `True` in `tpu_inference`'s `TpuPlatform` class, so the `is_tpu()` fallback check in `parallel_state.py` can be removed. Once this is done, the condition in `parallel_state.py` can be simplified from: ```python #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d to return `True`. Currently, the TPU platform still relies on an explicit `current_platform.is_tpu()` check in `vllm/distributed/parallel_state.py` because `TpuPlatform` is defined externally in the `tpu_inference` pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
