# vllm-project/vllm#12633: [Bug]: shape is invalid for input of size

| 字段 | 值 |
| --- | --- |
| Issue | [#12633](https://github.com/vllm-project/vllm/issues/12633) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: shape is invalid for input of size

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The vllm no longer working on server with MI300X GPU when running model DeepSeek R1 after this commit https://github.com/vllm-project/vllm/commit/cabaf4eff3c7df30d785769d5a0a1fa1a1c48a8a The error is as follows ```text Capturing CUDA graph shapes: 0%| | 0/35 [00:00<?, ?it/s] ERROR 01-31 21:25:22 engine.py:387] shape '[47325, 16, 12, -1, 16]' is invalid for input of size 678451200 ERROR 01-31 21:25:22 engine.py:387] Traceback (most recent call last): ERROR 01-31 21:25:22 engine.py:387] File "/data/vllm/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine ERROR 01-31 21:25:22 engine.py:387] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 01-31 21:25:22 engine.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 01-31 21:25:22 engine.py:387] File "/data/vllm/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args ERROR 01-31 21:25:22 engine.py:387] return cls(ipc_path=ipc_path, ERROR 01-31 21:25:22 engine.py:387] ^^^^^^^^^^^^^^^^^^^^^^ ERROR 01-31 21:25:22 engine.py:387] File "/data/vllm/vllm/engine/multiprocessing/engine.py", line 73...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onse_ ### 🐛 Describe the bug The vllm no longer working on server with MI300X GPU when running model DeepSeek R1 after this commit https://github.com/vllm-project/vllm/commit/cabaf4eff3c7df30d785769d5a0a1fa1a1c48a8a The...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ^^ ERROR 01-31 21:25:22 engine.py:387] File "/data/vllm/vllm/attention/backends/rocm_flash_attn.py", line 612, in forward ERROR 01-31 21:25:22 engine.py:387] key_cache, value_cache = PagedAttention.split_kv_cache( ERROR...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 21:25:22 engine.py:387] self.model_executor.initialize_cache(num_gpu_blocks, num_cpu_blocks) ERROR 01-31 21:25:22 engine.py:387] File "/data/vllm/vllm/executor/executor_base.py", line 119, in initialize_cache ERROR 01-3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: shape is invalid for input of size bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The vllm no longer working on server with MI300X GPU when running model DeepSee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
