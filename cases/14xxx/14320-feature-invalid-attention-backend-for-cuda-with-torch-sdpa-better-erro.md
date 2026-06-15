# vllm-project/vllm#14320: [Feature]: `Invalid attention backend for cuda` with `TORCH_SDPA` better error message

| 字段 | 值 |
| --- | --- |
| Issue | [#14320](https://github.com/vllm-project/vllm/issues/14320) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: `Invalid attention backend for cuda` with `TORCH_SDPA` better error message

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With `vllm==0.7.3`, running: ```bash VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len 2048 --tensor-parallel-size 8 ``` I get this stack trace: ```none File "/path/to/.venv/lib/python3.12/site-packages/vllm/worker/model_runner.py", line 1062, in __init__ self.attn_backend = get_attn_backend( ^^^^^^^^^^^^^^^^^ File "/path/to/.venv/lib/python3.12/site-packages/vllm/attention/selector.py", line 95, in get_attn_backend return _cached_get_attn_backend( ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/.venv/lib/python3.12/site-packages/vllm/attention/selector.py", line 148, in _cached_get_attn_backend attention_cls = current_platform.get_attn_backend_cls( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/.venv/lib/python3.12/site-packages/vllm/platforms/cuda.py", line 171, in get_attn_backend_cls raise ValueError( ValueError: Invalid attention backend for cuda, with use_v1: False use_mla: False ``` It can be resolved by moving to: ```bash VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len 2048 --tensor-parallel-size 8 ``` The request is the error be better: - I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tention backend for cuda` with `TORCH_SDPA` better error message feature request;stale ### 🚀 The feature, motivation and pitch With `vllm==0.7.3`, running: ```bash VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve Qwen/Qwen2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: `Invalid attention backend for cuda` with `TORCH_SDPA` better error message feature request;stale ### 🚀 The feature, motivation and pitch With `vllm==0.7.3`, running: ```bash VLLM_ATTENTION_BACKEND=TORCH_SDPA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: `Invalid attention backend for cuda` with `TORCH_SDPA` better error message feature request;stale ### 🚀 The feature, motivation and pitch With `vllm==0.7.3`, running: ```bash VLLM_ATTENTION_BACKEND=TORCH_SDPA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ==0.7.3`, running: ```bash VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len 2048 --tensor-parallel-size 8 ``` I get this stack trace: ```none File "/path/to/.venv/lib/python3.12/s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
