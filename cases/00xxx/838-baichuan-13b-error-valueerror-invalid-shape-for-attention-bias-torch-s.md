# vllm-project/vllm#838: 麻烦关注下baichuan-13b error:ValueError: Invalid shape for attention bias: torch.Size([40, 10, 10]) (expected (1, 40, 10, 10))

| 字段 | 值 |
| --- | --- |
| Issue | [#838](https://github.com/vllm-project/vllm/issues/838) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 麻烦关注下baichuan-13b error:ValueError: Invalid shape for attention bias: torch.Size([40, 10, 10]) (expected (1, 40, 10, 10))

### Issue 正文摘录

以下时报错内容，在容器里运行时的报错： Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/data1/zhangxing/pyprojects/vllm-main/vllm/entrypoints/openai/api_server.py", line 624, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/async_llm_engine.py", line 232, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/async_llm_engine.py", line 55, in __init__ self.engine = engine_class(*args, **kwargs) File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/llm_engine.py", line 104, in __init__ self._init_cache() File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/llm_engine.py", line 182, in _init_cache num_blocks = self._run_workers( File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/llm_engine.py", line 470, in _run_workers output = executor(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs)...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s/vllm-main/vllm/engine/llm_engine.py", line 182, in _init_cache num_blocks = self._run_workers( File "/data1/zhangxing/pyprojects/vllm-main/vllm/engine/llm_engine.py", line 470, in _run_workers output = executor(*args,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion.py", line 399, in multi_query_kv_attention out = xops.memory_efficient_attention_forward( File "/usr/local/lib/python3.8/dist-packages/xformers/ops/fmha/__init__.py", line 214, in memory_efficient_attention_forward...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm/worker/worker.py", line 108, in profile_num_available_blocks self.model( File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ata1/zhangxing/pyprojects/vllm-main/vllm/worker/worker.py", line 108, in profile_num_available_blocks self.model( File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1501, in _call_impl return...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
