# vllm-project/vllm#2024: Load Qlora-Mixtral-finetuned model: KeyError: 'model.layers.1.block_sparse_moe.experts.4.w3.weight

| 字段 | 值 |
| --- | --- |
| Issue | [#2024](https://github.com/vllm-project/vllm/issues/2024) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load Qlora-Mixtral-finetuned model: KeyError: 'model.layers.1.block_sparse_moe.experts.4.w3.weight

### Issue 正文摘录

File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 729, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/workspace/vllm/vllm/engine/async_llm_engine.py", line 495, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/workspace/vllm/vllm/engine/async_llm_engine.py", line 269, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/workspace/vllm/vllm/engine/async_llm_engine.py", line 314, in _init_engine return engine_class(*args, **kwargs) File "/workspace/vllm/vllm/engine/llm_engine.py", line 107, in __init__ self._init_workers_ray(placement_group) File "/workspace/vllm/vllm/engine/llm_engine.py", line 194, in _init_workers_ray self._run_workers( File "/workspace/vllm/vllm/engine/llm_engine.py", line 750, in _run_workers self._run_workers_in_batch(workers, method, *args, **kwargs)) File "/workspace/vllm/vllm/engine/llm_engine.py", line 727, in _run_workers_in_batch all_outputs = ray.get(all_outputs) File "/usr/local/lib/python3.10/dist-packages/ray/_private/auto_init_hook.py", line 24, in auto_init_wrapper return fn(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/ray/_private/client_mode_hook.py", line 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Load Qlora-Mixtral-finetuned model: KeyError: 'model.layers.1.block_sparse_moe.experts.4.w3.weight File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 729, in engine = AsyncLLMEngine.from_engine_args(engi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ad Qlora-Mixtral-finetuned model: KeyError: 'model.layers.1.block_sparse_moe.experts.4.w3.weight File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 729, in engine = AsyncLLMEngine.from_engine_args(engine...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Load Qlora-Mixtral-finetuned model: KeyError: 'model.layers.1.block_sparse_moe.experts.4.w3.weight File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 729, in engine = AsyncLLMEngine.from_engine_args(engi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
