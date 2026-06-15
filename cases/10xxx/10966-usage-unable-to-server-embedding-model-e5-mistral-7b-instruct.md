# vllm-project/vllm#10966: [Usage]: Unable to server embedding model e5-mistral-7b-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#10966](https://github.com/vllm-project/vllm/issues/10966) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to server embedding model e5-mistral-7b-instruct

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: AlmaLinux 8.10 (Cerulean Leopard) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.28 Python version: 3.11.3 | packaged by conda-forge | (main, Apr 6 2023, 08:57:19) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-4.18.0-553.22.1.el8_10.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 1 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 8 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7713 64-Core Processor Stepping: 1 CPU MHz: 3050.826 CPU max MHz:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: AlmaLinux 8.10 (Cerulean Leopard) (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: AlmaLinux 8.10 (Cerulean Leopard) (x86_64) GCC version: (GCC) 8.5.0 20210514...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Unable to server embedding model e5-mistral-7b-instruct usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] pyzmq 25.0.2 py311hd6ccaeb_0 conda-forge ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rf xsaveerptr wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
