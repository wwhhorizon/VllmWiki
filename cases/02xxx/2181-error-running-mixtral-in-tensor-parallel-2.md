# vllm-project/vllm#2181: Error running Mixtral in tensor-parallel 2

| 字段 | 值 |
| --- | --- |
| Issue | [#2181](https://github.com/vllm-project/vllm/issues/2181) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error running Mixtral in tensor-parallel 2

### Issue 正文摘录

AWQ mixtral-instruct downloaded from here: https://huggingface.co/ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ```bash docker run --gpus all \ -p 8000:8000 \ --shm-size=12gb \ vllm/vllm-openai \ --model /models/Mixtral-8x7B-Instruct-v0.1-AWQ \ -tp 2 ``` Result: ```bash INFO 12-18 19:16:27 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, model='/models/Mixtral-8x7B-Instruct-v0.1-AWQ', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=False, max_context_len_to_capture=8192, engine_use_ray=False, disable_log_requests=False, max_log_len=None) WARNING 12-18 19:1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in tensor-parallel 2 AWQ mixtral-instruct downloaded from here: https://huggingface.co/ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ```bash docker run --gpus all \ -p 8000:8000 \ --shm-size=12gb \ vllm/vllm-openai \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gingface.co/ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ Command: ```bash docker run --gpus all \ -p 8000:8000 \ --shm-size=12gb \ vllm/vllm-openai \ --model /models/Mixtral-8x7B-Instruct-v0.1-AWQ \ -tp 2 ``` Result: ```bash...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lse, max_context_len_to_capture=8192, engine_use_ray=False, disable_log_requests=False, max_log_len=None) WARNING 12-18 19:16:27 config.py:175] awq quantization is not fully optimized yet. The speed can be slower than n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
