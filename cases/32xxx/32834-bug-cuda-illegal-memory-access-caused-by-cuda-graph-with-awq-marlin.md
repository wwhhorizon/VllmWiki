# vllm-project/vllm#32834: [Bug]: CUDA illegal memory access caused by CUDA Graph with awq_marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#32834](https://github.com/vllm-project/vllm/issues/32834) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access caused by CUDA Graph with awq_marlin

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have further isolated the issue. Running with **`--enforce-eager` completely resolves the crash**, but results in significantly degraded performance. This confirms that the `illegal memory access` is strictly related to the **CUDA Graph capture/replay mechanism** in the V1 engine when paired with `awq_marlin` quantization on GLM-4.7-Flash. ### Test Results Summary | Configuration | Stability | Performance | | --- | --- | --- | | Default (CUDA Graph ON) | **Crash** (`cudagraph.replay()`) | N/A | | `--enforce-eager` | **Stable** | Very Slow | ### Precise Error Location The sync trace points to the following call stack: ```python (Worker_TP3_EP3) File ".../vllm/v1/worker/gpu_model_runner.py", line 2923, in _model_forward (Worker_TP3_EP3) return self.model(...) (Worker_TP3_EP3) File ".../vllm/compilation/cuda_graph.py", line 308, in __call__ (Worker_TP3_EP3) entry.cudagraph.replay() (Worker_TP3_EP3) torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` ### Technical Implications 1. **Kernel Incompatibility**: Some kernels in the `awq_marlin` implementation (or the way GLM-4.7-Flash uses them) might be usi...

## 现有链接修复摘要

#33896 [Bugfix] Fix illegal memory access in AWQ-Marlin with CUDA graphs (Fixes #32834)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eplay()`) | N/A | | `--enforce-eager` | **Stable** | Very Slow | ### Precise Error Location The sync trace points to the following call stack: ```python (Worker_TP3_EP3) File ".../vllm/v1/worker/gpu_model_runner.py", li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access caused by CUDA Graph with awq_marlin bug;stale ### Your current environment ### 🐛 Describe the bug I have further isolated the issue. Running with **`--enforce-eager` completely resolve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `awq_marlin` quantization on GLM-4.7-Flash. ### Test Results Summary | Configuration | Stability | Performance | | --- | --- | --- | | Default (CUDA Graph ON) | **Crash** (`cudagraph.replay()`) | N/A | | `--enforce-eage...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: CUDA illegal memory access caused by CUDA Graph with awq_marlin bug;stale ### Your current environment ### 🐛 Describe the bug I have further isolated the issue. Running with **`--enforce-eager` completely resolves...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown env_dependency #33896 [Bugfix] Fix illegal memory access in AWQ-Marlin with CUDA graphs (Fixes #32834) Y...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33896](https://github.com/vllm-project/vllm/pull/33896) | closes_keyword | 0.95 | [Bugfix] Fix illegal memory access in AWQ-Marlin with CUDA graphs (Fixes #32834) | fixes issue #32834 where AWQ-Marlin quantization causes illegal memory access when used with CUDA graphs. ## Problem AWQ-Marlin kernels use workspace buffers allocated during mode |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
