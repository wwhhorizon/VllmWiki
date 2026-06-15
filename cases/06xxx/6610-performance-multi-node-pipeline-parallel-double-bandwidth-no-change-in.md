# vllm-project/vllm#6610: [Performance]: Multi-node Pipeline Parallel double bandwidth, no change in performance

| 字段 | 值 |
| --- | --- |
| Issue | [#6610](https://github.com/vllm-project/vllm/issues/6610) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Multi-node Pipeline Parallel double bandwidth, no change in performance

### Issue 正文摘录

### Misc discussion on performance I've been running some simple tests on multi-node parallel pipeline with NCCL. I doubled the bandwidth between the nodes but saw no increase in t/s or throughput. I tested with 400Gbps and 800Gbps between nodes and was getting the same t/s, although [nccl-tests](https://github.com/NVIDIA/nccl-tests) showed the 2x bandwidth between GPUs. ## Questions: 1. What would be the bottleneck in multi-node parallel pipelines, if not inter-node connectivity? 2. What other tests or profiling can be done to figure out the bottleneck on parallel pipelines? 3. Are there currently any benchmarks in vllm (such as `benchmark_throughput.py` or `benchmark_latency.py`) that can be run with `--pipeline-parallel-size` (required Async: `Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise.`)? ## Environment: (2) x GH200 nodes (aarch64) - 800Gbps Ethernet between nodes **Model:** L3-70B-Instruct ## Test 1: (4)x 200Gbps Connections (800Gbps total) ### NCCL-Test: Execution Command ``` mpirun -np 2 -host localhost,10.5.6.103 ./build/{all_reduce_perf,all_gather_perf,alltoall_perf} -b 512k -e 1024M -f 2 -g 1 ``` NCCL...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: CL-Test: Execution Command ``` mpirun -np 2 -host localhost,10.5.6.103 ./build/{all_reduce_perf,all_gather_perf,alltoall_perf} -b 512k -e 1024M -f 2 -g 1 ``` NCCL Test (all_reduce_perf): algbw = 70.83GB/s, busbw = 70.83...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Pipeline Parallel double bandwidth, no change in performance performance;stale ### Misc discussion on performance I've been running some simple tests on multi-node parallel pipeline with NCCL. I doubled the bandwidth be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: run with `--pipeline-parallel-size` (required Async: `Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise.`)? ## Environment: (2) x GH200 nodes (aarch64) - 80...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ;stale ### Misc discussion on performance I've been running some simple tests on multi-node parallel pipeline with NCCL. I doubled the bandwidth between the nodes but saw no increase in t/s or throughput. I tested with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
