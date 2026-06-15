# vllm-project/vllm#39996: [Bug] Fatal AssertionError: Encoder KV cache fails to evict tokens, exceeding max_model_len in long-lived WebSocket sessions

| 字段 | 值 |
| --- | --- |
| Issue | [#39996](https://github.com/vllm-project/vllm/issues/39996) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Fatal AssertionError: Encoder KV cache fails to evict tokens, exceeding max_model_len in long-lived WebSocket sessions

### Issue 正文摘录

### Your current environment ### Description I am developing an Always-On voice chatbot using Voxtral via the vLLM Realtime WebSocket API. In this architecture, the WebSocket stays open indefinitely, continuously streaming audio chunks (including silence/ambient noise) to the backend. I have discovered that the **Encoder KV Cache** accumulates acoustic tokens indefinitely. When the total token count reaches `max_model_len`, instead of evicting old tokens (as a sliding window should), vLLM attempts to append a new token, causing a fatal `AssertionError` that kills the WebSocket session. ### Steps to Reproduce 1. Start vLLM on an isolated 24GB VRAM GPU RTX3090TI: `vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --max-model-len 16384` 2. Open a WebSocket connection to `/v1/realtime`. 3. Continuously stream base64 PCM audio chunks (16kHz, ~125 chunks/sec) representing room silence. 4. Wait for approximately 15 minutes (1 min from 0% to 10%, 1 min each 1% more, stabilizes for several minutes on 19%). 5. Observe the GPU KV cache usage slowly plateau around 19-20%. 6. The session abruptly crashes. ### Actual Behavior (The Smoking Gun) The crash is not an Out-Of-Memory error. It is a h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 2274342) assert end_idx max_model_len: 16384 ### Environment vLLM Version: 0.19.1rc1.dev335+g10e49d263 (also tested on 0.15.2rc1) Model: mistralai/Voxtral-Mini-4B-Realtime-2602 GPU: Isolated 24GB VRAM (Nvidia) max_model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: .com (raw.githubusercontent.com)|185.199.110.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 35090 (34K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[=======================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: voice chatbot using Voxtral via the vLLM Realtime WebSocket API. In this architecture, the WebSocket stays open indefinitely, continuously streaming audio chunks (including silence/ambient noise) to the backend. I have...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: al AssertionError: Encoder KV cache fails to evict tokens, exceeding max_model_len in long-lived WebSocket sessions bug ### Your current environment ### Description I am developing an Always-On voice chatbot using Voxtr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: inuously streaming audio chunks (including silence/ambient noise) to the backend. I have discovered that the **Encoder KV Cache** accumulates acoustic tokens indefinitely. When the total token count reaches `max_model_l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
