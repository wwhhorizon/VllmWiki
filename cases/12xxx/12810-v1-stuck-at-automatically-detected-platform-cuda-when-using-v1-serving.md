# vllm-project/vllm#12810: [V1]: Stuck at "Automatically detected platform cuda" when using V1 serving llava-next

| 字段 | 值 |
| --- | --- |
| Issue | [#12810](https://github.com/vllm-project/vllm/issues/12810) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [V1]: Stuck at "Automatically detected platform cuda" when using V1 serving llava-next

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python model_path="./llava-v1.6-mistral-7b-hf" model = LLM( model=model_path, trust_remote_code=True, max_model_len=8192, # Otherwise, it may not fit in smaller GPUs limit_mm_per_prompt={"image": 3}, gpu_memory_utilization=0.8, enable_prefix_caching=True ) ``` cmd: VLLM_ENABLE_V1_MULTIPROCESSING=1 VLLM_USE_V1=1 bash bootstrap.sh get stuck at: ``` [2025-02-06 06:30:46 +0000] [59332] [INFO] Starting gunicorn 20.1.0 [2025-02-06 06:30:46 +0000] [59332] [INFO] Listening at: http://[::]:10849 (59332) [2025-02-06 06:30:46 +0000] [59332] [INFO] Using worker: euler.worker.SyncWorker [2025-02-06 06:30:46 +0000] [59333] [INFO] Booting worker with pid: 59333 INFO 02-06 06:30:51 __init__.py:183] Automatically detected platform cuda. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t bug ### Your current environment ### 🐛 Describe the bug ```python model_path="./llava-v1.6-mistral-7b-hf" model = LLM( model=model_path, trust_remote_code=True, max_model_len=8192, # Otherwise, it may not fit in small...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [V1]: Stuck at "Automatically detected platform cuda" when using V1 serving llava-next bug ### Your current environment ### 🐛 Describe the bug ```python model_path="./llava-v1.6-mistral-7b-hf" model = LLM( model=model_p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
