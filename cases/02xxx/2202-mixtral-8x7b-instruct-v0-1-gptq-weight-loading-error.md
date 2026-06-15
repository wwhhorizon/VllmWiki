# vllm-project/vllm#2202: Mixtral-8x7B-Instruct-v0.1-GPTQ weight loading error

| 字段 | 值 |
| --- | --- |
| Issue | [#2202](https://github.com/vllm-project/vllm/issues/2202) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization |
| 症状 | crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral-8x7B-Instruct-v0.1-GPTQ weight loading error

### Issue 正文摘录

Command: ```bash python3 -m vllm.entrypoints.openai.api_server --model /models/Mixtral-8x7B-Instruct-v0.1-GPTQ -tp 2 --dtype float16 ``` Result: ```bash INFO 12-19 00:45:14 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, model='/models/Mixtral-8x7B-Instruct-v0.1-GPTQ', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='float16', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=False, max_context_len_to_capture=8192, engine_use_ray=False, disable_log_requests=False, max_log_len=None) WARNING 12-19 00:45:14 config.py:463] Casting torch.bfloat16 to torch.float16. WARNING 12-19 00:45:14 config.py:175] gptq quantization...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: i.api_server --model /models/Mixtral-8x7B-Instruct-v0.1-GPTQ -tp 2 --dtype float16 ``` Result: ```bash INFO 12-19 00:45:14 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug Command: ```bash python3 -m vllm.entrypoints.openai.api_server --model /models/Mixtral-8x7B-Instruct-v0.1-GPTQ -tp 2 --dtype float16 ``` Result: ```bash INFO 12-19 00:45:14 api_server.py:727] args: Namespace(host=Non...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: loaded by Mistral. Maybe we just need a lookup table? Or do the instruct versions have different params? correctness distributed_parallel;frontend_api;model_support;quantization cuda;moe;operator;quantization crash;mism...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: WARNING 12-19 00:45:14 config.py:187] gptq does not support CUDA graph yet. Disabling CUDA graph. 2023-12-19 00:45:16,379 INFO worker.py:1673 -- Started a local Ray instance. INFO 12-19 00:45:17 llm_engine.py:73] Initia...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
