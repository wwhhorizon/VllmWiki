# vllm-project/vllm#4734: [Bug]:Segmentation fault encountered while running model

| 字段 | 值 |
| --- | --- |
| Issue | [#4734](https://github.com/vllm-project/vllm/issues/4734) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Segmentation fault encountered while running model

### Issue 正文摘录

### Your current environment PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Tencent tlinux 2.2 (Final) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.17 Python version: 3.9.0 | packaged by conda-forge | (default, Nov 26 2020, 07:57:39) [GCC 9.3.0] (64-bit runtime) Python platform: Linux-4.14.105-1-tlinux3-0013-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: A100-SXM4-40GB GPU 1: A100-SXM4-40GB GPU 2: A100-SXM4-40GB GPU 3: A100-SXM4-40GB GPU 4: A100-SXM4-40GB GPU 5: A100-SXM4-40GB GPU 6: A100-SXM4-40GB GPU 7: A100-SXM4-40GB Nvidia driver version: 450.156.00 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.0.5 /usr/lib64/libcudnn_adv_infer.so.8.0.5 /usr/lib64/libcudnn_adv_train.so.8.0.5 /usr/lib64/libcudnn_cnn_infer.so.8.0.5 /usr/lib64/libcudnn_cnn_train.so.8.0.5 /usr/lib64/libcudnn_ops_infer.so.8.0.5 /usr/lib64/libcudnn_ops_train.so.8.0.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ncountered while running model bug ### Your current environment PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Tencent tlinux 2.2 (Final) (x86_64)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Tencent tlinux 2.2 (Final) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Cou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _mbm_local clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of rel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]:Segmentation fault encountered while running model bug ### Your current environment PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Tencent t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: =1.26.4 [pip3] nvidia-nccl-cu11==2.19.3 [pip3] torch==2.1.2+cu118 [pip3] triton==2.1.0 [pip3] vllm_nccl_cu11==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu11 2.19.3 pypi_0 pypi [conda] torch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
