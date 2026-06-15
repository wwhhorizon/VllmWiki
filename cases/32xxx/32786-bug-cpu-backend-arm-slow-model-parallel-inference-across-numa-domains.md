# vllm-project/vllm#32786: [Bug]:  [CPU Backend] [Arm] Slow model-parallel inference across NUMA domains

| 字段 | 值 |
| --- | --- |
| Issue | [#32786](https://github.com/vllm-project/vllm/issues/32786) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  [CPU Backend] [Arm] Slow model-parallel inference across NUMA domains

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On `m8g.metal.48xlarge` which has `2 numa nodes: (numa 0 -> cores 0-95), (numa 2 -> cores 96-191)` the benchmarks below show that serving on single NUMA with 96 cores and tensor-parallel-size=1 is significantly better than serving on 2 NUMAs with 96 cores each and tensor-parallel-size=2 **Benchmark:** ``` #!/usr/bin/env bash set -e export LD_PRELOAD="/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4:/usr/lib/aarch64-linux-gnu/libgomp.so.1" export VLLM_TARGET_DEVICE=cpu export VLLM_CPU_OMP_THREADS_BIND= vllm serve meta-llama/Llama-3.2-3B-Instruct -tp= -dp=1 -pp=1 --no-enable-prefix-caching & SERVER_PID=$! trap "kill $SERVER_PID 2>/dev/null || true" EXIT INT TERM vllm bench serve \ --backend vllm \ --dataset-name random \ --input-len 1024 \ --output-len 128 \ --model meta-llama/Llama-3.2-3B-Instruct \ --num-prompts 64 \ --seed 1 \ --top-k 1 \ --temperature 0 \ --endpoint /v1/completions ``` **Results:** These are percentages of the baseline which is: Single NUMA, tp=1 (96 cores), VLLM_CPU_OMP_THREADS_BIND=0-95 | Configuration | req/sec (higher-better) | median TTFT (lower-better) | median TPOT (lower-better) | |---|---:|---:|---:...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: has `2 numa nodes: (numa 0 -> cores 0-95), (numa 2 -> cores 96-191)` the benchmarks below show that serving on single NUMA with 96 cores and tensor-parallel-size=1 is significantly better than serving on 2 NUMAs with 96...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [CPU Backend] [Arm] Slow model-parallel inference across NUMA domains bug;cpu ### Your current environment ### 🐛 Describe the bug On `m8g.metal.48xlarge` which has `2 numa nodes: (numa 0 -> cores 0-95), (numa 2 -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [CPU Backend] [Arm] Slow model-parallel inference across NUMA domains bug;cpu ### Your current environment ### 🐛 Describe the bug On `m8g.metal.48xlarge` which has `2 numa nodes: (numa 0 -> cores 0-95), (numa 2 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Benchmark:** ``` #!/usr/bin/env bash set -e export LD_PRELOAD="/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4:/usr/lib/aarch64-linux-gnu/libgomp.so.1" export VLLM_TARGET_DEVICE=cpu export VLLM_CPU_OMP_THREADS_BIND=...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: meta-llama/Llama-3.2-3B-Instruct \ --num-prompts 64 \ --seed 1 \ --top-k 1 \ --temperature 0 \ --endpoint /v1/completions ``` **Results:** These are percentages of the baseline which is: Single NUMA, tp=1 (96 cores), VL...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
