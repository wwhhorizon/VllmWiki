# vllm-project/vllm#24758: [Bug]: fix when clean s3 tmp dir after cannot running  serve

| 字段 | 值 |
| --- | --- |
| Issue | [#24758](https://github.com/vllm-project/vllm/issues/24758) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fix when clean s3 tmp dir after cannot running  serve

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Because `__del__` method define in ObjectStorageModel, it will clean tmp file from s3 cache file, but when after use this path to read file, this path is not exist, so is considered is str model, then use hf to download. and ObjectStorageModel is a Local variables, when it level this method, it will be reference count is 0, after `__del__` method by exec. so we nned remote this method, only use single handler to clean tmp dir. https://github.com/vllm-project/vllm/blob/f17c075884009a3bfb7c66cb0897719b8e18f196/vllm/transformers_utils/runai_utils.py#L68-L69 ```shell INFO 09-12 08:12:59 [v1/worker/gpu_model_runner.py:2934] Graph capturing finished in 6 secs, took 0.07 GiB INFO 09-12 08:12:59 [v1/engine/core.py:218] init engine (profile, create kv cache, warmup model) took 44.23 seconds ERROR 09-12 08:12:59 [v1/engine/core.py:718] EngineCore failed to start. ERROR 09-12 08:12:59 [v1/engine/core.py:718] Traceback (most recent call last): ERROR 09-12 08:12:59 [v1/engine/core.py:718] File "/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py", line 479, in cached_files ERROR 09-12 08:12:59 [v1/engine/core.py:718] hf_hub_down...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ### 🐛 Describe the bug Because `__del__` method define in ObjectStorageModel, it will clean tmp file from s3 cache file, but when after use this path to read file, this path is not exist, so is considered is str model,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. WARNING 09-12 08:13:02 [platforms/interface.py:531] Current platform cuda does not have '__iter__' attribute. Traceback (most recent call last): File "/usr/lib/python3.12/runpy.py", line 198, in _run_module_as_main...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , took 0.07 GiB INFO 09-12 08:12:59 [v1/engine/core.py:218] init engine (profile, create kv cache, warmup model) took 44.23 seconds ERROR 09-12 08:12:59 [v1/engine/core.py:718] EngineCore failed to start. ERROR 09-12 08...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mance attention_kv_cache;frontend_api;model_support cache;cuda crash env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: INFO 09-12 08:12:59 [v1/engine/core.py:218] init engine (profile, create kv cache, warmup model) took 44.23 seconds ERROR 09-12 08:12:59 [v1/engine/core.py:718] EngineCore failed to start. ERROR 09-12 08:12:59 [v1/engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
