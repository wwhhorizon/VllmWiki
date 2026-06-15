# vllm-project/vllm#14954: [Bug]: vLLM running on Unspecified Platform raises NotImplementedError when using podman/docker-compose

| 字段 | 值 |
| --- | --- |
| Issue | [#14954](https://github.com/vllm-project/vllm/issues/14954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM running on Unspecified Platform raises NotImplementedError when using podman/docker-compose

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` (ran on host, not in a container) ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 9.5 (Blue Onyx) (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-2) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.9.21 (main, Dec 5 2024, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] (64-bit runtime) Python platform: Linux-5.14.0-427.35.1.el9_4.cloud.1.0.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.90.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU @ 2.20GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 2 So...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: vLLM running on Unspecified Platform raises NotImplementedError when using podman/docker-compose bug;stale ### Your current environment The output of `python collect_env.py` (ran on host, not in a container) ```t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: container) ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 9.5 (Blue Onyx) (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.90.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtim...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.3 vLLM Build Flags: CUDA Archs:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
