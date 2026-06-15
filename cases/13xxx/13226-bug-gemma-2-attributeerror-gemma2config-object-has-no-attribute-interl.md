# vllm-project/vllm#13226: [Bug]: Gemma 2 - AttributeError: 'Gemma2Config' object has no attribute 'interleaved_sliding_window'

| 字段 | 值 |
| --- | --- |
| Issue | [#13226](https://github.com/vllm-project/vllm/issues/13226) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma 2 - AttributeError: 'Gemma2Config' object has no attribute 'interleaved_sliding_window'

### Issue 正文摘录

### Your current environment Official docker image version: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug When setting Gemma2 models, vLLM search for `interleaved_sliding_window` attribute in the HF config. The full trace: INFO 02-13 06:16:19 model_runner.py:1111] Starting to load model google/gemma-2-2b-it... ERROR 02-13 06:16:19 engine.py:387] 'Gemma2Config' object has no attribute 'interleaved_sliding_window' ERROR 02-13 06:16:19 engine.py:387] Traceback (most recent call last): ERROR 02-13 06:16:19 engine.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine ERROR 02-13 06:16:19 engine.py:387] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 02-13 06:16:19 engine.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-13 06:16:19 engine.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args ERROR 02-13 06:16:19 engine.py:387] return cls(ipc_path=ipc_path, ERROR 02-13 06:16:19 engine.py:387] ^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-13 06:16:19 engine.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/mu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 'Gemma2Config' object has no attribute 'interleaved_sliding_window' bug;stale ### Your current environment Official docker image version: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug When setting Gemma2 models, vLLM s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma 2 - AttributeError: 'Gemma2Config' object has no attribute 'interleaved_sliding_window' bug;stale ### Your current environment Official docker image version: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug W...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 'interleaved_sliding_window' bug;stale ### Your current environment Official docker image version: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug When setting Gemma2 models, vLLM search for `interleaved_sliding_window`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
