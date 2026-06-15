# vllm-project/vllm#830: How to use API

| 字段 | 值 |
| --- | --- |
| Issue | [#830](https://github.com/vllm-project/vllm/issues/830) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to use API

### Issue 正文摘录

I have started a vLLM API server using the following command: `python -m vllm.entrypoints.api_server --model meta-llama/Llama-2-13b-chat-hf --port 5500` This produces the output and starts the api server: ``` INFO 08-22 15:27:08 llm_engine.py:70] Initializing an LLM engine with config: model='meta-llama/Llama-2-13b-chat-hf', tokenizer='meta-llama/Llama-2-13b-chat-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-22 15:27:08 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. INFO 08-22 15:27:25 llm_engine.py:196] # GPU blocks: 865, # CPU blocks: 327 INFO: Started server process [9264] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://localhost:5500 (Press CTRL+C to quit) ``` Now I am trying to generate some output using the API. I am using Python requests library to do so: ``` import requests myobj = { "prompt": "San Francisco i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: r using the following command: `python -m vllm.entrypoints.api_server --model meta-llama/Llama-2-13b-chat-hf --port 5500` This produces the output and starts the api server: ``` INFO 08-22 15:27:08 llm_engine.py:70] Ini...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: output using the API. I am using Python requests library to do so: ``` import requests myobj = { "prompt": "San Francisco is a" } requests.get('http://localhost:5500/generate', json = myobj) ``` This generates the follo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lama/Llama-2-13b-chat-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-22 15:27:08 tokeniz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: eta-llama/Llama-2-13b-chat-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-22 15:27:08 to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 5, # CPU blocks: 327 INFO: Started server process [9264] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://localhost:5500 (Press CTRL+C to quit) ``` Now I am tryi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
