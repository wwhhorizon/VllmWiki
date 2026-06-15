# vllm-project/vllm#27508: [Bug]: openai/gpt-oss-120b can't run on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#27508](https://github.com/vllm-project/vllm/issues/27508) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai/gpt-oss-120b can't run on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I followed the guide [here](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#h100-h200), but installed version 0.11 of vllm instead of 0.10.2, as I'm using Python 3.13. When running `vllm serve openai/gpt-oss-120b --async-scheduling` i get ```python-traceback (Worker pid=224024) INFO 10-25 13:08:43 [gpu_worker.py:298] Available KV cache memory: -2.28 GiB (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] Traceback (most recent call last): (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] File "/opt/conda/envs/vllm_env/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] File "/opt/conda/envs/vllm_env/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] super().__init__(vllm_config, executor_class, log_stats, (Engin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ibe the bug I followed the guide [here](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#h100-h200), but installed version 0.11 of vllm instead of 0.10.2, as I'm using Python 3.13. When running `vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: openai/gpt-oss-120b can't run on H100 bug;stale ### Your current environment ### 🐛 Describe the bug I followed the guide [here](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#h100-h200), but...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: openai/gpt-oss-120b can't run on H100 bug;stale ### Your current environment ### 🐛 Describe the bug I followed the guide [here](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#h100-h200), but...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: ck (Worker pid=224024) INFO 10-25 13:08:43 [gpu_worker.py:298] Available KV cache memory: -2.28 GiB (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=223840)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 43 [core.py:708] raise ValueError("No available memory for the cache blocks. " (EngineCore_DP0 pid=223840) ERROR 10-25 13:08:43 [core.py:708] "Try increasing `gpu_memory_utilization` when " (EngineCore_DP0 pid=223840) E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
