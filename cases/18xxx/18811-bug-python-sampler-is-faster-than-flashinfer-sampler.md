# vllm-project/vllm#18811: [Bug]: python sampler is faster than flashinfer sampler

| 字段 | 值 |
| --- | --- |
| Issue | [#18811](https://github.com/vllm-project/vllm/issues/18811) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: python sampler is faster than flashinfer sampler

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, vllm run from docker image. Version 0.9.0 is much better but still slower. In 0.8.5 python infer was about 2 token/sec faster than flash infer. In 0.9.0 difference is on the level 0,5 token/sec Python sampler docker run --runtime nvidia --gpus all -d --name vllm-Qwen3-32B-v10 --restart unless-stopped -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -e VLLM_FLASH_ATTN_VERSION=2 -e VLLM_USE_V1=1 -e VLLM_USE_FLASHINFER_SAMPLER=0 -e VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE=1 -e VLLM_ATTENTION_BACKEND=FLASH_ATTN -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True -e VLLM_ENABLE_V1_MULTIPROCESSING=1 -e MAX_JOBS=32 -e VLLM_USE_PRECOMPILED=true -e RAY_ROTATION_MAX_BYTES=0 -e RAY_ROTATION_BACKUP_COUNT=0 -p 8000:8000 vllm/vllm-openai:v0.9.0 --model Qwen/Qwen3-32B-FP8 --served-model-name BSSTelcoChat experimental reasoning llm --max-model-len 26060 --max-seq-len-to-capture 26060 --max-num-batched-tokens 26060 --block-size 32 --gpu-memory-utilization 0.999999 --seed 0 --max-log-len 35 --enable-auto-tool-choice --tool-call-parser hermes --tokenizer-pool-size 64 --max-parallel-loading-workers 64 --long-prefill-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment ### 🐛 Describe the bug Hi, vllm run from docker image. Version 0.9.0 is much better but still slower. In 0.8.5 python infer was about 2 token/sec faster than flash infer. In 0.9.0 difference is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: python sampler is faster than flashinfer sampler bug;stale ### Your current environment ### 🐛 Describe the bug Hi, vllm run from docker image. Version 0.9.0 is much better but still slower. In 0.8.5 python infer...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CKUP_COUNT=0 -p 8000:8000 vllm/vllm-openai:v0.9.0 --model Qwen/Qwen3-32B-FP8 --served-model-name BSSTelcoChat experimental reasoning llm --max-model-len 26060 --max-seq-len-to-capture 26060 --max-num-batched-tokens 2606...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: c Python sampler docker run --runtime nvidia --gpus all -d --name vllm-Qwen3-32B-v10 --restart unless-stopped -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -e VLLM_FLASH_ATTN_VERSIO...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: python sampler is faster than flashinfer sampler bug;stale ### Your current environment ### 🐛 Describe the bug Hi, vllm run from docker image. Version 0.9.0 is much better but still slower. In 0.8.5 python infer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
