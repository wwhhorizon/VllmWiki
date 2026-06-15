# vllm-project/vllm#10389: [Bug]: v0.6.4.post1 crashed：Error in model execution: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#10389](https://github.com/vllm-project/vllm/issues/10389) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.6.4.post1 crashed：Error in model execution: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20241116-081810.zip](https://github.com/user-attachments/files/17784441/err_execute_model_input_20241116-081810.zip) ### 🐛 Describe the bug command ```bash vllm serve /hestia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 32768 --quantization awq_marlin --port 8001 --served-model-name qwen --num-gpu-blocks-override 2048 --disable-log-requests --swap-space 4 --enable-prefix-caching --enable-chunked-prefill ``` ```bash INFO 11-16 10:37:50 metrics.py:449] Avg prompt throughput: 5941.0 tokens/s, Avg generation throughput: 16.5 tokens/s, Running: 3 reqs, Swapped: 0 reqs, Pending: 13 reqs, GPU KV cache usage: 1.5%, CPU KV cache usage: 0.0%. INFO 11-16 10:37:50 metrics.py:465] Prefix cache hit rate: GPU: 94.87%, CPU: 0.00% INFO: ::1:59242 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 11-16 10:37:53 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241116-103753.pkl... WARNING 11-16 10:37:53 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered WARNING 11-16 10:37:53 model_runner_base.py:143] CUDA...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 01 --served-model-name qwen --num-gpu-blocks-override 2048 --disable-log-requests --swap-space 4 --enable-prefix-caching --enable-chunked-prefill ``` ```bash INFO 11-16 10:37:50 metrics.py:449] Avg prompt throughput: 59...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CUDA_LAUNCH_BLOCKING=1 WARNING 11-16 10:37:53 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. WARNING 11-16 10:37:53 model_runner_base.py:143] CRITICAL 11-16 10:37:53 launch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: v0.6.4.post1 crashed：Error in model execution: CUDA error: an illegal memory access was encountered bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20241116-081810.zip](https://git...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 5%, CPU KV cache usage: 0.0%. INFO 11-16 10:37:50 metrics.py:465] Prefix cache hit rate: GPU: 94.87%, CPU: 0.00% INFO: ::1:59242 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 11-16 10:37:53 model_runner_base.py:120...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: : 16.5 tokens/s, Running: 3 reqs, Swapped: 0 reqs, Pending: 13 reqs, GPU KV cache usage: 1.5%, CPU KV cache usage: 0.0%. INFO 11-16 10:37:50 metrics.py:465] Prefix cache hit rate: GPU: 94.87%, CPU: 0.00% INFO: ::1:59242...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
