# vllm-project/vllm#29306: [Usage]: dots.llm.inst is not running due to a type error

| 字段 | 值 |
| --- | --- |
| Issue | [#29306](https://github.com/vllm-project/vllm/issues/29306) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;scheduler_memory |
| 子分类 | debug |
| Operator 关键词 | cuda;moe |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: dots.llm.inst is not running due to a type error

### Issue 正文摘录

### Your current environment I'm trying to run dots llm on 4xH100 ``` vllm serve \ --uvicorn-log-level=info \ rednote-hilab/dots.llm1.inst \ --dtype auto \ --api-key xxx \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 4 --ipc=host \ --trust-remote-code ``` It failed to run, I got the following crash: ```text (EngineCore_DP0 pid=10684) ERROR 11-24 09:41:25 [v1/executor/multiproc_executor.py:230] Worker proc VllmWorker-1 died unexpectedly, shutting down executor. (EngineCore_DP0 pid=10684) Process EngineCore_DP0: (EngineCore_DP0 pid=10684) Traceback (most recent call last): (EngineCore_DP0 pid=10684) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=10684) self.run() (EngineCore_DP0 pid=10684) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=10684) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=10684) File "/home/ubuntu/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 846, in run_engine_core (EngineCore_DP0 pid=10684) raise e (EngineCore_DP0 pid=10684) File "/home/ubuntu/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 833, in run_engine_co...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rror usage ### Your current environment I'm trying to run dots llm on 4xH100 ``` vllm serve \ --uvicorn-log-level=info \ rednote-hilab/dots.llm1.inst \ --dtype auto \ --api-key xxx \ --host 0.0.0.0 \ --port 8000 \ --ten...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ore_DP0 pid=11385) ERROR 11-24 09:45:27 [v1/engine/core.py:842] self.experts(hidden_states=hidden_states, router_logits=router_logits) (EngineCore_DP0 pid=11385) ERROR 11-24 09:45:27 [v1/engine/core.py:842] ', please ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: (EngineCore_DP0 pid=10684) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=10684) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=10684) File "/home/ubuntu/venv/lib/pyth...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: M_PLUGINS` to control which plugins to load. INFO 11-24 09:45:40 [config/scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. 0.11.2 ``` ### How would you like to use vllm I am not sure what wo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y:225] Automatically detected platform cuda. DEBUG 11-24 09:45:39 [utils/flashinfer.py:45] flashinfer-cubin package was not found DEBUG 11-24 09:45:40 [entrypoints/utils.py:175] Setting VLLM_WORKER_MULTIPROC_METHOD to '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
