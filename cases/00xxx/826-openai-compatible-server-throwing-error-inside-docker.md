# vllm-project/vllm#826: OpenAI-Compatible Server throwing error inside Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#826](https://github.com/vllm-project/vllm/issues/826) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OpenAI-Compatible Server throwing error inside Docker

### Issue 正文摘录

After using this command inside the docker container " python -m vllm.entrypoints.openai.api_server \ --model facebook/opt-125m " root@e4c01cdbf8f2:/workspace# python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m INFO 08-22 09:09:12 llm_engine.py:70] Initializing an LLM engine with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 589, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 232, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 55, in __init__ self.engine = engine_class(*args, **...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: OpenAI-Compatible Server throwing error inside Docker After using this command inside the docker container " python -m vllm.entrypoints.openai.api_server \ --model facebook/opt-125m " root@e4c01cdbf8f2:/workspace# pytho...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nizer='facebook/opt-125m', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent call...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tokenizer='facebook/opt-125m', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) Traceback (most recent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the docker container " python -m vllm.entrypoints.openai.api_server \ --model facebook/opt-125m " root@e4c01cdbf8f2:/workspace# python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m INFO 08-22 09:09:12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
