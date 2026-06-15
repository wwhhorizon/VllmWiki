# vllm-project/vllm#32653: [Usage]: CPU offload still results in out of VRAM error (Unsloth's DeepSeek R1)

| 字段 | 值 |
| --- | --- |
| Issue | [#32653](https://github.com/vllm-project/vllm/issues/32653) |
| 状态 | open |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: CPU offload still results in out of VRAM error (Unsloth's DeepSeek R1)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py`: Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (main, Oct 21 2025, 16:43:05) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-216-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 10.1.243 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 GPU 2: NVIDIA RTX A5000 GPU 3: NVIDIA RTX A5000 Nvidia driver version : 570.133.07 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.31 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: rsions of relevant libraries ============================== [pip3] conch-triton-kernels==1.3 [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ```text The output of `python collect_env.py`: Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
