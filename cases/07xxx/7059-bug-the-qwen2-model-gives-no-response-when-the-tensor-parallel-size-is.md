# vllm-project/vllm#7059: [Bug]: The Qwen2 model gives no response when the tensor_parallel_size is set to 1.

| 字段 | 值 |
| --- | --- |
| Issue | [#7059](https://github.com/vllm-project/vllm/issues/7059) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The Qwen2 model gives no response when the tensor_parallel_size is set to 1.

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 4.9.2 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.8.19 (default, Mar 20 2024, 19:58:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.19.91-011.ali4000.alios7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB Nvidia driver version: 535.129.03 cuDNN version: /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudnn.so.7.6.3 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ize is set to 1. bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: The Qwen2 model gives no response when the tensor_parallel_size is set to 1. bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: , trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=2, dtype=torch.float16) outputs = llm.generate(texts, sampling_params) # 输出结果 for output in outputs: prompt = output.prompt generated_text = output.o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: .3.1+cu121 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.3 [pip3] triton==2.3.1 [conda] numpy 1.24.1 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.1+cu121

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
