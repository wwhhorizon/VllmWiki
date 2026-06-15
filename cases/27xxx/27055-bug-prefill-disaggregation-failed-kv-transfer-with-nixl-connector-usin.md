# vllm-project/vllm#27055: [Bug]: Prefill disaggregation failed kv transfer with NiXL connector using LIBFABRIC backend with vllm 0.11 and nixl 0.6.1

| 字段 | 值 |
| --- | --- |
| Issue | [#27055](https://github.com/vllm-project/vllm/issues/27055) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefill disaggregation failed kv transfer with NiXL connector using LIBFABRIC backend with vllm 0.11 and nixl 0.6.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Disaggregated prefill produced garbage output with LIBFABRIC-backend NIXL connector in vllm v0.11.0 and NiXL 0.6.1. I dumped the KV tensors and see nothing is actually transferred. I don't see hangs, crashes, or errors from server logs, and everything looks like normal. The same setting **works fine** for UCX backend. I tested NiXL with LIBFABRIC backend using https://github.com/ai-dynamo/nixl/blob/main/examples/python/blocking_send_recv_example.py and it works fine. Output with LIBFABRIC backend ``` curl -s http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "meta-llama/Llama-3.1-8B-Instruct", "prompt": ["a KV cache is"], "max_tokens": 200, "temperature": 0 }' {"id":"cmpl-5510222c-a6ef-46dd-a572-936452011ebd","object":"text_completion","created":1760653810,"model":"meta-llama/Llama-3.1-8B-Instruct","choices":[{"index":0,"text":" (a) 0.5, (b) 0.25, (c) 0.5, (d) 0.25, (e) 0.5.\n* 2. A particle of mass \\(m\\) is projected with speed \\(v_{0}\\) from the origin. Find the equation of the path of the particle. (a) \\(y=\\frac{1}{2}gt^{2}\\), (b) \\(x=v_{0}t\\), (c) \\(y=\\frac{1}{2}gt^{2}+\\frac{v_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Prefill disaggregation failed kv transfer with NiXL connector using LIBFABRIC backend with vllm 0.11 and nixl 0.6.1 bug ### Your current environment ### 🐛 Describe the bug Disaggregated prefill produced garbage o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "meta-llama/Llama-3.1-8B-Instruct", "prompt": ["a KV cache is"], "max_tokens": 200, "temperature": 0 }' {"id":"cmpl-5510222c-a6ef-46dd-a57...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: for decode instance to start..." wait_for_server $DECODE_PORT # Build the command for the proxy server with all the hosts and ports echo "Starting proxy server with command: $PROXY_CMD" PROXY_PORT=8000 PROXY_CMD="python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ll disaggregation failed kv transfer with NiXL connector using LIBFABRIC backend with vllm 0.11 and nixl 0.6.1 bug ### Your current environment ### 🐛 Describe the bug Disaggregated prefill produced garbage output with L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ducer echo "Starting prefill instances..." PREFILL_PORT=8100 CUDA_VISIBLE_DEVICES=0,1,2,3 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve $model_name \ --port $PREFILL_PORT \ --max-model-len 5000 \ --max-num-batched-tokens=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
