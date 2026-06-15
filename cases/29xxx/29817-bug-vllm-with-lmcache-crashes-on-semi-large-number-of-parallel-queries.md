# vllm-project/vllm#29817: [Bug]: vllm with lmcache crashes on semi-large number of parallel queries

| 字段 | 值 |
| --- | --- |
| Issue | [#29817](https://github.com/vllm-project/vllm/issues/29817) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm with lmcache crashes on semi-large number of parallel queries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Before anyone reads this. I believe this has something to do with lmcache. Should i go to lmcache's issues for this or is lmcache fully supported in vllm and this belongs here? VLLM version 0.11.2 installed with `uv pip install vllm==0.11.2 --torch-backend=auto` So i was stress testing my installation of vllm with the model specified which was served on 4x4090 using this command: ``` LMCACHE_CONFIG_FILE=lmcache_config.yaml vllm serve cpatonn/GLM-4.5-Air-AWQ-4bit \ --pipeline-parallel-size 2 \ --tensor-parallel-size 2 \ --tokenizer-mode auto \ --max-model-len 128000 \ --enable-log-requests \ --kv-cache-dtype auto \ --enable-expert-parallel \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --port 8002 \ --dtype float16 \ --max-num-seqs 32 \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' \ --kv-offloading-backend lmcache \ --kv-offloading-size 32 \ --swap-space 16 ``` the lmcache_config.yaml (found somewhere online too) ``` chunk_size: 256 local_cpu: true max_local_cpu_size: 32 enable_async_loading: true ``` I was running my personal suite to test p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: this or is lmcache fully supported in vllm and this belongs here? VLLM version 0.11.2 installed with `uv pip install vllm==0.11.2 --torch-backend=auto` So i was stress testing my installation of vllm with the model spec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : vllm with lmcache crashes on semi-large number of parallel queries bug;stale ### Your current environment ### 🐛 Describe the bug Before anyone reads this. I believe this has something to do with lmcache. Should i go t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --max-model-len 128000 \ --enable-log-requests \ --kv-cache-dtype auto \ --enable-expert-parallel \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --port 8002 \ --dtyp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sync_loading: true ``` I was running my personal suite to test parallelism up to 32 concurrent requests. input tokens 1024, 2048 and 4096, output stopped at 1024 tokens with concurrency from 1 to 32 using powers of 2. A...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 2:07,636] LMCache ERROR: The number of tokens is more than the number of blocks.Something might be wrong in scheduling logic! (vllm_v1_adapter.py:381:lmcache.integration.vllm.vllm_v1_adapter) ``` Which ultimately result...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
