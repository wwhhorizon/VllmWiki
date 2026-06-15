# vllm-project/vllm#29840: [Bug]: LMCacheConnectorV1Impl has no attribute 'layerwise_storers' on remote full cache hit with layerwise mode

| 字段 | 值 |
| --- | --- |
| Issue | [#29840](https://github.com/vllm-project/vllm/issues/29840) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LMCacheConnectorV1Impl has no attribute 'layerwise_storers' on remote full cache hit with layerwise mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: When running vLLM with LMCache KVConnector (disable local_cpu, and set remote_url = "lm://", ) in layermode, vllm crashes with an [AttributeError] when a request has a full cache hit where all tokens can be fetched from lmcache remote url. Steps to Reproduce 1. start lm cache storage backend: lmcache_server localhost 65432 2. vllm config file: ``` chunk_size: 256 use_layerwise: true local_cpu: false remote_url: "lm://localhost:65432" remote_serde: "cachegen" max_local_cpu_size: 32 ``` 3. start vllm ``` LMCACHE_CONFIG_FILE=lmcache_svd.yaml \ vllm serve Qwen/Qwen3-8B \ --port 8000 \ --gpu-memory-utilization 0.8 \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"} ``` 4. Send a prompt to vllm (first request) and wait for completion and kv cache to be stored in lm cache remote backend 5. Stop the current vllm server. 6. Restart the vllm server (need a brand new vllm instance so the KV cache will need to be fetched from lm cache remote backend 7. Observe the crash with below error message when wait_for_save is called ``` self._lmcache_engine.wait_for_save() (EngineCore_DP0 pid=760811) ERROR 11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: start lm cache storage backend: lmcache_server localhost 65432 2. vllm config file: ``` chunk_size: 256 use_layerwise: true local_cpu: false remote_url: "lm://localhost:65432" remote_serde: "cachegen" max_local_cpu_size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: from lmcache remote url. Steps to Reproduce 1. start lm cache storage backend: lmcache_server localhost 65432 2. vllm config file: ``` chunk_size: 256 use_layerwise: true local_cpu: false remote_url: "lm://localhost:654...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: CacheConnectorV1Impl has no attribute 'layerwise_storers' on remote full cache hit with layerwise mode bug ### Your current environment ### 🐛 Describe the bug Description: When running vLLM with LMCache KVConnector (dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
