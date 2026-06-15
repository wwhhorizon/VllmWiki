# vllm-project/vllm#21306: [Bug]: all2all communication hangs when using DeepEP and PPLX for v0.9.2

| 字段 | 值 |
| --- | --- |
| Issue | [#21306](https://github.com/vllm-project/vllm/issues/21306) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: all2all communication hangs when using DeepEP and PPLX for v0.9.2

### Issue 正文摘录

### Your current environment See as below. ### 🐛 Describe the bug Dear all, we are trying to run large-scale EP (across DP) with **DeepEP**, using the [deepep dockerfile](https://github.com/sgl-project/sglang/blob/v0.4.7/docker/Dockerfile.deepep) provided by SGLang. **testbed:** 2 nodes, each with 8 GPUs (H20-141 GB). mlx5 IB card with IBGDA enabled. **model:** deepseek_r1 We have `nvidia_peermem` and `gdr driver` installed in the host. We can successfully run DeepEP internode benchmark with high_throughput and low_latency kernels (IBGDA enabled). However, when we are running **vLLM-v0.9.2** `dp=2, tp=8, ep=16`, with all2all backend set to `deepep_low_latency` or `deepep_high_throughput`. We found the process hangs when doing warm-up requests. The script we use is [offline_inference/data_parallel.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/data_parallel.py). We trace the code and find that the first MoE layer can complete the `dispatch -> expert compute -> combine` process. But in the second MoE layer, workers hang when calling `dispatch` ([here](https://github.com/vllm-project/vllm/blob/d97841078b6e0dde8da36d5a2b8e8857a2c37944/vllm/model_executor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing to run large-scale EP (across DP) with **DeepEP**, using the [deepep dockerfile](https://github.com/sgl-project/sglang/blob/v0.4.7/docker/Dockerfile.deepep) provided by SGLang. **testbed:** 2 nodes, each with 8 GPUs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: oject/sglang/blob/v0.4.7/docker/Dockerfile.deepep) provided by SGLang. **testbed:** 2 nodes, each with 8 GPUs (H20-141 GB). mlx5 IB card with IBGDA enabled. **model:** deepseek_r1 We have `nvidia_peermem` and `gdr drive...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: r, when we are running **vLLM-v0.9.2** `dp=2, tp=8, ep=16`, with all2all backend set to `deepep_low_latency` or `deepep_high_throughput`. We found the process hangs when doing warm-up requests. The script we use is [off...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nodes, each with 8 GPUs (H20-141 GB). mlx5 IB card with IBGDA enabled. **model:** deepseek_r1 We have `nvidia_peermem` and `gdr driver` installed in the host. We can successfully run DeepEP internode benchmark with high...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: _inference/data_parallel.py). We trace the code and find that the first MoE layer can complete the `dispatch -> expert compute -> combine` process. But in the second MoE layer, workers hang when calling `dispatch` ([her...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
