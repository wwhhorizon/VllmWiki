# vllm-project/vllm#3694: [Bug]: NeuronExecutor.__init__() takes 7 positional arguments but 8 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#3694](https://github.com/vllm-project/vllm/issues/3694) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NeuronExecutor.__init__() takes 7 positional arguments but 8 were given

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1031-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True ... Versions of relevant libraries: [pip3] numpy==1.25.2 [pip3] torch==2.1.2 [pip3] torch-neuronx==2.1.1.2.0.1b0 [pip3] torch-xla==2.1.1 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: (0, 'instance-type: inf2.48xlarge vLLM Version: 0.3.3 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ``` ### 🐛 Des...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =auto, revision=Non e, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=128, download_dir=None, load_format=auto, tensor_parallel_size=2, disable_custom_all_reduce=True, quantization=N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: given bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =2.1.1.2.0.1b0 [pip3] torch-xla==2.1.1 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: (0, 'instance-type: inf2.48xlarge vLLM Version: 0.3.3 v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
