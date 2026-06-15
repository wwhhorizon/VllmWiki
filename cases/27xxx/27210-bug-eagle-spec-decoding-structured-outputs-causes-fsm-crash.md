# vllm-project/vllm#27210: [Bug]: EAGLE Spec Decoding + Structured Outputs causes FSM Crash

| 字段 | 值 |
| --- | --- |
| Issue | [#27210](https://github.com/vllm-project/vllm/issues/27210) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE Spec Decoding + Structured Outputs causes FSM Crash

### Issue 正文摘录

### Your current environment vLLM 0.11.x , on H200s --2025-10-20 22:19:16-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28050 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env. 0% 0 --.-KB/s collect_env. 100% 27.39K --.-KB/s in 0s 2025-10-20 22:19:17 (185 MB/s) - ‘collect_env.py’ saved [28050/28050] Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ==================
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: .com (raw.githubusercontent.com)|185.199.111.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28050 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env. 0% 0 --.-KB/s collect_env. 100...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: EAGLE Spec Decoding + Structured Outputs causes FSM Crash bug ### Your current environment vLLM 0.11.x , on H200s --2025-10-20 22:19:16-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 5 MB/s) - ‘collect_env.py’ saved [28050/28050] Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
