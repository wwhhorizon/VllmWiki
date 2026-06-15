# vllm-project/vllm#2640: Error in newest dev ver: Worker.__init__() got an unexpected keyword argument 'cache_config'

| 字段 | 值 |
| --- | --- |
| Issue | [#2640](https://github.com/vllm-project/vllm/issues/2640) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Error in newest dev ver: Worker.__init__() got an unexpected keyword argument 'cache_config'

### Issue 正文摘录

I build the newest master branch with #2279 commit. And I run the following command `python -m vllm.entrypoints.openai.api_server --model ./Mistral-7B-Instruct-v0.2-AWQ --quantization awq --dtype auto --host 0.0.0.0 --port 8081 --tensor-parallel-size 2` I meet the error: ``` INFO 01-29 09:41:47 api_server.py:209] args: Namespace(host='0.0.0.0', port=8081, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='./Mistral-7B-Instruct-v0.2-AWQ', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization='awq', enforce_eager=False, max_context_len_to_capture=8192, disable_custom_all...

## 现有链接修复摘要

#2279 Support FP8-E5M2 KV Cache

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: orker.__init__() got an unexpected keyword argument 'cache_config' bug I build the newest master branch with #2279 commit. And I run the following command `python -m vllm.entrypoints.openai.api_server --model ./Mistral-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: m.entrypoints.openai.api_server --model ./Mistral-7B-Instruct-v0.2-AWQ --quantization awq --dtype auto --host 0.0.0.0 --port 8081 --tensor-parallel-size 2` I meet the error: ``` INFO 01-29 09:41:47 api_server.py:209] ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: est dev ver: Worker.__init__() got an unexpected keyword argument 'cache_config' bug I build the newest master branch with #2279 commit. And I run the following command `python -m vllm.entrypoints.openai.api_server --mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d keyword argument 'cache_config' ``` I am running with `python=3.11`, `CUDA 12.1`, `driver 530` with 2x RTX 3090 NVLink. I notice there is a discussion (https://github.com/vllm-project/vllm/pull/2279#discussion_r146877...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:209] args: Namespace(host='0.0.0.0', port=8081, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2279](https://github.com/vllm-project/vllm/pull/2279) | mentioned | 0.45 | Support FP8-E5M2 KV Cache | keyword argument 'cache_config' i build the newest master branch with #2279 commit. and i run the following command `python -m vllm.entrypoints.openai.api_server --model ./mistral… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
