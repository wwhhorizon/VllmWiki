# vllm-project/vllm#14201: [Usage]: How to enforce think for deepseek-r1?

| 字段 | 值 |
| --- | --- |
| Issue | [#14201](https://github.com/vllm-project/vllm/issues/14201) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to enforce think for deepseek-r1?

### Issue 正文摘录

### Your current environment Hi, according to [deepseek-r1](https://huggingface.co/deepseek-ai/DeepSeek-R1), _"To ensure that the model engages in thorough reasoning, we recommend enforcing the model to initiate its response with " \n" at the beginning of every output."_ . How could I do to add " \n" like [ktransformers](https://github.com/kvcache-ai/ktransformers/blob/f46b3fd51ce1c555dd4afffc3a77d5de02759c0d/ktransformers/server/backend/interfaces/transformers.py#L380-L384)? ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.36 Python version: 3.12.9 (main, Feb 6 2025, 22:36:39) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-5.4.0-42-generic-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: o ensure that the model engages in thorough reasoning, we recommend enforcing the model to initiate its response with " \n" at the beginning of every output."_ . How could I do to add " \n" like [ktransformers](https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: #L380-L384)? ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age ### Your current environment Hi, according to [deepseek-r1](https://huggingface.co/deepseek-ai/DeepSeek-R1), _"To ensure that the model engages in thorough reasoning, we recommend enforcing the model to initiate its...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rmers/blob/f46b3fd51ce1c555dd4afffc3a77d5de02759c0d/ktransformers/server/backend/interfaces/transformers.py#L380-L384)? ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Virtualization: AMD-V L1d cache: 4 MiB (128...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
