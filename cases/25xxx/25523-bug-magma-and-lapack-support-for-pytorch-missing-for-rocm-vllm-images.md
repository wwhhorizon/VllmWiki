# vllm-project/vllm#25523: [Bug]: MAGMA and LAPACK support for pytorch missing for rocm/vllm images

| 字段 | 值 |
| --- | --- |
| Issue | [#25523](https://github.com/vllm-project/vllm/issues/25523) |
| 状态 | closed |
| 标签 | bug;feature request;rocm;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MAGMA and LAPACK support for pytorch missing for rocm/vllm images

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Images tested: `rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909`, `rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6` and `rocm/vllm:rocm6.2_mi300_ubuntu20.04_py3.9_vllm_0.6.4` ```python >>> torch.cholesky(torch.tensor([[4., 2.], [2., 3.]], device='cuda')) Traceback (most recent call last): File " ", line 1, in RuntimeError: Calling torch.linalg.cholesky on a CUDA tensor requires compiling PyTorch with MAGMA. Please use PyTorch built with MAGMA support. >>> ``` ```python >>> torch.cholesky(torch.tensor([[4., 2.], [2., 3.]])) :1: UserWarning: torch.cholesky is deprecated in favor of torch.linalg.cholesky and will be removed in a future PyTorch release. L = torch.cholesky(A) should be replaced with L = torch.linalg.cholesky(A) and U = torch.cholesky(A, upper=True) should be replaced with U = torch.linalg.cholesky(A).mH This transform will produce equivalent results for all valid (symmetric positive definite) inputs. (Triggered internally at /app/pytorch/aten/src/ATen/native/BatchLinearAlgebra.cpp:1756.) Traceback (most recent call last): File " ", line 1, in RuntimeError: Calling torch.linalg.cholesky on a CPU tensor requires compil...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: MAGMA and LAPACK support for pytorch missing for rocm/vllm images bug;feature request;rocm;stale ### Your current environment ### 🐛 Describe the bug Images tested: `rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909`, `roc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: and LAPACK support for pytorch missing for rocm/vllm images bug;feature request;rocm;stale ### Your current environment ### 🐛 Describe the bug Images tested: `rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909`, `rocm/vllm:rocm6....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntly asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current envi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
