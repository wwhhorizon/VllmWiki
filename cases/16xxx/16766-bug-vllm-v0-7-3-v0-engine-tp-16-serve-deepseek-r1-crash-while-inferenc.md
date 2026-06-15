# vllm-project/vllm#16766: [Bug]: vllm-v0.7.3 V0 engine TP=16 serve DeepSeek-R1 Crash while inference

| 字段 | 值 |
| --- | --- |
| Issue | [#16766](https://github.com/vllm-project/vllm/issues/16766) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-v0.7.3 V0 engine TP=16 serve DeepSeek-R1 Crash while inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm-v0.7.3 V0 engine TP=16 serve DeepSeek-R1 Crash while inference ```bash 2*H800*8(80GB) ``` ```bash ray start --head --port=6379 && \ vllm serve $MODELPATH \ --max-num-seqs=16 \ --max-model-len=16384 \ --max-num-batched-tokens=16384 \ --tensor-parallel-size 16 \ --enable-prefix-caching \ --enable-chunked-prefill \ --distributed-executor-backend=ray \ --trust-remote-code \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --served-model-name deepseek-r1-250120 ``` ```bash ray start --block --address=$HEADPODIP:6379 ``` ```bash 2025-04-17 13:55:22,794 INFO usage_lib.py:467 -- Usage stats collection is enabled by default without user confirmation because this terminal is detected to be non-interactive. To disable this, add `--disable-usage-stats` to the command that starts the cluster, or run the following command: `ray disable-usage-stats` before starting the cluster. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details. 2025-04-17 13:55:22,795 INFO scripts.py:823 -- Local node IP: 172.20.141.222 2025-04-17 13:55:26,466 SUCC scripts.py:860 -- -------------------- 2025-04-17 13:55:26,466 SUCC scripts.py...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: vllm-v0.7.3 V0 engine TP=16 serve DeepSeek-R1 Crash while inference bug;stale ### Your current environment ### 🐛 Describe the bug vllm-v0.7.3 V0 engine TP=16 serve DeepSeek-R1 Crash while inference ```bash 2*H800*8(80GB...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nect to this Ray cluster: 2025-04-17 13:55:26,467 INFO scripts.py:881 -- import ray 2025-04-17 13:55:26,467 INFO scripts.py:882 -- ray.init() 2025-04-17 13:55:26,467 INFO scripts.py:913 -- To terminate the Ray runtime,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: 1 \ --served-model-name deepseek-r1-250120 ``` ```bash ray start --block --address=$HEADPODIP:6379 ``` ```bash 2025-04-17 13:55:22,794 INFO usage_lib.py:467 -- Usage stats collection is enabled by default without user c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: *8(80GB) ``` ```bash ray start --head --port=6379 && \ vllm serve $MODELPATH \ --max-num-seqs=16 \ --max-model-len=16384 \ --max-num-batched-tokens=16384 \ --tensor-parallel-size 16 \ --enable-prefix-caching \ --enable-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
