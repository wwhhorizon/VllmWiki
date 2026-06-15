# vllm-project/vllm#16692: [Bug]: Problems with vllm serve DeepSeek-R1 with 2 nodes and TP = 16（include vllm v0.8.4 v0.7.3 v0.7.2 V0 V1 engine）

| 字段 | 值 |
| --- | --- |
| Issue | [#16692](https://github.com/vllm-project/vllm/issues/16692) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;quantization;sampling |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Problems with vllm serve DeepSeek-R1 with 2 nodes and TP = 16（include vllm v0.8.4 v0.7.3 v0.7.2 V0 V1 engine）

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start command: head node: ```bash ray start --head --port=6379 && \ vllm serve $MODELPATH \ --max-num-seqs=256 \ --max-model-len=32768 \ --max-num-batched-tokens=32768 \ --tensor-parallel-size 16 \ --enable-expert-parallel \ --enable-prefix-caching \ --enable-chunked-prefill \ --distributed-executor-backend=ray \ --trust-remote-code \ --served-model-name deepseek-r1 ``` slave node: ```bash ray start --block --address=$HEADPODIP:6379 ``` get error: ```bash 2025-04-16 10:27:16,259 INFO usage_lib.py:467 -- Usage stats collection is enabled by default without user confirmation because this terminal is detected to be non-interactive. To disable this, add `--disable-usage-stats` to the command that starts the cluster, or run the following command: `ray disable-usage-stats` before starting the cluster. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details. 2025-04-16 10:27:16,259 INFO scripts.py:865 -- Local node IP: 172.20.155.155 2025-04-16 10:27:19,206 SUCC scripts.py:902 -- -------------------- 2025-04-16 10:27:19,206 SUCC scripts.py:903 -- Ray runtime started. 2025-04-16 10:27:19,206 SUCC scripts.py:904 -- ---...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: odes and TP = 16（include vllm v0.8.4 v0.7.3 v0.7.2 V0 V1 engine） bug;ray;stale ### Your current environment ### 🐛 Describe the bug start command: head node: ```bash ray start --head --port=6379 && \ vllm serve $MODELPAT...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nect to this Ray cluster: 2025-04-16 10:27:19,207 INFO scripts.py:923 -- import ray 2025-04-16 10:27:19,207 INFO scripts.py:924 -- ray.init() 2025-04-16 10:27:19,207 INFO scripts.py:955 -- To terminate the Ray runtime,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distrib...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: --served-model-name deepseek-r1 ``` slave node: ```bash ray start --block --address=$HEADPODIP:6379 ``` get error: ```bash 2025-04-16 10:27:16,259 INFO usage_lib.py:467 -- Usage stats collection is enabled by default wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: efix-caching \ --enable-chunked-prefill \ --distributed-executor-backend=ray \ --trust-remote-code \ --served-model-name deepseek-r1 ``` slave node: ```bash ray start --block --address=$HEADPODIP:6379 ``` get error: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
