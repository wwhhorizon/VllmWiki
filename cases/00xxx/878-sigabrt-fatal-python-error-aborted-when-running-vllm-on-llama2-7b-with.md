# vllm-project/vllm#878: SIGABRT - Fatal Python error: Aborted when running vllm on llama2-7b with --tensor-parallel-size 2

| 字段 | 值 |
| --- | --- |
| Issue | [#878](https://github.com/vllm-project/vllm/issues/878) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> SIGABRT - Fatal Python error: Aborted when running vllm on llama2-7b with --tensor-parallel-size 2

### Issue 正文摘录

In my setup, vLLM works fine when running llama2-7b with 1 GPU. But when running it with multiple gpus, it runs into a Fatal error every time. Sharing the traces below. This is persistent - that is there is no single instance when I am able to run vllm with multiple gpus. Can you please share thoughts on what could be the issue and how to go about it ? -- Environment-- CentOS 7.9 Cuda 11.8, V11.8.89 Nvidia Driver 530.30.2 A100 host with 8 GPU cards python 3.10 vLLM 0.1.3 /dev/shm 60G ulimit -u 30000 --- Error Trace 1 --- python3.10 -m vllm.entrypoints.api_server --model "models/llama-2-7b-hf" --swap-space 1 --disable-log-requests --disable-log-stats --tensor-parallel-size 2 2023-08-25 08:22:59,206 INFO worker.py:1627 -- Started a local Ray instance. View the dashboard at 127.0.0.1:8265 INFO 08-25 08:23:00 llm_engine.py:70] Initializing an LLM engine with config: model='models/llama-2-7b-hf', tokenizer='models/llama-2-7b-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-25 08:23:00 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokeniz...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ._linalg, torch._C._nested, torch._C._nn, torch._C._sparse, torch._C._special, simplejson._speedups, yaml._yaml, sentencepiece._sentencepiece, psutil._psutil_linux, psutil._psutil_posix, msgpack._cmsgpack, setproctitle,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: SIGABRT - Fatal Python error: Aborted when running vllm on llama2-7b with --tensor-parallel-size 2 In my setup, vLLM works fine when running llama2-7b with 1 GPU. But when running it with multiple gpus, it runs into a F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: could be the issue and how to go about it ? -- Environment-- CentOS 7.9 Cuda 11.8, V11.8.89 Nvidia Driver 530.30.2 A100 host with 8 GPU cards python 3.10 vLLM 0.1.3 /dev/shm 60G ulimit -u 30000 --- Error Trace 1 --- pyt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: as._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.tslib, pandas._libs.lib, pandas._l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: er='models/llama-2-7b-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-25 08:23:00 tokeniz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
