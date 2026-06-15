# vllm-project/vllm#37404: [Bug]: AssertionError: assert num_kv_heads == 1 with CPU KV Offloading + GLM-5-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#37404](https://github.com/vllm-project/vllm/issues/37404) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: assert num_kv_heads == 1 with CPU KV Offloading + GLM-5-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve zai-org/GLM-5-FP8" --gpu-memory-utilization 0.85 \ ---enable-auto-tool-choice \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --default-chat-template-kwargs {"enable_thinking": false} \ --tensor-parallel-size 8 \ --performance-mode interactivity \ --kv-offloading-size 1000 \ --disable-hybrid-kv-cache-manager ``` AssertionError in mla/indexer.py when using kv_offloading_size with MLA attention model (GLM-5-FP8) (Worker_TP6 pid=604) INFO 03-17 22:03:06 factory.py:51] Creating offloading spec with name: CPUOffloadingSpec (Worker_TP7 pid=605) WARNING 03-17 22:03:06 spec.py:25] Initializing OffloadingSpec. This API is experimental and subject to change in the future as we iterate the design. (Worker_TP4 pid=602) ERROR 03-17 22:03:06 multiproc_executor.py:932] WorkerProc hit an exception. (Worker_TP4 pid=602) ERROR 03-17 22:03:06 multiproc_executor.py:932] Traceback (most recent call last): (Worker_TP4 pid=602) ERROR 03-17 22:03:06 multiproc_executor.py:932] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 927, in worker_busy_loop (Worker_TP4 pid=602) ERROR 03-17 22:03:0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: executor.py:932] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_TP4 pid=602) ERROR 03-17 22:03:06 multiproc_executor.py:932] return func(*args, **kwargs) (Worker_T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: AssertionError: assert num_kv_heads == 1 with CPU KV Offloading + GLM-5-FP8 bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve zai-org/GLM-5-FP8" --gpu-memory-utilization 0.85 \ ---enable-auto-tool-c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 6 multiproc_executor.py:932] self._register_handlers(kv_caches, attn_backends) (Worker_TP4 pid=602) ERROR 03-17 22:03:06 multiproc_executor.py:932] File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: = 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: AssertionError: assert num_kv_heads == 1 with CPU KV Offloading + GLM-5-FP8 bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve zai-org/GLM-5-FP8" --gpu-memory-utilization 0.85 \ ---enable-auto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
