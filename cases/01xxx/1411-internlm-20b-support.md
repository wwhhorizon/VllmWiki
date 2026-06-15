# vllm-project/vllm#1411: InternLM 20B Support

| 字段 | 值 |
| --- | --- |
| Issue | [#1411](https://github.com/vllm-project/vllm/issues/1411) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> InternLM 20B Support

### Issue 正文摘录

Traceback (most recent call last): File "/root/miniconda3/envs/vllm/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/root/miniconda3/envs/vllm/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/home/ubuntu/vllm/vllm/entrypoints/openai/api_server.py", line 613, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 487, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 270, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 306, in _init_engine return engine_class(*args, **kwargs) File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 113, in __init__ self._init_cache() File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 193, in _init_cache num_blocks = self._run_workers( File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 704, in _run_workers all_outputs = ray.get(all_outputs) File "/root/miniconda3/envs/vllm/lib/python3.8/site-packages/ray/_private/auto_init_hook.py", line 24...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ubuntu/vllm/vllm/engine/llm_engine.py", line 193, in _init_cache num_blocks = self._run_workers( File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 704, in _run_workers all_outputs = ray.get(all_outputs) File "/ro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm/worker/worker.py", line 111, in profile_num_available_blocks self.model( File "/root/miniconda3/envs/vllm/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, *...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: **kwargs) File "/home/ubuntu/vllm/vllm/worker/worker.py", line 111, in profile_num_available_blocks self.model( File "/root/miniconda3/envs/vllm/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1501, in _ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
