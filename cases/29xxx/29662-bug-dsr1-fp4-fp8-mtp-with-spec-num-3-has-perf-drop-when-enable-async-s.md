# vllm-project/vllm#29662: [Bug]: DSR1 fp4/fp8 MTP with spec num 3 has perf drop when enable async-scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#29662](https://github.com/vllm-project/vllm/issues/29662) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 fp4/fp8 MTP with spec num 3 has perf drop when enable async-scheduling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 machine. Found the regression caused by https://github.com/vllm-project/vllm/pull/24799. FP8 with --async-scheduling, Output token throughput (tok/s): 1994 without --async-scheduling, Output token throughput (tok/s): 2421 FP4 with --async-scheduling, Output token throughput (tok/s): 2375 without --async-scheduling, Output token throughput (tok/s): 2895 Repro command FP8 export VLLM_USE_NCCL_SYMM_MEM=1 export NCCL_NVLS_ENABLE=1 export NCCL_CUMEM_ENABLE=1 export VLLM_USE_TRTLLM_RAGGED_DEEPSEEK_PREFILL=1 export VLLM_ATTENTION_BACKEND=FLASHINFER_MLA export VLLM_FLASHINFER_MOE_BACKEND=latency export VLLM_USE_FLASHINFER_MOE_FP8=1 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model deepseek-ai/DeepSeek-R1-0528 --tokenizer deepseek-ai/DeepSeek-R1-0528 --dtype auto --kv-cache-dtype fp8 --tensor-parallel-size 8 --pipeline-parallel-size 1 --data-parallel-size 1 --swap-space 16 --max-num-seqs 1024 --trust-remote-code --max-model-len 2176 --gpu-memory-utilization 0.9 --max-num-batched-tokens 8192 --no-enable-prefix-caching --async-scheduling --compilation_config.pass_config.enable_fi_allreduce_fu...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: current environment ### 🐛 Describe the bug B200 machine. Found the regression caused by https://github.com/vllm-project/vllm/pull/24799. FP8 with --async-scheduling, Output token throughput (tok/s): 1994 without --async...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: owing repo. git clone https://github.com/kimbochen/bench_serving.git pip install pandas datasets --break-system-packages FP4 export VLLM_USE_NCCL_SYMM_MEM=1 export NCCL_NVLS_ENABLE=1 export NCCL_CUMEM_ENABLE=1 export VL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: DSR1 fp4/fp8 MTP with spec num 3 has perf drop when enable async-scheduling bug;stale ### Your current environment ### 🐛 Describe the bug B200 machine. Found the regression caused by https://github.com/vllm-proje...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 4/fp8 MTP with spec num 3 has perf drop when enable async-scheduling bug;stale ### Your current environment ### 🐛 Describe the bug B200 machine. Found the regression caused by https://github.com/vllm-project/vllm/pull/2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: uling bug;stale ### Your current environment ### 🐛 Describe the bug B200 machine. Found the regression caused by https://github.com/vllm-project/vllm/pull/24799. FP8 with --async-scheduling, Output token throughput (tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
