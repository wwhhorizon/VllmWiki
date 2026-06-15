# vllm-project/vllm#4432: [Bug]:  all_reduce assert result == 0, File "torch/cuda/graphs.py", line 88, in capture_end    super().capture_end(), RuntimeError: CUDA error: operation failed due to a previous error during capture

| 字段 | 值 |
| --- | --- |
| Issue | [#4432](https://github.com/vllm-project/vllm/issues/4432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  all_reduce assert result == 0, File "torch/cuda/graphs.py", line 88, in capture_end    super().capture_end(), RuntimeError: CUDA error: operation failed due to a previous error during capture

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Centos 7 (Final) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Could not collect CMake version: version 3.26.1 Libc version: glibc-2.17 Python version: 3.8.12 (default, Nov 11 2021, 20:11:20) [GCC 7.3.0] (64-bit runtime) Python platform: Linux-4.14.105-1-tlinux3-0013-x86_64-with-glibc2.2.5 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: Tesla V100-SXM2-32GB GPU 5: Tesla V100-SXM2-32GB GPU 6: Tesla V100-SXM2-32GB GPU 7: Tesla V100-SXM2-32GB Nvidia driver version: 450.156.00 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.0.5 /usr/lib64/libcudnn_adv_infer.so.8.0.5 /usr/lib64/libcudnn_adv_train.so.8.0.5 /usr/lib64/libcudnn_cnn_infer.so.8.0.5 /usr/lib64/libcudnn_cnn_train.so.8.0.5 /usr/lib64/libcudnn_ops_infer.so.8.0.5 /usr/lib64/libcudnn_ops_train.so.8.0.5 HIP runtime version: N/A M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Centos 7 (Final) (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: all_reduce assert result == 0, File "torch/cuda/graphs.py", line 88, in capture_end super().capture_end(), RuntimeError: CUDA error: operation failed due to a previous error during capture bug;stale ### Your curr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: chaudio==0.9.0 [pip3] torchdata==0.6.0 [pip3] torchvision==0.15.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0.post1 vLLM Build Flags: CUDA Ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Centos 7 (Fina...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=2, disable_custom_all_reduce=True, quantization=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
