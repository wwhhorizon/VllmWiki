# vllm-project/vllm#1114: AWQ: bfloat16 not supported? And `--dtype` arg doesn't allow specifying float16 

| 字段 | 值 |
| --- | --- |
| Issue | [#1114](https://github.com/vllm-project/vllm/issues/1114) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ: bfloat16 not supported? And `--dtype` arg doesn't allow specifying float16 

### Issue 正文摘录

Hi guys I had a report earlier today from a user telling me that he tried one of my new AWQ models, and got an error indicating that only float16 is supported with AWQ. I tested it myself with the server and found the same, eg trying to run: https://huggingface.co/TheBloke/Spicyboros-13B-2.2-AWQ gives this output: ``` INFO 09-20 19:09:33 llm_engine.py:72] Initializing an LLM engine with config: model='TheBloke/Spicyboros-13B-2.2-AWQ', tokenizer='TheBloke/Spicyboros-13B-2.2-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/vllm/vllm/vllm/entrypoints/api_server.py", line 83, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/vllm/vllm/vllm/engine/async_llm_engine.py", line 486, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/home/vllm/vllm/vllm/engine/async_llm_engine.py", line 270,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: AWQ: bfloat16 not supported? And `--dtype` arg doesn't allow specifying float16 Hi guys I had a report earlier today from a user telling me that he tried one of my new AWQ models, and got an error indicating that only f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ort earlier today from a user telling me that he tried one of my new AWQ models, and got an error indicating that only float16 is supported with AWQ. I tested it myself with the server and found the same, eg trying to r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: AWQ: bfloat16 not supported? And `--dtype` arg doesn't allow specifying float16 Hi guys I had a report earlier today from a user telling me that he tried one of my new AWQ models, and got an error indicating that only f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: os-13B-2.2-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Traceback (most recent call last...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: and got an error indicating that only float16 is supported with AWQ. I tested it myself with the server and found the same, eg trying to run: https://huggingface.co/TheBloke/Spicyboros-13B-2.2-AWQ gives this output: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
