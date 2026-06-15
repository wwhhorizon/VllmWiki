# vllm-project/vllm#43563: [Usage]: Intel Xeon Prefill Decode Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#43563](https://github.com/vllm-project/vllm/issues/43563) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Intel Xeon Prefill Decode Disaggregation

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Mar 3 2026, 11:56:32) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-177-generic-x86_64-with-glibc2.35 ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) 6767P CPU family: 6 Model: 173 Thread(s) per core: 2 Core(s) per socket: 64 Socket(s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: h version : 2.11.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Intel Xeon Prefill Decode Disaggregation usage ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... ============================== System Info ===...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cudnn-frontend==1.18.0 [pip3] nvidia-cutlass-dsl==4.4.2 [pip3] nvidia-cutlass-dsl...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
