# vllm-project/vllm#14996: [Bug]: CDNA cc >= 90, choose_mp_linear_kernel MacheteLinearKernel is possible

| 字段 | 值 |
| --- | --- |
| Issue | [#14996](https://github.com/vllm-project/vllm/issues/14996) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CDNA cc >= 90, choose_mp_linear_kernel MacheteLinearKernel is possible

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On CDNA / gfx908 (Mi100): ``` >>> import torch >>> torch.cuda.get_device_capability(0) (9, 0) ``` ``` INFO 03-17 19:57:37 [__init__.py:256] Automatically detected platform rocm. INFO 03-17 19:57:39 [api_server.py:972] vLLM API server version 0.7.4.dev481+g80bb57ee ... INFO 03-17 19:58:14 [compressed_tensors_wNa16.py:85] Using MacheteLinearKernel for CompressedTensorsWNA16 ERROR 03-17 19:59:08 [engine.py:443] '_OpNamespace' '_C' object has no attribute 'machete_prepack_B' ``` I assume this would need some other axis of test here? But I don't actually know whether "compute capability" is supposed to be platform agnostic in torch. Semi-related: I think this would also happen to people on SM90a who built without Machete supported, because I don't see a mechanism for skipping this kernel just because it didn't build (also includes my case). Sadly, even if I ban it out with `VLLM_DISABLED_KERNELS=MacheteLinearKernel`, I still get `'_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack'`. I don't know if that's basically the same issue, or if Marlin is supposed to work on ROCm. ### Before submitting a new issue... - [x] Make su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vironment ### 🐛 Describe the bug On CDNA / gfx908 (Mi100): ``` >>> import torch >>> torch.cuda.get_device_capability(0) (9, 0) ``` ``` INFO 03-17 19:57:37 [__init__.py:256] Automatically detected platform rocm. INFO 03-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cribe the bug On CDNA / gfx908 (Mi100): ``` >>> import torch >>> torch.cuda.get_device_capability(0) (9, 0) ``` ``` INFO 03-17 19:57:37 [__init__.py:256] Automatically detected platform rocm. INFO 03-17 19:57:39 [api_se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: NA cc >= 90, choose_mp_linear_kernel MacheteLinearKernel is possible bug;stale ### Your current environment ### 🐛 Describe the bug On CDNA / gfx908 (Mi100): ``` >>> import torch >>> torch.cuda.get_device_capability(0) (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ectness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your curren...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
