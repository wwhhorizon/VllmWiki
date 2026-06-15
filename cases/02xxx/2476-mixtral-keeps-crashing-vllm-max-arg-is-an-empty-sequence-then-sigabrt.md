# vllm-project/vllm#2476: Mixtral keeps crashing vLLM.  max() arg is an empty sequence then SIGABRT

| 字段 | 值 |
| --- | --- |
| Issue | [#2476](https://github.com/vllm-project/vllm/issues/2476) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel;operator |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral keeps crashing vLLM.  max() arg is an empty sequence then SIGABRT

### Issue 正文摘录

``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/vllm.git pip install mosaicml-turbo --upgrade pip install git+https://github.com/stanford-futuredata/megablocks.git pip install fschat==0.2.34 ``` ``` export CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model mistralai/Mixtral-8x7B-Instruct-v0.1 --seed 1234 --tensor-parallel-size=2 --max-num-batched-tokens=153600 ``` Sometimes there are aborted generations: ``` INFO 01-18 01:53:25 async_llm_engine.py:134] Aborted request cmpl-2b7bd3e1f8cb434e9f98e8b3ea2c58e6. ``` But at some point, every day, we hit this: ``` INFO 01-18 06:58:46 async_llm_engine.py:384] Received request cmpl-dfb5d2e7322a4697b8a0184901953e56: prompt: ' [INST] MATCH DETAILS\n- Tournament: NBA\n- Sport: Basketball\n- Season: NBA 23/24\n- HomeTeam: Detroit Pistons\n- AwayTeam: Minnesota Timberwolves> INFO 01-18 06:58:47 async_llm_engine.py:134] Aborted request cmpl-6bd865032aef41c6b135d86278e38264. Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/vllm.git pip install mosaicml-turbo --upgrade pip install git+https://github.com/stanford-futuredata/me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s crashing vLLM. max() arg is an empty sequence then SIGABRT ``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.3%, CPU KV cache usage: 0.0% INFO: 38.128.232.144:34135 - "POST /v1/completions HTTP/1.1" 200 OK INFO 01-18 07:29:06 async_llm_e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rbo --upgrade pip install git+https://github.com/stanford-futuredata/megablocks.git pip install fschat==0.2.34 ``` ``` export CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed generations: ``` INFO 01-18 01:53:25 async_llm_engine.py:134] Aborted request cmpl-2b7bd3e1f8cb434e9f98e8b3ea2c58e6. ``` But at some point, every day, we hit this: ``` INFO 01-18 06:58:46 async_llm_engine.py:384] Rec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
