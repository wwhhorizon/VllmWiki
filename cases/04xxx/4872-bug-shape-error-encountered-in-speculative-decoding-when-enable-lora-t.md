# vllm-project/vllm#4872: [Bug]: Shape error encountered in speculative decoding when `enable_lora=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#4872](https://github.com/vllm-project/vllm/issues/4872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Shape error encountered in speculative decoding when `enable_lora=True`

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.11.6 (main, Oct 3 2023, 01:26:22) [Clang 17.0.1 ] (64-bit runtime) Python platform: Linux-6.2.0-37-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.3 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nable_lora=True` bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Shape error encountered in speculative decoding when `enable_lora=True` bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
