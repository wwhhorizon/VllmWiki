# vllm-project/vllm#1984: Assertion Error when loading NousResearch/Yarn-Llama-2-70b-32k

| 字段 | 值 |
| --- | --- |
| Issue | [#1984](https://github.com/vllm-project/vllm/issues/1984) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Assertion Error when loading NousResearch/Yarn-Llama-2-70b-32k

### Issue 正文摘录

Hello, I'm trying to load the following model: https://huggingface.co/NousResearch/Yarn-Llama-2-70b-32k Using the following command: `python -m vllm.entrypoints.openai.api_server --model NousResearch/Yarn-Llama-2-70b-32k --trust-remote-code` I get the following error: ``` INFO 12-08 08:57:50 api_server.py:711] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='NousResearch/Yarn-Llama-2-70b-32k', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) INFO 12-08 08:57:50 llm_engine.py:73] Initializing an LLM engine with config: model='NousResearch/Yarn-Llama-2-70b-3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Assertion Error when loading NousResearch/Yarn-Llama-2-70b-32k Hello, I'm trying to load the following model: https://huggingface.co/NousResearch/Yarn-Llama-2-70b-32k Using the following command: `python -m vllm.entrypo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: original_max_position: 4096, scaling_factor: 8.0` I'm using vllm 0.2.3 installed using pip. This is the config.json of the model: ``` { "_name_or_path": "meta-llama/Llama-2-70b-hf", "architectures": [ "LlamaForCausalLM"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:711] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: le_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) INFO 12-08 08:57:50 llm_engine.py:73] Initializing an LLM engine with config: model='NousResearch/Yarn-Llama-2-7...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
