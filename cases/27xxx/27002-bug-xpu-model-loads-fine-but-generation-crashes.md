# vllm-project/vllm#27002: [Bug]: XPU - Model loads fine but generation crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#27002](https://github.com/vllm-project/vllm/issues/27002) |
| 状态 | closed |
| 标签 | bug;intel-gpu;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: XPU - Model loads fine but generation crashes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to test some models, i.e. LFM2 via `vllm serve LiquidAI/LFM2-1.2B --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 -O0` or granite 4 h via `vllm serve ibm-granite/granite-4.0-h-micro --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 -O0` (note: using jikunshang's branch to make the granite model load in first place), I am able to load the models, however trying to generate anything results in EngineCore unexpectedly dying. Few cases with different errors: ``` (APIServer pid=10774) INFO: 127.0.0.1:40202 - "POST /v1/completions HTTP/1.1" 200 OK (APIServer pid=10774) ERROR 10-16 10:40:41 [core_client.py:564] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. (APIServer pid=10774) ERROR 10-16 10:40:41 [async_llm.py:480] AsyncLLM output_handler failed. (APIServer pid=10774) ERROR 10-16 10:40:41 [async_llm.py:480] Traceback (most recent call last): (APIServer pid=10774) ERROR 10-16 10:40:41 [async_llm.py:480] File "/mnt/Mediaz/Projekt/LLMao/localenv/lib/python3.12/site-packages/vllm-0.11.0+xpu-py3.12.egg/vllm/v1/engine/async_llm.py", line 439, in output_handler (APIServer pid=1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_dep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mnt/Mediaz/Projekt/LLMao/vllm-test/localenv/lib/python3.12/site-packages/triton/backends/intel/include/sycl_functions.h:82: std::tuple create_module(ze_context_handle_t, ze_device_handle_t, uint8_t *, size_t, const char...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 🙏 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: XPU - Model loads fine but generation crashes bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug When trying to test some models, i.e. LFM2 via `vllm serve LiquidAI/LFM2-1.2B --dtype half --m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: XPU - Model loads fine but generation crashes bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug When trying to test some models, i.e. LFM2 via `vllm serve LiquidAI/LFM2-1.2B --dtype half --m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
