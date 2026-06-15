# vllm-project/vllm#701: set max-num-batched-tokens cause RuntimeError

| 字段 | 值 |
| --- | --- |
| Issue | [#701](https://github.com/vllm-project/vllm/issues/701) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> set max-num-batched-tokens cause RuntimeError

### Issue 正文摘录

Hi, I try set --max-num-batched-tokens with 1 for the baichuan13B model, but get following error during loading. For those application with latency concern, how could we provide such QoS? ``` File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/data/aigc/workset/vllm/vllm/worker/worker.py", line 108, in profile_num_available_blocks self.model( File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/data/aigc/workset/vllm/vllm/model_executor/models/baichuan.py", line 292, in forward hidden_states = self.model(input_ids, positions, kv_caches, File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/data/aigc/workset/vllm/vllm/model_executor/models/baichuan.py", line 260, in forward hidden_states = layer( File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/data/aigc/workset/vllm/vllm/model_executor/models/baichuan.py", line 210, in for...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: /workset/vllm/vllm/worker/worker.py", line 108, in profile_num_available_blocks self.model( File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: odel, but get following error during loading. For those application with latency concern, how could we provide such QoS? ``` File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decora...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: False) File "/usr/local/lib/python3.10/dist-packages/xformers/ops/fmha/cutlass.py", line 175, in apply out, lse, rng_seed, rng_offset = cls.OPERATOR( File "/usr/local/lib/python3.10/dist-packages/torch/_ops.py", line 50...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion.py", line 399, in multi_query_kv_attention out = xops.memory_efficient_attention_forward( File "/usr/local/lib/python3.10/dist-packages/xformers/ops/fmha/__init__.py", line 213, in memory_efficient_attention_forward...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Error Hi, I try set --max-num-batched-tokens with 1 for the baichuan13B model, but get following error during loading. For those application with latency concern, how could we provide such QoS? ``` File "/usr/local/lib/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
