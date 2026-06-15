# vllm-project/vllm#1710: Crash with `--tensor-parallel-size` in the docker container

| 字段 | 值 |
| --- | --- |
| Issue | [#1710](https://github.com/vllm-project/vllm/issues/1710) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | operator;quantization |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Crash with `--tensor-parallel-size` in the docker container

### Issue 正文摘录

I build the docker image from the master and ran into this error while serving 13B model in the docker container. ``` (base) ubuntu@ip-10-217-30-221:~$ docker run --runtime nvidia --gpus all \ > -p 8000:8000 \ > -v :/mnt/model/ \ > vllm:latest \ > --host 0.0.0.0 \ > --model="/mnt/model/" \ > --tensor-parallel-size 2 WARNING 11-18 03:39:14 config.py:128] None quantization is not fully optimized yet. The speed can be slower than non-quantized models. 2023-11-18 03:39:16,283 WARNING services.py:1996 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 67108864 bytes available. This will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM. 2023-11-18 03:39:16,440 INFO worker.py:1673 -- Started a local Ray instance. INFO 11-18 03:39:17 llm_engine.py:72] Initializing an LLM engine with config: model='/mnt/model/', tokenizer='/mnt/model/', tokenizer_mode=auto, revision=None, tokenizer_revision...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Crash with `--tensor-parallel-size` in the docker container I build the docker image from the master and ran into this error while serving 13B model in the docker container. ``` (base) ubuntu@ip-10-217-30-221:~$ docker...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: > --tensor-parallel-size 2 WARNING 11-18 03:39:14 config.py:128] None quantization is not fully optimized yet. The speed can be slower than non-quantized models. 2023-11-18 03:39:16,283 WARNING services.py:1996 -- WARNI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e docker image from the master and ran into this error while serving 13B model in the docker container. ``` (base) ubuntu@ip-10-217-30-221:~$ docker run --runtime nvidia --gpus all \ > -p 8000:8000 \ > -v :/mnt/model/ \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: as._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.lib, pandas._libs.ops, pyarrow._co...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
