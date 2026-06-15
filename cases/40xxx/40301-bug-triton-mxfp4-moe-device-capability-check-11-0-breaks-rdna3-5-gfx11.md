# vllm-project/vllm#40301: [Bug]: Triton MXFP4 MoE device capability check < (11, 0) breaks RDNA3.5 (gfx1151) support

| 字段 | 值 |
| --- | --- |
| Issue | [#40301](https://github.com/vllm-project/vllm/issues/40301) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | kernel;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton MXFP4 MoE device capability check < (11, 0) breaks RDNA3.5 (gfx1151) support

### Issue 正文摘录

### Your current environment ### System Info **OS:** Linux (e.g., Fedora 43) **Hardware:** AMD Strix Halo APU (gfx1151 / RDNA 3.5) **vLLM version:** `v0.19.2` (and recent nightlies/main) **Model:** `openai/gpt-oss-20b` (or any `gpt_oss_mxfp4` quantized MoE model) ### 🐛 Describe the bug I am trying to run vLLM on an AMD Strix Halo (gfx1151) using ROCm. The environment is properly configured to compile Triton kernels. Previously, `gpt-oss-20b` (which initializes using `gpt_oss_mxfp4` quantization) worked perfectly fine and used the Triton MXFP4 MoE backend as expected. However, a recent update explicitly bounded the `device_capability` checks for the Triton MoE kernels to ` bool: ... return (9, 0) <= (cap.major, cap.minor) < (11, 0) ``` * In `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`: ```python triton_kernels_supported = has_triton_kernels() and ( 9, 0, ) <= current_platform.get_device_capability() < (11, 0) ``` Because vLLM maps `gfx1151` to a device capability of `(11, 5)`, the `< (11, 0)` check completely fails for the entire RDNA3/RDNA3.5 family. As a result, the backend oracle drops the Triton kernels, cannot find any other fallback MXFP4 backends for ROCm, and cras...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Fedora 43) **Hardware:** AMD Strix Halo APU (gfx1151 / RDNA 3.5) **vLLM version:** `v0.19.2` (and recent nightlies/main) **Model:** `openai/gpt-oss-20b` (or any `gpt_oss_mxfp4` quantized MoE model) ### 🐛 Describe the bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Triton MXFP4 MoE device capability check < (11, 0) breaks RDNA3.5 (gfx1151) support bug;rocm ### Your current environment ### System Info **OS:** Linux (e.g., Fedora 43) **Hardware:** AMD Strix Halo APU (gfx1151...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Triton MXFP4 MoE device capability check < (11, 0) breaks RDNA3.5 (gfx1151) support bug;rocm ### Your current environment ### System Info **OS:** Linux (e.g., Fedora 43) **Hardware:** AMD Strix Halo APU (gfx1151...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Triton MXFP4 MoE device capability check < (11, 0) breaks RDNA3.5 (gfx1151) support bug;rocm ### Your current environment ### System Info **OS:** Linux (e.g., Fedora 43) **Hardware:** AMD Strix Halo APU (gfx1151...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 51 / RDNA 3.5) **vLLM version:** `v0.19.2` (and recent nightlies/main) **Model:** `openai/gpt-oss-20b` (or any `gpt_oss_mxfp4` quantized MoE model) ### 🐛 Describe the bug I am trying to run vLLM on an AMD Strix Halo (gf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
