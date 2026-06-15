# vllm-project/vllm#7201: [Bug]: NCCL gives an error when I use tensor_parallel ：RuntimeError: NCCL error: invalid usage

| 字段 | 值 |
| --- | --- |
| Issue | [#7201](https://github.com/vllm-project/vllm/issues/7201) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL gives an error when I use tensor_parallel ：RuntimeError: NCCL error: invalid usage

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-52-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version: 520.61.05 cuDNN version: Probably one of the following: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: invalid usage bug ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: nown Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store byp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Qwen/Qwen2-7B-Instruct/', tokenizer='/data/wjc/Qwen/Qwen2-7B-Instruct/', quantization=None, tensor_parallel_size=2, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=False,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
