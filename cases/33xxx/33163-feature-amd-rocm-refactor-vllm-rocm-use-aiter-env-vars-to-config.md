# vllm-project/vllm#33163: [Feature][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config

| 字段 | 值 |
| --- | --- |
| Issue | [#33163](https://github.com/vllm-project/vllm/issues/33163) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config

### Issue 正文摘录

## Background We currently uses 13 environment variables to control AITER (AI Tensor Engine for ROCm) optimizations for ROCm platforms. Issue #25700 discusses the need to move away from such heavy reliance on env vars: - Environment variables lack type checking, validation, and hierarchical organization - They represent a form of global state that makes the codebase harder to maintain - They are difficult to discover and document - They create technical debt as the project scales See #29912 for a pattern which can be followed. See also: - #33043 - recent PR to add another env var - #21138, #26719, #21805, #18367 - several issues describing the complexity of having to tune so many vars (but note, this is not significantly improved by moving to a config format) ## Proposal The IR Ops PR #32358 adds `--kernel-config`: ```bash --kernel-config.ir_op_priority.rms_norm=vllm_c --kernel-config.ir_op_priority.linear=aiter --kernel-config.ir_op_priority.attention=aiter ``` It will also allow use to choose variants of aiter kernel (kernels of the same type in AITER can be implemented many ways, CK, ASM, triton, gluon, HIP. So through the IR Ops we can have aiter_ck, aiter_asm, aiter_triton, e...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config feature request;rocm;stale ## Background We currently uses 13 environment variables to control AITER (AI Tensor Engine for ROCm) optimizations for ROC...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config feature request;rocm;stale ## Background We currently uses 13 environment variables to control AITER (AI Tensor Engine for ROCm) optimizations for ROC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config feature request;rocm;stale ## Background We currently uses 13 environment variables to control AITER (AI Tensor Engine for ROCm) optimizations for ROC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ture][AMD][ROCm] Refactor VLLM_ROCM_USE_AITER env vars to config feature request;rocm;stale ## Background We currently uses 13 environment variables to control AITER (AI Tensor Engine for ROCm) optimizations for ROCm pl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ult to discover and document - They create technical debt as the project scales See #29912 for a pattern which can be followed. See also: - #33043 - recent PR to add another env var - #21138, #26719, #21805, #18367 - se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
