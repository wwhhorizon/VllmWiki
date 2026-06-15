# vllm-project/vllm#6201: [Bug]: vLLM 0.5.1 tensor parallel 2 stuck with Mixtral-8x7B-Instruct-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#6201](https://github.com/vllm-project/vllm/issues/6201) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.5.1 tensor parallel 2 stuck with Mixtral-8x7B-Instruct-v0.1

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2.1-11) Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.17 Python version: 3.9.16 (main, Aug 15 2023, 19:38:56) [GCC 8.3.1 20190311 (Red Hat 8.3.1-3)] (64-bit runtime) Python platform: Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.103.01 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.9.2 /usr/lib64/libcudnn_adv_infer.so.8.9.2 /usr/lib64/libcudnn_adv_train.so.8.9.2 /usr/lib64/libcudnn_cnn_infer.so.8.9.2 /usr/lib64/libcudnn_cnn_train.so.8.9.2 /usr/lib64/libcudnn_ops_infer.so.8.9.2 /usr/lib64/libcudnn_ops_train.so.8.9.2 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little E...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ral-8x7B-Instruct-v0.1 bug ### Your current environment ```text PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of relevant libraries: [pip3] flake...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of rel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.103.01 cuDNN version: Probably one o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
