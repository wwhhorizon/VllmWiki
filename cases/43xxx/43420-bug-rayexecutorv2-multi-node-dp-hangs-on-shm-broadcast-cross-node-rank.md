# vllm-project/vllm#43420: [Bug]: RayExecutorV2 multi-node DP hangs on shm_broadcast — cross-node ranks can't share single-host shared memory

| 字段 | 值 |
| --- | --- |
| Issue | [#43420](https://github.com/vllm-project/vllm/issues/43420) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;moe;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RayExecutorV2 multi-node DP hangs on shm_broadcast — cross-node ranks can't share single-host shared memory

### Issue 正文摘录

## Summary `RayExecutorV2` (introduced via PR #36836, "[Feat][Executor] Introduce RayExecutorV2") inherits from `MultiprocExecutor` and uses `shm_broadcast` for inter-rank communication. `shm_broadcast` is single-host shared memory — it has no cross-node path natively. For multi-node DP, vLLM falls back to Gloo TCP for the cross-node bits, which times out after ~30 min: ``` gloo/transport/tcp/unbound_buffer.cc:78 Timed out waiting 1800000ms for recv operation to complete ``` The pre-`RayExecutorV2` `ray_executor.py` uses pure Ray RPC for ALL collective operations — Ray handles cross-node natively via its own RPC layer, no shm. ## Repro Run any MoE model with `data_parallel_size > 1` spanning multiple nodes, leaving `VLLM_USE_V2_MODEL_RUNNER=1` (the default). E.g. MiniMax-M2.7-AWQ-4bit on 2× single-node-TP=4 (DP=2 across two 4×H100/GH200 nodes): ```bash python -m vllm.entrypoints.openai.api_server \ --model cyankiwi/MiniMax-M2.7-AWQ-4bit \ --tensor-parallel-size 4 --data-parallel-size 2 \ --data-parallel-backend ray --data-parallel-size-local 1 \ --data-parallel-address \ --distributed-executor-backend ray \ --trust-remote-code --enforce-eager ``` The job starts, both `DPMoEEngineC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _executor_v2.py`: \`\`\`python from vllm.v1.executor.multiproc_executor import ( FutureWrapper, MultiprocExecutor, WorkerProc, ) # ... class RayExecutorV2(MultiprocExecutor): ... \`\`\` By inheriting from `MultiprocExec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t). E.g. MiniMax-M2.7-AWQ-4bit on 2× single-node-TP=4 (DP=2 across two 4×H100/GH200 nodes): ```bash python -m vllm.entrypoints.openai.api_server \ --model cyankiwi/MiniMax-M2.7-AWQ-4bit \ --tensor-parallel-size 4 --data...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ``` INFO ... [shm_broadcast.py:698] No available shared memory broadcast block found in 600 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: \ --tensor-parallel-size 4 --data-parallel-size 2 \ --data-parallel-backend ray --data-parallel-size-local 1 \ --data-parallel-address \ --distributed-executor-backend ray \ --trust-remote-code --enforce-eager ``` The j...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: es cross-node natively via its own RPC layer, no shm. ## Repro Run any MoE model with `data_parallel_size > 1` spanning multiple nodes, leaving `VLLM_USE_V2_MODEL_RUNNER=1` (the default). E.g. MiniMax-M2.7-AWQ-4bit on 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
