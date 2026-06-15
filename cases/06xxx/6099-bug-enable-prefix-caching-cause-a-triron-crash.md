# vllm-project/vllm#6099: [Bug]: enable_prefix_caching cause a triron crash

| 字段 | 值 |
| --- | --- |
| Issue | [#6099](https://github.com/vllm-project/vllm/issues/6099) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable_prefix_caching cause a triron crash

### Issue 正文摘录

### Your current environment `Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9) Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.17 Python version: 3.9.16 (main, Jul 10 2023, 11:13:07) [GCC 8.3.1 20190311 (Red Hat 8.3.1-3)] (64-bit runtime) Python platform: Linux-4.18.0-147.20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.103.01 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.9.2 /usr/lib64/libcudnn_adv_infer.so.8.9.2 /usr/lib64/libcudnn_adv_train.so.8.9.2 /usr/lib64/libcudnn_cnn_infer.so.8.9.2 /usr/lib64/libcudnn_cnn_train.so.8.9.2 /usr/lib64/libcudnn_ops_infer.so.8.9.2 /usr/lib64/libcudnn_ops_train.so.8.9.2 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment `Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 11.2.1 20220127 (Red Hat 11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: triron crash bug ### Your current environment `Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of relevant libraries: [pip3] mypy-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .3.0+cu118 [pip3] torchvision==0.14.1 [pip3] transformers==4.41.1 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu11==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
