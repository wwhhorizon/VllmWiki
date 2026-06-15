# vllm-project/vllm#28456: [Usage]: benchmark_moe Usage

| 字段 | 值 |
| --- | --- |
| Issue | [#28456](https://github.com/vllm-project/vllm/issues/28456) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: benchmark_moe Usage

### Issue 正文摘录

### Your current environment ```text (EngineCore_DP0 pid=7498) INFO 11-10 11:42:48 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). (APIServer pid=7416) INFO 11-10 11:42:50 [loggers.py:127] Engine 000: Avg prompt throughput: 104162.6 tokens/s, Avg generation throughput: 10.0tokens/s, Running: 100 reqs, Waiting: 0 reqs, GPU KV cache usage: 10.1%, Prefix cache hit rate: 98.6% (APIServer pid=7416) INFO 11-10 11:43:00 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 100 reqs, Waiting: 0 reqs, GPU KV cache usage: 10.1%, Prefix cache hit rate: 98.6% (APIServer pid=7416) INFO 11-10 11:43:20 [loggers.py:127] Engine 000: Avg prompt throughput: 5.1 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 98.6% Collecting environment information...============================== System Info============================== OS : Ubuntu 24.04.3 LTS (x86_64)GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========== OS : Ubuntu 24.04.3 LTS (x86_64)GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collectCMake version : version 3.28.3 Libc version : glibc-2.39 ===================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ache usage: 0.1%, Prefix cache hit rate: 98.6% Collecting environment information...============================== System Info============================== OS : Ubuntu 24.04.3 LTS (x86_64)GCC version : (Ubuntu 13.3.0-6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Usage]: benchmark_moe Usage usage;stale ### Your current environment ```text (EngineCore_DP0 pid=7498) INFO 11-10 11:42:48 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: h version : 2.8.0+cu128Is debug build : False CUDA used to build PyTorch : 12.8ROCM used to build PyTorch : N/A ============================== Python Environment============================== Python version : 3.12.3 (ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
