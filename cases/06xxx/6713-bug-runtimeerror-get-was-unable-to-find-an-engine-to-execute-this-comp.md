# vllm-project/vllm#6713: [Bug]: RuntimeError: GET was unable to find an engine to execute this computation for llava-next model

| 字段 | 值 |
| --- | --- |
| Issue | [#6713](https://github.com/vllm-project/vllm/issues/6713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: GET was unable to find an engine to execute this computation for llava-next model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could not collect CMake version: version 3.28.1 Libc version: glibc-2.35 Python version: 3.10.2 (main, Feb 22 2024, 00:00:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.138.1-4.cm2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.85.12 cuDNN version: Probably one of the following: /usr/lib/libcudnn.so.8.9.5 /usr/lib/libcudnn_adv_infer.so.8.9.5 /usr/lib/libcudnn_adv_train.so.8.9.5 /usr/lib/libcudnn_cnn_infer.so.8.9.5 /usr/lib/libcudnn_cnn_train.so.8.9.5 /usr/lib/libcudnn_ops_infer.so.8.9.5 /usr/lib/libcudnn_ops_train.so.8.9.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: f `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: was unable to find an engine to execute this computation for llava-next model bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.3.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
