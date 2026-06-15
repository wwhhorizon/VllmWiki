# vllm-project/vllm#14263: [Bug]: Dose V1  support MLA + PP now? Raise error while using PP+TP+V1.

| 字段 | 值 |
| --- | --- |
| Issue | [#14263](https://github.com/vllm-project/vllm/issues/14263) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dose V1  support MLA + PP now? Raise error while using PP+TP+V1.

### Issue 正文摘录

Device: 3xL20x8, DeepSeek-R1, PP=3, TP=8, VLLM_USE_V1=1 Launch: ```bash python3 -m vllm.entrypoints.openai.api_server --dtype=auto --tensor-parallel-size=8 --host=0.0.0.0 --port=80 --tokenizer-mode=slow --model=/DeepSeek-R1 --block-size=32 --swap-space=16 --g pu-memory-utilization=0.9 --pipeline-parallel-size=3 --max-num-seqs=48 --trust-remote-code --no-enable-prefix-caching --enable-chunked-prefill=True --max-model-len=16384 --max-num-batched-tokens=2048 --served-model-name=/DeepSeek-R1 ``` Error: ``` [2025-03-05 14:28:30,815] [INFO] [MainThread] [vllm.transformers_utils.config] >>> Replacing legacy 'type' key with 'rope_type' [2025-03-05 14:28:34,452] [INFO] [MainThread] [vllm.platforms] >>> Automatically detected platform cuda. [2025-03-05 14:28:37,141] [INFO] [MainThread] [vllm.config] >>> This model supports multiple tasks: {'generate', 'embed', 'classify', 'score', 'reward'}. Defaulting to 'generate'. [2025-03-05 14:28:37,343] [INFO] [MainThread] [vllm.config] >>> Defaulting to use ray for distributed inference [2025-03-05 14:28:37,343] [INFO] [MainThread] [vllm.config] >>> Chunked prefill is enabled with max_num_batched_tokens=2048. [2025-03-05 14:28:37,344] [WARNING] [Main...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _V1=1 Launch: ```bash python3 -m vllm.entrypoints.openai.api_server --dtype=auto --tensor-parallel-size=8 --host=0.0.0.0 --port=80 --tokenizer-mode=slow --model=/DeepSeek-R1 --block-size=32 --swap-space=16 --g pu-memory...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: seqs=48 --trust-remote-code --no-enable-prefix-caching --enable-chunked-prefill=True --max-model-len=16384 --max-num-batched-tokens=2048 --served-model-name=/DeepSeek-R1 ``` Error: ``` [2025-03-05 14:28:30,815] [INFO] [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 28:30,815] [INFO] [MainThread] [vllm.transformers_utils.config] >>> Replacing legacy 'type' key with 'rope_type' [2025-03-05 14:28:34,452] [INFO] [MainThread] [vllm.platforms] >>> Automatically detected platform cuda. [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =8 --host=0.0.0.0 --port=80 --tokenizer-mode=slow --model=/DeepSeek-R1 --block-size=32 --swap-space=16 --g pu-memory-utilization=0.9 --pipeline-parallel-size=3 --max-num-seqs=48 --trust-remote-code --no-enable-prefix-ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -tensor-parallel-size=8 --host=0.0.0.0 --port=80 --tokenizer-mode=slow --model=/DeepSeek-R1 --block-size=32 --swap-space=16 --g pu-memory-utilization=0.9 --pipeline-parallel-size=3 --max-num-seqs=48 --trust-remote-code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
