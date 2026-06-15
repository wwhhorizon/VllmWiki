# vllm-project/vllm#40983: [Bug]: arange_buffer size mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#40983](https://github.com/vllm-project/vllm/issues/40983) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;kernel;moe |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: arange_buffer size mismatch

### Issue 正文摘录

### Your current environment image: vllm/vllm-openai:deepseekv4-cu129 model: DeepSeek-V4-Pro GPU: 16 * H200 ### 🐛 Describe the bug ``` (Worker_DP14_EP14 pid=3379) 2026-04-27 06:31:12 [TileLang:tilelang.jit.kernel:INFO]: TileLang completes to compile kernel `mhc_pre_big_fuse_tilelang` (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] WorkerProc hit an exception. (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] Traceback (most recent call last): (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 966, in worker_busy_loop (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] output = func(*args, **kwargs) (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 896, in execute_dummy_batch (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] self.model_runner._dummy_run(nu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -27 06:31:12 [TileLang:tilelang.jit.kernel:INFO]: TileLang completes to compile kernel `mhc_pre_big_fuse_tilelang` (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] WorkerProc hit an exception...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e deepseek-ai/DeepSeek-V4-Pro --port 8000 --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-hybrid-lb --data-parallel-size 16 --data-parallel-size-local 8 --data-parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: arange_buffer size mismatch bug;DSv4 ### Your current environment image: vllm/vllm-openai:deepseekv4-cu129 model: DeepSeek-V4-Pro GPU: 16 * H200 ### 🐛 Describe the bug ``` (Worker_DP14_EP14 pid=3379) 2026-04-27 0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] attn_metadata, _ = self._build_attention_metadata( (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] ^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y:971] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/indexer.py", line 508, in build (Worker_DP14_EP14 pid=3379) ERROR 04-27 06:33:46 [multiproc_executor.py:971] self._prepare_decode_tenso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
