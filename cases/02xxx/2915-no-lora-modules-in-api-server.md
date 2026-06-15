# vllm-project/vllm#2915: No --lora-modules in api server

| 字段 | 值 |
| --- | --- |
| Issue | [#2915](https://github.com/vllm-project/vllm/issues/2915) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No --lora-modules in api server

### Issue 正文摘录

Hi, it seems that the API server misses the `--lora-modules` when I run `python -m vllm.entrypoints.api_server -h` (my version is `0.3.1`). Can you check again? Here is the full log ``` usage: api_server.py [-h] [--host HOST] [--port PORT] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE] [--root-path ROOT_PATH] [--model MODEL] [--tokenizer TOKENIZER] [--revision REVISION] [--tokenizer-revision TOKENIZER_REVISION] [--tokenizer-mode {auto,slow}] [--trust-remote-code] [--download-dir DOWNLOAD_DIR] [--load-format {auto,pt,safetensors,npcache,dummy}] [--dtype {auto,half,float16,bfloat16,float,float32}] [--kv-cache-dtype {auto,fp8_e5m2}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipeline-parallel-size PIPELINE_PARALLEL_SIZE] [--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--max-parallel-loading-workers MAX_PARALLEL_LOADING_WORKERS] [--block-size {8,16,32}] [--seed SEED] [--swap-space SWAP_SPACE] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [--max-num-seqs MAX_NUM_SEQS] [--max-paddings MAX_PADDINGS] [--disable-log-stats] [--quantization {awq,gptq,squeezellm,None}] [--enforce-eager] [--max-context-len-to-capture MA...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: load-format {auto,pt,safetensors,npcache,dummy}] [--dtype {auto,half,float16,bfloat16,float,float32}] [--kv-cache-dtype {auto,fp8_e5m2}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipeline-parallel-size PIPEL...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [--dtype {auto,half,float16,bfloat16,float,float32}] [--kv-cache-dtype {auto,fp8_e5m2}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipeline-parallel-size PIPELINE_PARALLEL_SIZE] [--tensor-parallel-size TENSOR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: l-certfile SSL_CERTFILE] [--root-path ROOT_PATH] [--model MODEL] [--tokenizer TOKENIZER] [--revision REVISION] [--tokenizer-revision TOKENIZER_REVISION] [--tokenizer-mode {auto,slow}] [--trust-remote-code] [--download-d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -lora-modules` when I run `python -m vllm.entrypoints.api_server -h` (my version is `0.3.1`). Can you check again? Here is the full log ``` usage: api_server.py [-h] [--host HOST] [--port PORT] [--ssl-keyfile SSL_KEYFIL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: el-loading-workers MAX_PARALLEL_LOADING_WORKERS] [--block-size {8,16,32}] [--seed SEED] [--swap-space SWAP_SPACE] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [--ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
