# vllm-project/vllm#10168: [Bug]: KeyError: 'layers.0.self_attn.qkv_proj.weight' when using mistral or phi 

| 字段 | 值 |
| --- | --- |
| Issue | [#10168](https://github.com/vllm-project/vllm/issues/10168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.0.self_attn.qkv_proj.weight' when using mistral or phi 

### Issue 正文摘录

### Your current environment > No module named 'vllm._version' > from vllm.version import __version__ as VLLM_VERSION > Collecting environment information... > PyTorch version: 2.4.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.5 LTS (x86_64) > GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 > Clang version: Could not collect > CMake version: Could not collect > Libc version: glibc-2.35 > > Python version: 3.11.10 (main, Oct 3 2024, 07:29:13) [GCC 11.2.0] (64-bit runtime) > Python platform: Linux-6.8.0-48-generic-x86_64-with-glibc2.35 > Is CUDA available: True > CUDA runtime version: 11.5.119 > CUDA_MODULE_LOADING set to: LAZY > GPU models and configuration: > GPU 0: Quadro RTX 4000 > GPU 1: Quadro RTX 4000 > GPU 2: Quadro RTX 4000 > GPU 3: Quadro RTX 4000 > > Nvidia driver version: 535.183.01 > cuDNN version: Could not collect > HIP runtime version: N/A > MIOpen runtime version: N/A > Is XNNPACK available: True > > CPU: > 架构： x86_64 > CPU 运行模式： 32-bit, 64-bit > Address sizes: 46 bits physical, 48 bits virtual > 字节序： Little Endian > CPU: 32 > 在线 CPU 列表： 0-31 > 厂商 ID： GenuineIntel > 型号名称： Intel(R) Xeon(R)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: or phi bug;stale ### Your current environment > No module named 'vllm._version' > from vllm.version import __version__ as VLLM_VERSION > Collecting environment information... > PyTorch version: 2.4.0+cu121 > Is debug bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: information... > PyTorch version: 2.4.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: Ubuntu 22.04.5 LTS (x86_64) > GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: lm.version import __version__ as VLLM_VERSION > Collecting environment information... > PyTorch version: 2.4.0+cu121 > Is debug build: False > CUDA used to build PyTorch: 12.1 > ROCM used to build PyTorch: N/A > > OS: U...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rom line: ```python llm = LLM(model= args.llm_name, dtype='float16', #max_model_len = max_len, tensor_parallel_size= torch.cuda.device_count(), gpu_memory_utilization= 0.96, #seed=None, tru
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Mitigation; TSX disabled > > Versions of relevant libraries: > [pip3] flashinfer==0.1.6+cu121torch2.4 > [pip3] numpy==1.26.4 > [pip3] nvidia-cublas-cu12==12.1.3.1 > [pip3] nvidia-cuda-cupti-cu12==12.1.105 > [pip3] nvidi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
