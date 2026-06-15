# vllm-project/vllm#5365: [Bug]: load nvidia/Llama3-ChatQA-1.5-8B model 15 min 

| 字段 | 值 |
| --- | --- |
| Issue | [#5365](https://github.com/vllm-project/vllm/issues/5365) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: load nvidia/Llama3-ChatQA-1.5-8B model 15 min 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.32 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.112-005.ali5000.alios7.x86_64-x86_64-with-glibc2.32 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 24-31,56-63,88-95,120-127 Off-line CPU(s) list: 0-23,32-55,64-87,96-119 Thread(s) per core: 0 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz Stepping: 6 CPU MHz: 3499....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: A-1.5-8B model 15 min bug ### Your current environment ```text PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: urrent environment ```text PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: load nvidia/Llama3-ChatQA-1.5-8B model 15 min bug ### Your current environment ```text PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Gro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ion=VLLM_GPU_MEMORY_UTILIZATION, trust_remote_code=True, dtype="half", # note: bfloat16 is not supported on nvidia-T4 GPUs enforce_eager=True, ) tokenizer = llm.get_tokenizer() return llm, tokenizer self.vllm, self.toke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf14

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
