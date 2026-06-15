# vllm-project/vllm#14845: [Bug]: TTFT Performance Regression in vLLM v0.7.0 Compared to v0.6.1.post2

| 字段 | 值 |
| --- | --- |
| Issue | [#14845](https://github.com/vllm-project/vllm/issues/14845) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TTFT Performance Regression in vLLM v0.7.0 Compared to v0.6.1.post2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Summary** After upgrading from vLLM 0.6.1.post2 to vLLM 0.7.0, we observed a significant increase in TTFT. While e2e latency and throughput improved in v0.7.0, TTFT became 3x slower. We use: - Our own model. The base model is Llama3 8B - QPS: 1.2 - TTFT (v0.7.0): 0.39s - TTFT (v0.6.1.post2): 0.13s - Input Prompt: 4K tokens - Output Tokens: 100 **Reproduction Steps** 1. Get TTFT on v0.7.0 - Run vLLM server ``` vllm serve /export/content/data/tmp/custom_model_path/proxima/model_resources \ --tokenizer /export/content/data/tmp/custom_model_path/proxima/tokenizer_resources \ --tensor-parallel-size 1 \ --max-num-batched-tokens 2048 \ --gpu-memory-utilization 0.9 \ --enable-chunked-prefill \ --use-v2-block-manager \ --trust-remote-code \ --guided-decoding-backend outlines ``` - Send requests to vLLM backend ``` python benchmark_serving.py --backend vllm --model (our model) --request-rate 1.2 --save-result ``` 2. Get TTFT on v0.6.1.post2 - Run vLLM server ``` vllm serve /export/content/data/tmp/custom_model_path/proxima/model_resources \ --tokenizer /export/content/data/tmp/custom_model_path/proxima/tokenizer_resources \ --tensor-para...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: TTFT Performance Regression in vLLM v0.7.0 Compared to v0.6.1.post2 bug;stale ### Your current environment ### 🐛 Describe the bug **Summary** After upgrading from vLLM 0.6.1.post2 to vLLM 0.7.0, we observed a sig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: TTFT Performance Regression in vLLM v0.7.0 Compared to v0.6.1.post2 bug;stale ### Your current environment ### 🐛 Describe the bug **Summary** After upgrading from vLLM 0.6.1.post2 to vLLM 0.7.0, we observed a significan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory cuda;operator;sampling;triton build_err...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --use-v2-block-manager \ --trust-remote-code \ --guided-decoding-backend outlines ``` - Send requests to vLLM backend ``` python benchmark_serving.py --backend vllm --model (our model) --request-rate 1.2 --save-result `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lts ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
