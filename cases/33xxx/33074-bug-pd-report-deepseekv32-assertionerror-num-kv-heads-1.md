# vllm-project/vllm#33074: [Bug]: PD report DeepseekV32 AssertionError: num_kv_heads == 1

| 字段 | 值 |
| --- | --- |
| Issue | [#33074](https://github.com/vllm-project/vllm/issues/33074) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PD report DeepseekV32 AssertionError: num_kv_heads == 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running command ```bash export VLLM_USE_FLASHINFER_MOE_FP4=0 export CUDA_VISIBLE_DEVICES=0,1 export UCX_NET_DEVICES=all export VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/nfs/models/nvidia/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 2 --no-enable-prefix-caching \ --max-num-batched-tokens 20480 --tokenizer-mode deepseek_v32 --async-scheduling --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_load_failure_policy":"fail"}' ``` error log ```bash (Worker_TP0 pid=370908) DEBUG 01-26 09:28:29 [distributed/.../v1/nixl_connector.py:1010] Detected attention backend DEEPSEEK_V32_INDEXER (Worker_TP0 pid=370908) DEBUG 01-26 09:28:29 [distributed/.../v1/nixl_connector.py:1011] Detected kv cache layout NHD (Worker_TP0 pid=370908) ERROR 01-26 09:28:29 [v1/executor/multiproc_executor.py:852] WorkerProc hit an exception. (Worker_TP0 pid=370908) ERROR 01-26 09:28:29 [v1/executor/multiproc_executor.py:852] Traceback (most recent call last): (Worker_TP0 pid=370908) ERROR 01-26 09:28:29 [v1/executor/multiproc_executor.py:852] File "/home/vllm/nicole-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 847, in worker_b...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Describe the bug running command ```bash export VLLM_USE_FLASHINFER_MOE_FP4=0 export CUDA_VISIBLE_DEVICES=0,1 export UCX_NET_DEVICES=all export VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/nfs/models/nvidia/DeepSeek-V3.2-NV...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ment ### 🐛 Describe the bug running command ```bash export VLLM_USE_FLASHINFER_MOE_FP4=0 export CUDA_VISIBLE_DEVICES=0,1 export UCX_NET_DEVICES=all export VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/nfs/models/nvidia/DeepS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 6 09:28:29 [distributed/.../v1/nixl_connector.py:1011] Detected kv cache layout NHD (Worker_TP0 pid=370908) ERROR 01-26 09:28:29 [v1/executor/multiproc_executor.py:852] WorkerProc hit an exception. (Worker_TP0 pid=37090...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: PD report DeepseekV32 AssertionError: num_kv_heads == 1 bug;stale ### Your current environment ### 🐛 Describe the bug running command ```bash export VLLM_USE_FLASHINFER_MOE_FP4=0 export CUDA_VISIBLE_DEVICES=0,1 e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
