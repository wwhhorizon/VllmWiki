# vllm-project/vllm#15158: [Installation]: uv install not installing FlashInfer anymore

| 字段 | 值 |
| --- | --- |
| Issue | [#15158](https://github.com/vllm-project/vllm/issues/15158) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: uv install not installing FlashInfer anymore

### Issue 正文摘录

### Your current environment Current Install ```text INFO 03-19 20:06:08 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Oracle Linux Server 9.5 (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-2.0.1) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.12.9 (main, Feb 12 2025, 14:50:50) [Clang 19.1.6 ] (64-bit runtime) Python platform: Linux-5.15.0-304.171.4.3.el9uek.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 Nvidia driver version: 570.86.10 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.9.7 /usr/lib64/libcudnn_adv_infer.so.8.9.7 /usr/lib64/libcudnn_adv_train.so.8.9.7 /usr/lib64/libcudnn_cnn_infer.so.8.9.7 /usr/lib64/libcudnn_cnn_train.so.8.9.7 /usr/lib64/libcudnn_ops_infer.so.8.9.7 /usr/lib64/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: uv install not installing FlashInfer anymore installation ### Your current environment Current Install ```text INFO 03-19 20:06:08 [__init__.py:256] Automatically detected platform cuda. Collecting enviro
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 03-19 20:06:08 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Oracle Linux...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Installation]: uv install not installing FlashInfer anymore installation ### Your current environment Current Install ```text INFO 03-19 20:06:08 [__init__.py:256] Automatically detected platform cuda. Collecting envir...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: o following warning with no FlashInfer: ```bash WARNING 03-19 19:36:28 [topk_topp_sampler.py:63] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best per...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
