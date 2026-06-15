# vllm-project/vllm#37273: [Usage]: Failed to run Qwen3 Eagle3 speculate

| 字段 | 值 |
| --- | --- |
| Issue | [#37273](https://github.com/vllm-project/vllm/issues/37273) |
| 状态 | open |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Failed to run Qwen3 Eagle3 speculate

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (main, Feb 12 2026, 00:42:24) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-5.15.148-tegra-aarch64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: Orin (nvgpu) Nvidia driver version : 540.4.0 cuDNN version : Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.3.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.3.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.3.0 /usr/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ======== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 3.31.10 Libc version : glibc-2.35 ==============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: Failed to run Qwen3 Eagle3 speculate usage ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ub
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 (/opt/venv/lib/python3.10/site-packages) [pip3] numpy==2.2.6 (/opt/venv/lib/python3.10/site-packages) [pip3] nvidia-cudnn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ==================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 3.31.10 Libc version : glibc-2.35 ==
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
