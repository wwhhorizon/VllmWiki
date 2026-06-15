# vllm-project/vllm#8243: [Installation]: NotImplementedError get_device_capability

| 字段 | 值 |
| --- | --- |
| Issue | [#8243](https://github.com/vllm-project/vllm/issues/8243) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: NotImplementedError get_device_capability

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: AlmaLinux release 8.10 (Cerulean Leopard) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.28 Python version: 3.11.9 (main, Jul 2 2024, 16:32:17) [GCC 8.5.0 20210514 (Red Hat 8.5.0-22)] (64-bit runtime) Python platform: Linux-4.18.0-553.8.1.el8_10.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: NotImplementedError get_device_capability installation ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Installation]: NotImplementedError get_device_capability installation ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lity installation ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: AlmaLinux rele...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.0@32e7db25365415841ebc7c42158517...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
