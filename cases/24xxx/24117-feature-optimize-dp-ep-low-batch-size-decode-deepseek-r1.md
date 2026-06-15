# vllm-project/vllm#24117: [Feature]: Optimize DP/EP Low Batch Size Decode DeepSeek-R1

| 字段 | 值 |
| --- | --- |
| Issue | [#24117](https://github.com/vllm-project/vllm/issues/24117) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize DP/EP Low Batch Size Decode DeepSeek-R1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - batch 1 decode traces for DeepSeek are very bad - deployment config: ```bash vllm serve \ deepseek-ai/DeepSeek-V3-0324 \ --port 8200 \ --disable-log-requests \ --disable-uvicorn-access-log \ --enable-expert-parallel \ --data-parallel-hybrid-lb \ --tensor-parallel-size 1\ --data-parallel-size 8 \ --data-parallel-size-local 8 \ --data-parallel-address ${LWS_LEADER_ADDRESS} \ --data-parallel-rpc-port 5555 \ --data-parallel-start-rank 0 \ --trust-remote-code \ --max-model-len 8192 \ --async-scheduling \ -O '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \ --enable-microbatching ``` - env: ``` yaml - name: VLLM_MOE_DP_CHUNK_SIZE value: "512" - name: DP_SIZE_LOCAL value: "8" - name: TRITON_LIBCUDA_PATH value: "/usr/lib64" - name: VLLM_SKIP_P2P_CHECK value: "1" - name: VLLM_RANDOMIZE_DP_DUMMY_INPUTS value: "1" - name: VLLM_USE_DEEP_GEMM value: "1" - name: VLLM_ALL2ALL_BACKEND value: "deepep_low_latency" - name: NVIDIA_GDRCOPY value: "enabled" - name: NVSHMEM_DEBUG value: "INFO" - name: NVSHMEM_REMOTE_TRANSPORT value: "ibgda" - name: NVSHMEM_IB_ENABLE_IBGDA value: "true" - name: NVSHMEM_BOOTSTRAP_UID_SOCK_IFNAME value: "eth0" - name: GLOO_SOCKET_IFNAME v...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: itch - batch 1 decode traces for DeepSeek are very bad - deployment config: ```bash vllm serve \ deepseek-ai/DeepSeek-V3-0324 \ --port 8200 \ --disable-log-requests \ --disable-uvicorn-access-log \ --enable-expert-paral...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: quests \ --disable-uvicorn-access-log \ --enable-expert-parallel \ --data-parallel-hybrid-lb \ --tensor-parallel-size 1\ --data-parallel-size 8 \ --data-parallel-size-local 8 \ --data-parallel-address ${LWS_LE
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Optimize DP/EP Low Batch Size Decode DeepSeek-R1 feature request;stale ### 🚀 The feature, motivation and pitch - batch 1 decode traces for DeepSeek are very bad - deployment config: ```bash vllm serve \ deeps...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e: "1" - name: VLLM_ALL2ALL_BACKEND value: "deepep_low_latency" - name: NVIDIA_GDRCOPY value: "enabled" - name: NVSHMEM_DEBUG value: "INFO" - name: NVSHMEM_REMOTE_TRANSPORT value: "ibgda" - name: NVSHMEM_IB_ENABLE
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "512" - name: DP_SIZE_LOCAL value: "8" - name: TRITON_LIBCUDA_PATH value: "/usr/lib64" - name: VLLM_SKIP_P2P_CHECK value: "1" - name: VLLM_RANDOMIZE_DP_DUMMY_INPUTS value: "1" - name: VLLM_USE_DEEP_GEMM

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
