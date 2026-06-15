# vllm-project/vllm#29373: [Bug]: Multinode inference request with Ray and vLLM crashes - regression from vLLM v0.7.3

| 字段 | 值 |
| --- | --- |
| Issue | [#29373](https://github.com/vllm-project/vllm/issues/29373) |
| 状态 | open |
| 标签 | bug;ray |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multinode inference request with Ray and vLLM crashes - regression from vLLM v0.7.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray --dtype bfloat16 --gpu-memory-utilization 0.9 --trust-remote-code --served-model-name deepseek-ai/DeepSeek-R1 ``` vLLM loads and warms up cleanly, but the first inference hangs until a Ray compiled-DAG channel times out after 300s and the Raylet dies (RayChannelTimeoutError → ChannelError: Channel closed in deepseek_multinode.log). That points to Ray’s compiled-graph path hanging/crashing rather than an NCCL collective failing. ``` (APIServer pid=37667) INFO 11-24 16:09:24 [launcher.py:46] Route: /ping, Methods: POST (APIServer pid=37667) INFO 11-24 16:09:24 [launcher.py:46] Route: /invocations, Methods: POST (APIServer pid=37667) INFO 11-24 16:09:24 [launcher.py:46] Route: /metrics, Methods: GET (APIServer pid=37667) INFO: Started server process [37667] (APIServer pid=37667) INFO: Waiting for application startup. (APIServer pid=37667) INFO: Application startup complete. (APIServer pid=37667) INFO: 10.2.21.131:56994 - "GET /v1/models HTTP/1.1" 200 OK (APIServer pid=37667) INFO 11-24 16:09:47 [chat_utils.py:557] Detected th...

## 现有链接修复摘要

#41218 fix: convert LogprobsLists to lists for cross node Ray transport (#38602)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Multinode inference request with Ray and vLLM crashes - regression from vLLM v0.7.3 bug;ray ### Your current environment ### 🐛 Describe the bug ``` vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: l-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray --dtype bfloat16 --gpu-memory-utilization 0.9 --trust-remote-code --served-model-name deepseek-ai/DeepSeek-R1 ``` vLLM loads and warms up cleanly, b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: LM loads and warms up cleanly, but the first inference hangs until a Ray compiled-DAG channel times out after 300s and the Raylet dies (RayChannelTimeoutError → ChannelError: Channel closed in deepseek_multinode.log). T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: tensor-parallel-size 8 --pipeline-parallel-size 2 --distributed-executor-backend ray --dtype bfloat16 --gpu-memory-utilization 0.9 --trust-remote-code --served-model-name deepseek-ai/DeepSeek-R1 ``` vLLM loads and warms...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 6:09:48 [ray_executor.py:546] VLLM_USE_RAY_COMPILED_DAG_OVERLAP_COMM = False (EngineCore_DP0 pid=37804) INFO 11-24 16:09:48 [ray_executor.py:605] Using RayPPCommunicator (which wraps vLLM _PP GroupCoordinator) for Ray C...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41218](https://github.com/vllm-project/vllm/pull/41218) | closes_keyword | 0.95 | fix: convert LogprobsLists to lists for cross node Ray transport (#38602) | fix this case. I tested it before going further. - #29373, #37001: related multi node Ray crashes, different code paths. - #38602: the issue this closes. Bisect data and the experi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
