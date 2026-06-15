# vllm-project/vllm#9193: [Bug]: 500 Internal Server Error when calling v1/completions and v1/chat/completions with vllm/vllm-openai:v0.6.2 on K8s

| 字段 | 值 |
| --- | --- |
| Issue | [#9193](https://github.com/vllm-project/vllm/issues/9193) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 500 Internal Server Error when calling v1/completions and v1/chat/completions with vllm/vllm-openai:v0.6.2 on K8s

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting "500 Internal Server Error" while calling `v1/completions` and `v1/chat/completions` endpoints when deployed on Kubernetes. Remaining endpoints sych as `tokenize` and `v1/models` are working as expected. Followed the deployment guide provided [here](https://github.com/vllm-project/vllm/blob/main/docs/source/serving/deploying_with_k8s.rst). ``` INFO: Started server process [7] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) DEBUG 10-09 05:19:37 client.py:148] Heartbeat successful. INFO: 10.121.X.X:33112 - "GET /health HTTP/1.1" 200 OK INFO: 10.121.X.X:33122 - "GET /v1/models HTTP/1.1" 200 OK INFO 10-09 05:19:37 logger.py:36] Received request tokn-788eaaca463f4228a9458b94a97bb373: prompt: 'Sample sentence for API testing', params: None, prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. INFO: 10.121.X.X:33124 - "POST /tokenize HTTP/1.1" 200 OK INFO: 10.121.X.X:33134 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error INFO: 10.121.X.X:33142 - "POST /v1/chat/completi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: h vllm/vllm-openai:v0.6.2 on K8s bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting "500 Internal Server Error" while calling `v1/completions` and `v1/chat/completions` e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: at successful. ``` Here is the yml used to create the deployment: ``` apiVersion: apps/v1 kind: Deployment metadata: labels: app: vllm-app name: vllm-deployment namespace: vllm spec: replicas: 1 selector: matchLabels: a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ying_with_k8s.rst). ``` INFO: Started server process [7] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) DEBUG 10-09 05:19:3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "-c"] args: ["vllm serve neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --trust-remote-code --enable-chunked-prefill --max-model-len 16384 --disable-log-stats"] image: vllm/vllm-openai:v0.6.2 env: - name: HF_HOME value: /ho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
