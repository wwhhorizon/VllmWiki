# vllm-project/vllm#17412: [Bug]: Llama 4 model config from meta not working

| 字段 | 值 |
| --- | --- |
| Issue | [#17412](https://github.com/vllm-project/vllm/issues/17412) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;moe;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 4 model config from meta not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Met this issue when running with vllm `0.8.5` with offline mode for `meta-llama/Llama-4-Scout-17B-16E-Instruct` (downloaded from https://www.llama.com/) on 4 H100s, and build vllm from source `vllm-0.8.5.dev346+ga6977dbd1.precompiled` and got the same. Should I run with the model weights from HF? ```text [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] WorkerProc failed to start. [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] Traceback (most recent call last): [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] File "/net/storage149/mnt/md0/zhuoran/miniconda3/envs/fmwork-v22-cu126-vllm084/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 409, in worker_main [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] worker = WorkerProc(*args, **kwargs) [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_execu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: B-16E-Instruct` (downloaded from https://www.llama.com/) on 4 H100s, and build vllm from source `vllm-0.8.5.dev346+ga6977dbd1.precompiled` and got the same. Should I run with the model weights from HF? ```text [1;36m(Vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama 4 model config from meta not working bug ### Your current environment ### 🐛 Describe the bug Met this issue when running with vllm `0.8.5` with offline mode for `meta-llama/Llama-4-Scout-17B-16E-Instruct` (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -4-Scout-17B-16E-Instruct` (downloaded from https://www.llama.com/) on 4 H100s, and build vllm from source `vllm-0.8.5.dev346+ga6977dbd1.precompiled` and got the same. Should I run with the model weights from HF? ```tex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: i_build;distributed_parallel;hardware_porting;model_support;moe cuda;moe;triton build_error;crash env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: =60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [1;36m(VllmWorker rank=0 pid=60515)[0;0m ERROR 04-29 19:43:23 [multiproc_executor.py:435] ^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
