# vllm-project/vllm#20441: [Bug]: DSR1 with DEP OOM during initialization on 32xH100

| 字段 | 值 |
| --- | --- |
| Issue | [#20441](https://github.com/vllm-project/vllm/issues/20441) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DSR1 with DEP OOM during initialization on 32xH100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to run DSR1 with DEP32 with HT kernels, my run cmd looks like this (on node 2): ```bash VLLM_ALL2ALL_BACKEND="deepep_high_throughput" \ VLLM_USE_DEEP_GEMM=1 \ VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 \ --data_parallel_size 32 \ --data-parallel-size-local 8 \ --enable-expert-parallel \ --max-model-len 10240 \ --enforce-eager \ --data-parallel-address eos0391 \ --data-parallel-rpc-port 13345 \ --data-parallel-start-rank 8 \ --headless \ | tee ./dsr1_dep32_node2.log ``` I am able to run with max model len 128, but not even 10240 on 32 H100s due to OOM, which doesn't seem right. Low latency kernel works fine. Is that expected? I have seen https://github.com/vllm-project/vllm/pull/19298 was addressing this issue but I still get OOM errors @varun-sundar-rabindranath . I have attached the logs. OOM error in logs from node 4. [dsr1_dep32_node4.log](https://github.com/user-attachments/files/21038108/dsr1_dep32_node4.log) [dsr1_dep32_node3.log](https://github.com/user-attachments/files/21038109/dsr1_dep32_node3.log) [dsr1_dep32_node2.log](https://github.com/user-attachments/files/21038107/dsr1_dep32_node2...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: looks like this (on node 2): ```bash VLLM_ALL2ALL_BACKEND="deepep_high_throughput" \ VLLM_USE_DEEP_GEMM=1 \ VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 \ --data_parallel_size 32 \ --data-parall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: DSR1 with DEP OOM during initialization on 32xH100 bug;stale ### Your current environment ### 🐛 Describe the bug I try to run DSR1 with DEP32 with HT kernels, my run cmd looks like this (on node 2): ```bash VLLM_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ```bash VLLM_ALL2ALL_BACKEND="deepep_high_throughput" \ VLLM_USE_DEEP_GEMM=1 \ VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 \ --data_parallel_size 32 \ --data-parallel-size-local 8 \ --enable-ex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: T kernels, my run cmd looks like this (on node 2): ```bash VLLM_ALL2ALL_BACKEND="deepep_high_throughput" \ VLLM_USE_DEEP_GEMM=1 \ VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 \ --data_parallel_s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: DSR1 with DEP OOM during initialization on 32xH100 bug;stale ### Your current environment ### 🐛 Describe the bug I try to run DSR1 with DEP32 with HT kernels, my run cmd looks like this (on node 2): ```bash VLLM_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
