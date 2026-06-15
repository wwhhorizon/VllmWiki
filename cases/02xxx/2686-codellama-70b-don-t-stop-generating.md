# vllm-project/vllm#2686: codellama 70b don't stop generating

| 字段 | 值 |
| --- | --- |
| Issue | [#2686](https://github.com/vllm-project/vllm/issues/2686) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> codellama 70b don't stop generating

### Issue 正文摘录

Hello I tried running codellama 70b using docker.io/vllm/vllm-openai:v0.2.7 docker image. ``` INFO 01-31 12:11:56 api_server.py:727] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_ce rtfile=None, model='codellama/CodeLlama-70b-Instruct-hf', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_paral lel_size=1, tensor_parallel_size=8, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=True, max_co ntext_len_to_capture=8192, engine_use_ray=False, disable_log_requests=False, max_log_len=None) 2024-01-31 12:11:58,035 INFO worker.py:1724 -- Started a local Ray instance. INFO 01-31 12:11:58 llm_engine.py:70] Initializing an LLM engine with config: model='codellama/CodeLlama-70b-Instruct...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: codellama 70b don't stop generating Hello I tried running codellama 70b using docker.io/vllm/vllm-openai:v0.2.7 docker image. ``` INFO 01-31 12:11:56 api_server.py:727] args: Namespace(host='0.0.0.0', port=8000, allow_c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ama 70b don't stop generating Hello I tried running codellama 70b using docker.io/vllm/vllm-openai:v0.2.7 docker image. ``` INFO 01-31 12:11:56 api_server.py:727] args: Namespace(host='0.0.0.0', port=8000, allow_credent...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_paral lel_size=1, tensor_parallel_size=8, max_parallel_loading_workers=None, bloc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:727] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rue, max_co ntext_len_to_capture=8192, engine_use_ray=False, disable_log_requests=False, max_log_len=None) 2024-01-31 12:11:58,035 INFO worker.py:1724 -- Started a local Ray instance. INFO 01-31 12:11:58 llm_engine.py:7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
