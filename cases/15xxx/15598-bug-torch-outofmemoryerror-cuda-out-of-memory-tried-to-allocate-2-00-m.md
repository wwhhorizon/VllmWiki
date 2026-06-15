# vllm-project/vllm#15598: [Bug]:torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 6 has a total capacity of 44.53 GiB of which 448.00 KiB is free.

| 字段 | 值 |
| --- | --- |
| Issue | [#15598](https://github.com/vllm-project/vllm/issues/15598) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 6 has a total capacity of 44.53 GiB of which 448.00 KiB is free.

### Issue 正文摘录

### Your current environment 1.Four L40S machines, each with 8 GPUs。 2.cuda 12.4。 3.vllm 0.7.3。 4.Each execution environment variable export GLOO_SOCKET_IFNAME=ens3 5.ray status ` (vllm) root@gpu01:/work# ray status ======== Autoscaler status: 2025-03-27 13:20:23.684121 ======== Node status --------------------------------------------------------------- Active: 1 node_8de0d2a664613d27ee8af540a49494d5f20d668a5ee4419df7a1a239 1 node_c8f2e7f66aac753444f342fd08a6b5594b4d69f0cbd1d8f233536c4e 1 node_07469f6feab5890d5ba500dc53e8525fd0cb437fd3e5e0f6071c7dca 1 node_01fbdcf5361fde5871bcd45a2e2dee37aa7788decc9e557bd56a3a70 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/256.0 CPU 0.0/32.0 GPU 0B/1.28TiB memory 0B/565.81GiB object_store_memory Demands: (no resource demands) ` ### 🐛 Describe the bug 1.When starting the model using the following command (without adding the -- enforce-eager parameter): `vllm serve /ai_models/hf_hub/models/deepseek-ai/DeepSeek-R1 \ --trust-remote-code \ --served-model-name DeepSeek-R1 \ --max-model-len 16384 \ --host 0.0.0.0 \ --port 9999 \ --tensor-parallel-size 8 \ -...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: base.py:620] Error executing method 'initialize_cache'. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=206994, ip=192.168.10.25) ERROR 03-27 10:29:13 [worker_base.py:620] Traceback (most recen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 6 has a total capacity of 44.53 GiB of which 448.00 KiB is free. bug ### Your current environment 1.Four L40S machines, each with 8 GPUs。 2.cuda 12.4。 3.vllm 0.7.3。...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/attention/backends/mla/common.py", line 1410, in forward (RayWorkerWrapper pid=206994, ip=192.168.10.25) ERROR 03-27 10:29:13 [worker_base.py:620] output[nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]:torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.00 MiB. GPU 6 has a total capacity of 44.53 GiB of which 448.00 KiB is free. bug ### Your current environment 1.Four L40S machines, each with 8 GPUs。...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ctivation peak memory takes 1.52GiB; the rest of the memory reserved for KV Cache is 21.20GiB. [repeated 30x across cluster] (RayWorkerWrapper pid=206994, ip=192.168.10.25) ERROR 03-27 10:29:13 [worker_base.py:620] Erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
