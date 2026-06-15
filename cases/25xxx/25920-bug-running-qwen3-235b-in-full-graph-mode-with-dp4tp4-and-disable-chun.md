# vllm-project/vllm#25920: [Bug]: Running qwen3-235b in full graph mode with dp4tp4 and disable chunked_prefill will cause  inference hang

| 字段 | 值 |
| --- | --- |
| Issue | [#25920](https://github.com/vllm-project/vllm/issues/25920) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Running qwen3-235b in full graph mode with dp4tp4 and disable chunked_prefill will cause  inference hang

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using these pr: https://github.com/vllm-project/vllm-ascend/pull/3208 https://github.com/vllm-project/vllm-ascend/pull/3102 And ensure that uniform_decode is set to false in with_prefill request in _dummy_run ``` python -m vllm.entrypoints.openai.api_server \ --model="/mnt/weight/Qwen3-235B-A22B" \ --trust-remote-code \ -dp 4 \ --tensor-parallel-size 4 \ --max-model-len 16800 \ --port 8000 \ --no-enable-expert-parallel \ --no-enable-prefix-caching \ --max-num-seqs 512 \ --gpu-memory-utilization 0.9 \ --compilation-config='{"cudagraph_capture_sizes": [512,448,384,320,256,192,160,128,96,64,48,32,8,4,1], "cudagraph_mode": "FULL_DECODE_ONLY"}' \ --additional-config='{"ascend_scheduler_config":{"enabled": true, "enable_chunked_prefill":false, "chunked_prefill_enabled":false}}' ``` Send 10,000 requests at once. After returning a few hundred successfully, the service gets stuck and reports a timeout error. No errors are reported in the plog. ``` File "/vllm/vllm/v1/executor/multiproc_executor.py", line 269, in collective_rpc (EngineCore_DP3 pid=1852080) ERROR 09-29 14:42:29 [core.py:720] raise TimeoutError(f"RPC call to {method} timed o...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: Running qwen3-235b in full graph mode with dp4tp4 and disable chunked_prefill will cause inference hang bug;stale ### Your current environment ### 🐛 Describe the bug Using these pr: https://github.com/vllm-project/vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Running qwen3-235b in full graph mode with dp4tp4 and disable chunked_prefill will cause inference hang bug;stale ### Your current environment ### 🐛 Describe the bug Using these pr: https://github.com/vllm-projec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2 \ --gpu-memory-utilization 0.9 \ --compilation-config='{"cudagraph_capture_sizes": [512,448,384,320,256,192,160,128,96,64,48,32,8,4,1], "cudagraph_mode": "FULL_DECODE_ONLY"}' \ --additional-config='{"ascend_scheduler_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: project/vllm-ascend/pull/3102 And ensure that uniform_decode is set to false in with_prefill request in _dummy_run ``` python -m vllm.entrypoints.openai.api_server \ --model="/mnt/weight/Qwen3-235B-A22B" \ --trust-remot...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: \ --max-model-len 16800 \ --port 8000 \ --no-enable-expert-parallel \ --no-enable-prefix-caching \ --max-num-seqs 512 \ --gpu-memory-utilization 0.9 \ --compilation-config='{"cudagraph_capture_sizes": [512,448,384,320,2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
