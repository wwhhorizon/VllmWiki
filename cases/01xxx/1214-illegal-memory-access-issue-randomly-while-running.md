# vllm-project/vllm#1214: Illegal Memory Access issue randomly while running

| 字段 | 值 |
| --- | --- |
| Issue | [#1214](https://github.com/vllm-project/vllm/issues/1214) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Illegal Memory Access issue randomly while running

### Issue 正文摘录

Running in a docker container. After this, the subsequent api requests returned 'Internal server error' ```INFO 09-28 06:39:29 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 29.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 16.8%, CPU KV cache usage: 0.0% INFO 09-28 06:39:34 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 28.9 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 17.1%, CPU KV cache usage: 0.0% INFO 09-28 06:39:39 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 28.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 17.4%, CPU KV cache usage: 0.0% INFO 09-28 06:39:44 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 28.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 17.8%, CPU KV cache usage: 0.0% INFO 09-28 06:39:49 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 28.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 18.0%, CPU KV cache...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Illegal Memory Access issue randomly while running Running in a docker container. After this, the subsequent api requests returned 'Internal server error' ```INFO 09-28 06:39:29 llm_engine.py:613] Avg prompt throughput:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .tensor(last_token_indicies, device=hidden_states.device)) RuntimeError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in forward hidden_states = _prune_hidden_states(hidden_states, input_metadata) File "/data/vllm/vllm/model_executor/layers/sampler.py", line 104, in _prune_hidden_states 0, torch.tensor(last_token_indicies, device=hidde...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: *kwargs) File "/data/vllm/vllm/worker/worker.py", line 293, in execute_model output = self.model( File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
