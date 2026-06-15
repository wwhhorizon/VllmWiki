# vllm-project/vllm#1953: Runtime Memory Error

| 字段 | 值 |
| --- | --- |
| Issue | [#1953](https://github.com/vllm-project/vllm/issues/1953) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Runtime Memory Error

### Issue 正文摘录

Hello Everyone, I am running VLLM with Singularity on the following configuration: ## System CPU: 16 Cores GPU: 4 x 2080TI - 11GB VRAM Memory: 32GB ## VLLM Model: CodeLlama 13B AWQ Dtype: Float16 Tensor Parallel Size: 4 GPU Memory Utilization: 1 Swap Space: 4 VLLM runs without any problems reaching 200 tokens/s in batch inference, however, the following starts to show up after running overnight. ``` (raylet) [2023-12-07 03:27:39,873 E 101250 101275] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2023-12-06_16-50-22_168114_101109 is over 95% full, available space: 0; capacity: 67108864. Object creation will fail if spilling is required. ``` I am not sure what exactly the 67108864 value means here. Once these show up, running any query will result in the following error. ``` INFO: :52432 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ror Hello Everyone, I am running VLLM with Singularity on the following configuration: ## System CPU: 16 Cores GPU: 4 x 2080TI - 11GB VRAM Memory: 32GB ## VLLM Model: CodeLlama 13B AWQ Dtype: Float16 Tensor Parallel Siz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: U: 4 x 2080TI - 11GB VRAM Memory: 32GB ## VLLM Model: CodeLlama 13B AWQ Dtype: Float16 Tensor Parallel Size: 4 GPU Memory Utilization: 1 Swap Space: 4 VLLM runs without any problems reaching 200 tokens/s in batch infere...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", lin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 3-12-06_16-50-22_168114_101109 is over 95% full, available space: 0; capacity: 67108864. Object creation will fail if spilling is required. ``` I am not sure what exactly the 67108864 value means here. Once these show u...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ## VLLM Model: CodeLlama 13B AWQ Dtype: Float16 Tensor Parallel Size: 4 GPU Memory Utilization: 1 Swap Space: 4 VLLM runs without any problems reaching 200 tokens/s in batch inference, however, the following starts to s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
