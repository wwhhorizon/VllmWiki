# vllm-project/vllm#27059: [Feature]: Batch-invariant Inference Support for VLMs

| 字段 | 值 |
| --- | --- |
| Issue | [#27059](https://github.com/vllm-project/vllm/issues/27059) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Batch-invariant Inference Support for VLMs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be great if we can have the determinism (aka batch invariance) support for VLM models such as Qwen-VL Currently the VIT attn backend can't work with the flag `VLLM_KERNEL_OVERRIDE_BATCH_INVARIANT=1 ` project: https://github.com/orgs/vllm-project/projects/29 ``` (EngineCore_DP0 pid=16503) (EngineCore_DP0 pid=16503) INFO 10-16 16:02:03 [default_loader.py:314] Loading weights took 11.20 seconds (EngineCore_DP0 pid=16503) INFO 10-16 16:02:03 [gpu_model_runner.py:2904] Model loading took 62.4358 GiB and 93.523430 seconds (EngineCore_DP0 pid=16503) INFO 10-16 16:02:04 [gpu_model_runner.py:3670] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. (EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] EngineCore failed to start. (EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] Traceback (most recent call last): (EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] File "/opt/conda/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 788, in run_engine_core (EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] engine_core = Eng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Batch-invariant Inference Support for VLMs feature request;stale ### 🚀 The feature, motivation and pitch It would be great if we can have the determinism (aka batch invariance) support for VLM models such as...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: variance) support for VLM models such as Qwen-VL Currently the VIT attn backend can't work with the flag `VLLM_KERNEL_OVERRIDE_BATCH_INVARIANT=1 ` project: https://github.com/orgs/vllm-project/projects/29 ``` (EngineCor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: op/__init__.py", line 109, in run (APIServer pid=16294) return __asyncio.run( (APIServer pid=16294) ~~~~~~~~~~~~~^ (APIServer pid=16294) wrapper(), (APIServer pid=16294) ^^^^^^^^^^ (APIServer pid=16294) ... ... (APIServ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure, motivation and pitch It would be great if we can have the determinism (aka batch invariance) support for VLM models such as Qwen-VL Currently the VIT attn backend can't work with the flag `VLLM_KERNEL_OVERRIDE_BATC...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=16503) ERROR 10-16 16:02:05 [core.py:797] ~~~~~~~~~~~~~~~~~~...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
