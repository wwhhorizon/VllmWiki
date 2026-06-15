# vllm-project/vllm#29688: Document Ray Serve LLM incompatibility with vLLM v1 engine for PD disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#29688](https://github.com/vllm-project/vllm/issues/29688) |
| 状态 | open |
| 标签 | ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Document Ray Serve LLM incompatibility with vLLM v1 engine for PD disaggregation

### Issue 正文摘录

## Summary vLLM v1 engine with `RayDistributedExecutor` is incompatible with Ray Serve LLM's `build_pd_openai_app` due to nested placement group conflicts. Users attempting PD (prefill/decode) disaggregation with Ray Serve LLM encounter silent failures. This should be documented to guide users toward working deployment patterns. ## Environment - **vLLM**: 0.10.0+ (v1 engine) - **Ray**: 2.43.0 - **Hardware**: AWS p5.48xlarge (8x H100 80GB) - **NIXL**: 0.7.1 ## Problem When deploying vLLM with Ray Serve LLM's PD disaggregation API: ```python from ray.serve.llm import build_pd_openai_app, LLMConfig app = build_pd_openai_app({ "prefill_config": prefill_llm_config, "decode_config": decode_llm_config, }) ``` The deployment fails with: ``` RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` ## Root Cause 1. Ray Serve LLM pre-allocates GPUs in a placement group 2. vLLM v1 detects Ray environment and uses `RayDistributedExecutor` 3. `RayDistributedExecutor` attempts to create its own placement group 4. Inner placement group fails because GPUs are already reserved This creates a fundamental conflict between the two resource allocation strategie...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: gine with `RayDistributedExecutor` is incompatible with Ray Serve LLM's `build_pd_openai_app` due to nested placement group conflicts. Users attempting PD (prefill/decode) disaggregation with Ray Serve LLM encounter sil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: penai_app` due to nested placement group conflicts. Users attempting PD (prefill/decode) disaggregation with Ray Serve LLM encounter silent failures. This should be documented to guide users toward working deployment pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gation API: ```python from ray.serve.llm import build_pd_openai_app, LLMConfig app = build_pd_openai_app({ "prefill_config": prefill_llm_config, "decode_config": decode_llm_config, }) ``` The deployment fails with: ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e":"kv_producer","kv_buffer_device":"cuda","kv_connector_extra_config":{"backends":["UCX"]}}' # Decode instance (kv_consumer) python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2-7B-Instruct \ --port 8200 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .10.0+ (v1 engine) - **Ray**: 2.43.0 - **Hardware**: AWS p5.48xlarge (8x H100 80GB) - **NIXL**: 0.7.1 ## Problem When deploying vLLM with Ray Serve LLM's PD disaggregation API: ```python from ray.serve.llm import build_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
