# vllm-project/vllm#35724: [Bug] H100 PCIe: RuntimeError '[SymmDeviceMemory] Device does not support multicasting' when running Qwen3.5-122B with TP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#35724](https://github.com/vllm-project/vllm/issues/35724) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] H100 PCIe: RuntimeError '[SymmDeviceMemory] Device does not support multicasting' when running Qwen3.5-122B with TP=2

### Issue 正文摘录

### My environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-90-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 PCIe GPU 1: NVIDIA H100 PCIe Nvidia driver version : 580.126.09 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug] H100 PCIe: RuntimeError '[SymmDeviceMemory] Device does not support multicasting' when running Qwen3.5-122B with TP=2 usage ### My environment ```text Collecting environment information... ========================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug] H100 PCIe: RuntimeError '[SymmDeviceMemory] Device does not support multicasting' when running Qwen3.5-122B with TP=2 usage ### My environment ```text Collecting environment information... ========================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r '[SymmDeviceMemory] Device does not support multicasting' when running Qwen3.5-122B with TP=2 usage ### My environment ```text Collecting environment information... ============================== System Info =========...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
