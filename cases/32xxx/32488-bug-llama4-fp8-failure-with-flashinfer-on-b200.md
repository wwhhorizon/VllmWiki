# vllm-project/vllm#32488: [Bug]: Llama4 FP8 failure with Flashinfer on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#32488](https://github.com/vllm-project/vllm/issues/32488) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama4 FP8 failure with Flashinfer on B200

### Issue 正文摘录

### Your current environment Tried with both trtllm and cutlass moe in flashinfer. Neither seems to work. ### 🐛 Describe the bug Flashinfer Cutlass MoE command: ``` SAFETENSORS_FAST_GPU=1 \ TORCH_SHOW_CPP_STACKTRACES=1 \ VLLM_DISABLE_PYNCCL=1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ VLLM_FORCE_TORCH_ALLREDUCE=1 \ VLLM_GPU_MEMORY_UTILIZATION=0.88 \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ vllm serve /data/local/models/Llama-4-Maverick-17B-128E-Instruct-FP8/ \ --gpu-memory-utilization 0.85 \ --kv-cache-dtype fp8 \ --max-num-seqs 128 \ --max-model-len 8192 \ --max-num-batched-tokens 8192 \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \ 2>&1 | tee ~/mylogs/llama4_oss.log ``` ``` [0;36m(Worker_TP1_EP1 pid=1616078)[0;0m ERROR 01-16 10:34:07 [multiproc_executor.py:822] File "/data/users/mxz/gitrepos/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 1209, in forward [0;36m(Worker_TP1_EP1 pid=1616078)[0;0m ERROR 01-16 10:34:07 [multiproc_executor.py:822] fused_out = self._fused_experts( [0;36m(Worker_TP1_EP1 pid=1616078)[0;0m ERROR 01-16 10:34:07 [multiproc_executor.py:822] ^^^^^^^^^^^^^^^^^^^^ [0;36m(Wo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Llama4 FP8 failure with Flashinfer on B200 bug;stale ### Your current environment Tried with both trtllm and cutlass moe in flashinfer. Neither seems to work. ### 🐛 Describe the bug Flashinfer Cutlass MoE command...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Llama4 FP8 failure with Flashinfer on B200 bug;stale ### Your current environment Tried with both trtllm and cutlass moe in flashinfer. Neither seems to work. ### 🐛 Describe the bug Flashinfer Cutlass MoE command...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Llama4 FP8 failure with Flashinfer on B200 bug;stale ### Your current environment Tried with both trtllm and cutlass moe in flashinfer. Neither seems to work. ### 🐛 Describe the bug Flashinfer Cutlass MoE command...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama4 FP8 failure with Flashinfer on B200 bug;stale ### Your current environment Tried with both trtllm and cutlass moe in flashinfer. Neither seems to work. ### 🐛 Describe the bug Flashinfer Cutlass MoE command...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: _CPP_STACKTRACES=1 \ VLLM_DISABLE_PYNCCL=1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ VLLM_FORCE_TORCH_ALLREDUCE=1 \ VLLM_GPU_MEMORY_UTILIZATION=0.88 \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ vllm serve /data/local/models/Llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
