# vllm-project/vllm#2565: vLLM computes max sequence length for Yi 200k at 4k

| 字段 | 值 |
| --- | --- |
| Issue | [#2565](https://github.com/vllm-project/vllm/issues/2565) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM computes max sequence length for Yi 200k at 4k

### Issue 正文摘录

https://huggingface.co/01-ai/Yi-34B-Chat/blob/main/config.json vLLM not accounting for rope scaling. So can't use full context. ``` -m vllm.entrypoints.openai.api_server \ --port=5000 \ --host=0.0.0.0 \ --model=01-ai/Yi-34B-Chat \ --seed 1234 \ --tensor-parallel-size=4 \ --trust-remote-code \ --max-model-len=204800 \ --download-dir=/workspace/.cache/huggingface/hub ``` gives: ``` INFO 01-23 21:18:03 api_server.py:727] args: Namespace(host='0.0.0.0', port=5000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, model='01-ai/Yi-34B-Chat', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/workspace/.cache/huggingface/hub', load_format='auto', dtype='auto', max_model_len=204800, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, max_parallel_loading_workers=None, block_size=16, seed=1234, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eage...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: vLLM computes max sequence length for Yi 200k at 4k https://huggingface.co/01-ai/Yi-34B-Chat/blob/main/config.json vLLM not accounting for rope scaling. So can't use full context. ``` -m vllm.entrypoints.openai.api_serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e, download_dir='/workspace/.cache/huggingface/hub', load_format='auto', dtype='auto', max_model_len=204800, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, max_parallel_loading_workers=None, blo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 096 in model's config.json). This may lead to incorrect model outputs or CUDA errors. Make sure the value is correct and within the model context size. ``` and otherwise defaults to 4096. correctness distributed_paralle...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:727] args: Namespace(host='0.0.0.0', port=5000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: parallel;frontend_api;model_support;quantization cuda;quantization crash;mismatch dtype https://huggingface.co/01-ai/Yi-34B-Chat/blob/main/config.json

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
