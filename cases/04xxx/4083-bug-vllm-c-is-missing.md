# vllm-project/vllm#4083: [Bug]: vllm_C is missing. 

| 字段 | 值 |
| --- | --- |
| Issue | [#4083](https://github.com/vllm-project/vllm/issues/4083) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm_C is missing. 

### Issue 正文摘录

### Your current environment Previous fix from https://github.com/vllm-project/vllm/pull/3913 did not seem to work. Same issue still encountered. ```text Collecting environment information... INFO 04-15 07:13:37 pynccl.py:58] Loading nccl from library /home/me/.config/vllm/nccl/cu12/libnccl.so.2.18.1 PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: 11.0.1-2 CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.9.2 (default, Feb 28 2021, 17:03:44) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.16.0-0.bpo.4-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Could not collect HIP runtime version: N/A M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: l from library /home/me/.config/vllm/nccl/cu12/libnccl.so.2.18.1 PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: u12/libnccl.so.2.18.1 PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm Versio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: cl/cu12/libnccl.so.2.18.1 PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: o work. Same issue still encountered. ```text Collecting environment information... INFO 04-15 07:13:37 pynccl.py:58] Loading nccl from library /home/me/.config/vllm/nccl/cu12/libnccl.so.2.18.1 PyTorch version: 2.1.2+cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
