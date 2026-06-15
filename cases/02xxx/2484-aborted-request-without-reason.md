# vllm-project/vllm#2484: Aborted request without reason

| 字段 | 值 |
| --- | --- |
| Issue | [#2484](https://github.com/vllm-project/vllm/issues/2484) |
| 状态 | closed |
| 标签 |  |
| 评论 | 50; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Aborted request without reason

### Issue 正文摘录

Hi, i am trying to load test vllm on a single gpu with 20 concurrent request. Each request would pass through the llm engine twice. Once to change the prompt, the other to generate the output. However, normally only between 6 - 10 requests finished successfully. The remaining requests would normally just be displayed as "Aborted request" without any error logs or trace. GPU KV cache can be up to 95% for those sequences which finished successfully. ``` INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request 0e89f1d2d94c4a039f868222c100cc8a. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request be67046b843244b5bf1ed3d2ff2f5a02. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request b532ed57647945869a4cae499fe54f23. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request 6c56897bbc9d4a808b8e056c39baf91b. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request 75b645c69d7449509f68ca23b34f1048. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request eb87d6473a9d4b3699ca0cc236900248. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request ca15a251849c45329825ca95a2fce96b. INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request c42bbea2f781469e8...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ust_remote_code=True, download_dir=None, load_format="auto", dtype="auto", seed=0, max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_siz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: dtype="auto", seed=0, max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, swap_space=4, gpu_memory_utilization=0.9, max_num_batch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to load the engine is as follows: ``` engine_args = AsyncEngineArgs( model=LLM_BASEMODEL, tokenizer=LLM_BASEMODEL, tokenizer_mode="auto", trust_remote_code=True, download_dir=None, load_format="auto", dtype="auto", seed...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ways to find out what's the cause of the abortion without success. Appreciate any help. Thanks! My code to load the engine is as follows: ``` engine_args = AsyncEngineArgs( model=LLM_BASEMODEL, tokenizer=LLM_BASEMODEL,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t be displayed as "Aborted request" without any error logs or trace. GPU KV cache can be up to 95% for those sequences which finished successfully. ``` INFO 01-17 03:11:25 async_llm_engine.py:134] Aborted request 0e89f1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
