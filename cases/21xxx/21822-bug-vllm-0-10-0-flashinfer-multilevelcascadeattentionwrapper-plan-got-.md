# vllm-project/vllm#21822: [Bug]: vllm==0.10.0 + flashinfer, MultiLevelCascadeAttentionWrapper.plan() got an unexpected keyword argument 'kv_data_type'

| 字段 | 值 |
| --- | --- |
| Issue | [#21822](https://github.com/vllm-project/vllm/issues/21822) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | attention;fp8;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm==0.10.0 + flashinfer, MultiLevelCascadeAttentionWrapper.plan() got an unexpected keyword argument 'kv_data_type'

### Issue 正文摘录

### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-af9dc182ee24be77a81ade64a15aa73250440a81224b9c4b7df897d025410b30) flashinfer v0.2.8rc1 GPU: 1 x H100 ### 🐛 Describe the bug Entrypoint: ``` VLLM_ATTENTION_BACKEND=FLASHINFER python3 -m vllm.entrypoints.openai.api_server \ --model /data/model/ \ --served-model-name Qwen3-32B \ --disable-log-requests \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --reasoning-parser qwen3 ``` After some successful requests, it crashes with this error: ``` ERROR 07-29 11:19:43 [core.py:634] EngineCore encountered a fatal error. ERROR 07-29 11:19:43 [core.py:634] Traceback (most recent call last): ERROR 07-29 11:19:43 [core.py:634] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 625, in run_engine_core ERROR 07-29 11:19:43 [core.py:634] engine_core.run_busy_loop() ERROR 07-29 11:19:43 [core.py:634] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 652, in run_busy_loop ERROR 07-29 11:19:43 [core.py:634] self._process_engine_step() ERROR 07-29 11:19:43 [core.py:634] File "/usr/local/lib/py...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: tionWrapper.plan() got an unexpected keyword argument 'kv_data_type' bug;stale ### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: type' bug;stale ### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-af9dc182ee24be77a81ade64a15aa73250440a81224b9c4b7d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 'kv_data_type' bug;stale ### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-af9dc182ee24be77a81ade64a15aa73250440a812...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: keyword argument 'kv_data_type' bug;stale ### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-af9dc182ee24be77a81ade64...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: vllm==0.10.0 + flashinfer, MultiLevelCascadeAttentionWrapper.plan() got an unexpected keyword argument 'kv_data_type' bug;stale ### Your current environment Model: Qwen3-32B FP8 quant docker vllm-openai v0.10.0 (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
