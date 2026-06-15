# vllm-project/vllm#19052: [Bug]: vllm 0.9 image gives me gibberish

| 字段 | 值 |
| --- | --- |
| Issue | [#19052](https://github.com/vllm-project/vllm/issues/19052) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.9 image gives me gibberish

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` export VLLM_USE_V1=1 export VLLM_ROCM_USE_AITER=1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMERS_CACHE=/app/model/.cache/transformers export HF_HOME=/app/model/.cache/huggingface vllm serve \ /app/model/meta-llama/Llama-3.2-3B-Instruct \ --host 0.0.0.0 \ --port 8000 \ --served-model-name "Llama-3.2-3B-Instruct" \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 \ --dtype auto \ --trust-remote-code \ --tensor-parallel-size 1 \ --api-key "key" ``` then I curl from another terminal window ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer key" \ -d '{ "model": "Llama-3.2-3B-Instruct", "messages": [ { "role": "system", "content": "You are a helpful and concise assistant." }, { "role": "user", "content": "Explain the significance of the year 1984 in literature." } ], "max_tokens": 200, "temperature": 0.7 }' ``` I get : ``` {"id":"chatcmpl-ddfbf8b6a325424696f38af37585d1a7","object":"chat.completion","created":1748926719,"model":"Llama-3.2-3B-Instruct","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"The Relationsh...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: xport VLLM_USE_V1=1 export VLLM_ROCM_USE_AITER=1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMERS_CACHE=/app/model/.cache/transformers export HF_HOME=/app/model/.cache/huggingface vllm serve \ /app/model/meta-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: vllm 0.9 image gives me gibberish bug;rocm;stale ### Your current environment ### 🐛 Describe the bug ``` export VLLM_USE_V1=1 export VLLM_ROCM_USE_AITER=1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: =1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMERS_CACHE=/app/model/.cache/transformers export HF_HOME=/app/model/.cache/huggingface vllm serve \ /app/model/meta-llama/Llama-3.2-3B-Instruct \ --host 0.0.0.0 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug ``` export VLLM_USE_V1=1 export VLLM_ROCM_USE_AITER=1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMERS_CACHE=/app/model/.cache/transformers export HF_HOME=/app/model/.cache/huggingface v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm 0.9 image gives me gibberish bug;rocm;stale ### Your current environment ### 🐛 Describe the bug ``` export VLLM_USE_V1=1 export VLLM_ROCM_USE_AITER=1 export HSA_OVERRIDE_GFX_VERSION=11.0.0 export TRANSFORMER...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
