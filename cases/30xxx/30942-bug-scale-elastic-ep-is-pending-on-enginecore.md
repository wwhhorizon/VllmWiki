# vllm-project/vllm#30942: [Bug]: Scale Elastic EP is Pending on EngineCore

| 字段 | 值 |
| --- | --- |
| Issue | [#30942](https://github.com/vllm-project/vllm/issues/30942) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scale Elastic EP is Pending on EngineCore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Commands Run Run ``` vllm serve --model /mnt/Qwen3-30B-A3B/ --data-parallel-size 2 --data-parallel-backend ray --distributed-executor-backend ray --enforce-eager --disable-log-stats ``` and then DP Scale from 2->3. ``` curl -s -X POST http://localhost:8000/scale_elastic_ep -H "Content-Type: application/json" -d '{"new_data_parallel_size": 3}' ``` # Main Program Logs ``` [0;36m(APIServer pid=70686)[0;0m INFO 12-17 23:25:21 [v1/engine/async_llm.py:835] Waiting for requests to drain before scaling up to 3 engines... [0;36m(APIServer pid=70686)[0;0m INFO 12-17 23:25:21 [v1/engine/async_llm.py:806] Engines are idle, requests have been drained [0;36m(APIServer pid=70686)[0;0m INFO 12-17 23:25:21 [v1/engine/async_llm.py:840] Requests have been drained, proceeding with scale to 3 engines [0;36m(APIServer pid=70686)[0;0m INFO 12-17 23:25:21 [v1/engine/core_client.py:1312] All reconfigure messages sent, starting engine creation [0;36m(APIServer pid=70686)[0;0m [36m(pid=99758)[0m DEBUG 12-17 23:25:25 [plugins/__init__.py:35] No plugins for group vllm.platform_plugins found. [0;36m(APIServer pid=70686)[0;0m [36m(pid=99758)[...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: d=99758)[0m DEBUG 12-17 23:25:25 [platforms/__init__.py:61] Checking if CUDA platform is available. [0;36m(APIServer pid=70686)[0;0m [36m(RayWorkerWrapper pid=82710)[0m DEBUG 12-17 23:22:38 [v1/worker/gpu_worker.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pid=70686)[0;0m [36m(pid=99758)[0m DEBUG 12-17 23:25:27 [triton_utils/importing.py:38] Triton found 0 active drivers in distributed environment. This is expected during initialization. [0;36m(APIServer pid=70686)[0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Scale Elastic EP is Pending on EngineCore bug;stale ### Your current environment ### 🐛 Describe the bug # Commands Run Run ``` vllm serve --model /mnt/Qwen3-30B-A3B/ --data-parallel-size 2 --data-parallel-backend...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: worker/gpu_worker.py:358] Memory profiling takes 7.29 seconds. Total non KV cache memory: 36.07GiB; torch peak memory increase: 5.58GiB; non-torch forward increase memory: 0.61GiB; weights memory: 29.88GiB. [0;36m(APIS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: onment ### 🐛 Describe the bug # Commands Run Run ``` vllm serve --model /mnt/Qwen3-30B-A3B/ --data-parallel-size 2 --data-parallel-backend ray --distributed-executor-backend ray --enforce-eager --disable-log-stats ``` a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
