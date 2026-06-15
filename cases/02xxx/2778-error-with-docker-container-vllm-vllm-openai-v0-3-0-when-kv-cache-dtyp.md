# vllm-project/vllm#2778: Error with docker container `vllm/vllm-openai:v0.3.0` when `--kv-cache-dtype=fp8_e5m2`

| 字段 | 值 |
| --- | --- |
| Issue | [#2778](https://github.com/vllm-project/vllm/issues/2778) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error with docker container `vllm/vllm-openai:v0.3.0` when `--kv-cache-dtype=fp8_e5m2`

### Issue 正文摘录

When I run the following command, it works as expected: ``` docker run --rm --gpus "device=8" vllm/vllm-openai:v0.3.0 --model=facebook/opt-125m ``` However, when I add `--kv-cache-dtype=fp8_e5m2`, it results in an error: ``` docker run --rm --gpus "device=8" vllm/vllm-openai:v0.3.0 --model=facebook/opt-125m --kv-cache-dtype=fp8_e5m2 ``` Error log: ```txt INFO 02-06 01:02:56 api_server.py:209] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='facebook/opt-125m', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='fp8_e5m2', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforc...

## 现有链接修复摘要

#2781 Fix nvcc not found in vllm-openai image

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Error with docker container `vllm/vllm-openai:v0.3.0` when `--kv-cache-dtype=fp8_e5m2` When I run the following command, it works as expected: ``` docker run --rm --gpus "device=8" vllm/vllm-openai:v0.3.0 --model=facebo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Error with docker container `vllm/vllm-openai:v0.3.0` when `--kv-cache-dtype=fp8_e5m2` When I run the following command, it works as expected: ``` docker run --rm --gpus "device=8" vllm/vllm-openai:v0.3.0 --model=facebo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pected: ``` docker run --rm --gpus "device=8" vllm/vllm-openai:v0.3.0 --model=facebook/opt-125m ``` However, when I add `--kv-cache-dtype=fp8_e5m2`, it results in an error: ``` docker run --rm --gpus "device=8" vllm/vll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:209] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e "/workspace/vllm/config.py", line 312, in _verify_cache_dtype nvcc_cuda_version = get_nvcc_cuda_version() File "/workspace/vllm/utils.py", line 191, in get_nvcc_cuda_version nvcc_output = subprocess.check_output([cuda...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2781](https://github.com/vllm-project/vllm/pull/2781) | closes_keyword | 0.95 | Fix nvcc not found in vllm-openai image | Fix #2778 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
