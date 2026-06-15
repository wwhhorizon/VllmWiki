# vllm-project/vllm#1111: Bug - vllm not working for L4 GPUs and tensor_parallel_size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#1111](https://github.com/vllm-project/vllm/issues/1111) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug - vllm not working for L4 GPUs and tensor_parallel_size > 1

### Issue 正文摘录

Hello, I'm trying to deploy a model using 2 L4 GPUs (and tensor_parallel_size=2), but it is failing. With 1 L4 GPU and tensor_parallel_size=1 is working fine. Code to reproduce the error: ```python from vllm import LLM llm = LLM(model="gpt2", tensor_parallel_size=2) ``` Error stack trace: ``` 2023-09-20 11:37:58,722 WARNING services.py:1889 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 46972928 bytes available. This will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM. 2023-09-20 11:37:59,864 INFO worker.py:1642 -- Started a local Ray instance. INFO 09-20 11:38:01 llm_engine.py:72] Initializing an LLM engine with config: model='gpt2', tokenizer='gpt2', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) (RayWorker pid=4856) *** SIGBUS received at time=16952098...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ize=1 is working fine. Code to reproduce the error: ```python from vllm import LLM llm = LLM(model="gpt2", tensor_parallel_size=2) ``` Error stack trace: ``` 2023-09-20 11:37:58,722 WARNING services.py:1889 -- WARNING:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: zer='gpt2', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) (RayWorker pid=4856) *** SIGBUS recei...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: for L4 GPUs and tensor_parallel_size > 1 Hello, I'm trying to deploy a model using 2 L4 GPUs (and tensor_parallel_size=2), but it is failing. With 1 L4 GPU and tensor_parallel_size=1 is working fine. Code to reproduce t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: inux, psutil._psutil_posix, setproctitle, yaml._yaml, ray._raylet, _cffi_backend, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._comm...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
