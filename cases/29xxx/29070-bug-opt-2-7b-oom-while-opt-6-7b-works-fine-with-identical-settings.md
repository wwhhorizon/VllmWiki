# vllm-project/vllm#29070: [Bug]: OPT-2.7B OOM while OPT-6.7B works fine with identical settings

| 字段 | 值 |
| --- | --- |
| Issue | [#29070](https://github.com/vllm-project/vllm/issues/29070) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OPT-2.7B OOM while OPT-6.7B works fine with identical settings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### OPT-2.7B OOM while OPT-6.7B works fine with identical settings ### Describe the bug OPT-2.7B crashes with OOM error while the larger OPT-6.7B model runs successfully under identical configuration. This counterintuitive behavior suggests a memory allocation bug specific to smaller models. ### Observed Behavior | Model | Status | Memory Usage | Throughput | |-------|--------|--------------|------------| | OPT-2.7B | ❌ OOM (crash on first step) | 23.46/23.50 GiB (99.8%) | N/A | | OPT-6.7B | ✅ Success | Normal | 6.58 req/s | **Key Issue**: The smaller 2.7B model exhausts nearly all GPU memory across all 4 GPUs and crashes on the **first decoding step** (step_counter=0), while the larger 6.7B model handles the same workload efficiently. ### Reproduction Script ```bash # Works fine for OPT-6.7B, OOM for OPT-2.7B sudo docker exec vllm vllm bench throughput \ --model facebook/opt-2.7b \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.8 \ --input-len 512 \ --output-len 256 \ --num-prompts 200 ``` ## Error Logs ### OPT-2.7B (Failure) #### Memory Profiling at Initialization ``` [Worker_TP3 pid=540] DEBUG 11-19 21:09:35 [v1/worker/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 8.8 tokens/s, Avg generation throughput: 8.9 tokens/s, Running: 65 reqs, Waiting: 135 reqs, GPU KV cache usage: 15.0%, Prefix cache hit rate: 0.0% INFO 11-19 21:10:13 [v1/metrics/loggers.py:127] Engine 000: Avg prompt t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tion. This counterintuitive behavior suggests a memory allocation bug specific to smaller models. ### Observed Behavior | Model | Status | Memory Usage | Throughput | |-------|--------|--------------|------------| | OPT...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: OPT-2.7B OOM while OPT-6.7B works fine with identical settings bug ### Your current environment ### 🐛 Describe the bug ### OPT-2.7B OOM while OPT-6.7B works fine with identical settings ### Describe the bug OPT-2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s counterintuitive behavior suggests a memory allocation bug specific to smaller models. ### Observed Behavior | Model | Status | Memory Usage | Throughput | |-------|--------|--------------|------------| | OPT-2.7B | ❌...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: maller models. ### Observed Behavior | Model | Status | Memory Usage | Throughput | |-------|--------|--------------|------------| | OPT-2.7B | ❌ OOM (crash on first step) | 23.46/23.50 GiB (99.8%) | N/A | | OPT-6.7B |...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
