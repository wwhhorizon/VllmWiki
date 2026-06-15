# vllm-project/vllm#3651: [Usage]: api_server.py: error: unrecognized arguments: --api-key 

| 字段 | 值 |
| --- | --- |
| Issue | [#3651](https://github.com/vllm-project/vllm/issues/3651) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: api_server.py: error: unrecognized arguments: --api-key 

### Issue 正文摘录

### Your current environment vllm==0.3.3 Problem: I run : `root@autodl-container-aa4d48ac02-16fdcb75:~# python -m vllm.entrypoints.api_server --model /root/autodl-tmp/Qwen15_14B_Chat_sft --tensor-parallel-size 2 --max-model-len 12800 --port 8080 --api-key token-temp` and get: ``` usage: api_server.py [-h] [--host HOST] [--port PORT] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE] [--root-path ROOT_PATH] [--model MODEL] [--tokenizer TOKENIZER] [--revision REVISION] [--code-revision CODE_REVISION] [--tokenizer-revision TOKENIZER_REVISION] [--tokenizer-mode {auto,slow}] [--trust-remote-code] [--download-dir DOWNLOAD_DIR] [--load-format {auto,pt,safetensors,npcache,dummy}] [--dtype {auto,half,float16,bfloat16,float,float32}] [--kv-cache-dtype {auto,fp8_e5m2}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipeline-parallel-size PIPELINE_PARALLEL_SIZE] [--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--max-parallel-loading-workers MAX_PARALLEL_LOADING_WORKERS] [--block-size {8,16,32,128}] [--seed SEED] [--swap-space SWAP_SPACE] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [--max-num-seqs MAX_NUM_SEQS] [--max-paddings...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: dir DOWNLOAD_DIR] [--load-format {auto,pt,safetensors,npcache,dummy}] [--dtype {auto,half,float16,bfloat16,float,float32}] [--kv-cache-dtype {auto,fp8_e5m2}] [--max-model-len MAX_MODEL_LEN] [--worker-use-ray] [--pipelin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: container-aa4d48ac02-16fdcb75:~# python -m vllm.entrypoints.api_server --model /root/autodl-tmp/Qwen15_14B_Chat_sft --tensor-parallel-size 2 --max-model-len 12800 --port 8080 --api-key token-temp` and get: ``` usage: ap...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: el-loading-workers MAX_PARALLEL_LOADING_WORKERS] [--block-size {8,16,32,128}] [--seed SEED] [--swap-space SWAP_SPACE] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: U_LORAS] [--device {auto,cuda,neuron}] [--engine-use-ray] [--disable-log-requests] [--max-log-len MAX_LOG_LEN] api_server.py: error: unrecognized arguments: --api-key token-temp ``` performance attention_kv_cache;distri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pport;quantization;scheduler_memory cuda;quantization slowdown dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
