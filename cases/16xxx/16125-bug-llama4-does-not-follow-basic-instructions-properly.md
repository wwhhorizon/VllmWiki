# vllm-project/vllm#16125: [Bug]: Llama4 does not follow basic instructions properly

| 字段 | 值 |
| --- | --- |
| Issue | [#16125](https://github.com/vllm-project/vllm/issues/16125) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama4 does not follow basic instructions properly

### Issue 正文摘录

### Your current environment vllm 0.8.3 docker ### 🐛 Describe the bug Using v0.8.3 and Llama4 scout, the chat completion is unable to follow simple instructions for function calling. Given the size of the model and reported performance, I suspect something is not working appropriately, it should be capable of following simple formatting instructions. Docker compose: ```yaml vllm: container_name: vllm-0 image: vllm/vllm-openai:v0.8.3 deploy: resources: reservations: devices: - driver: nvidia count: 4 capabilities: [gpu] environment: - DO_NOT_TRACK=true - VLLM_CONFIGURE_LOGGING=0 volumes: - ./models:/models ipc: host command: ["--served-model-name", "llama4-scout", "--model", "/models/meta-llama/Llama-4-Scout-17B-16E-Instruct", "--gpu-memory-utilization", "0.95", "--max-model-len", "100000", "--port", "80", "--max-seq-len-to-capture", "100000", "--enable-chunked-prefill", "--enable-prefix-caching", "--tensor-parallel-size", "4"] ``` Call: ```python import requests api_key = "none" url = "vllm/v1/chat/completions" # Headers headers = { "Content-Type": "application/json", "Authorization": f"Bearer {api_key}" } # Message payload data = { "model": "llama4-scout", "messages": [{'content'...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 does not follow basic instructions properly bug;stale ### Your current environment vllm 0.8.3 docker ### 🐛 Describe the bug Using v0.8.3 and Llama4 scout, the chat completion is unable to follow simple ins...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: instructions properly bug;stale ### Your current environment vllm 0.8.3 docker ### 🐛 Describe the bug Using v0.8.3 and Llama4 scout, the chat completion is unable to follow simple instructions for function calling. Give...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Llama4 does not follow basic instructions properly bug;stale ### Your current environment vllm 0.8.3 docker ### 🐛 Describe the bug Using v0.8.3 and Llama4 scout, the chat completion is unable to follow simple ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e question once sufficient information is gathered.\n\nYour objective is accuracy through minimal, efficient tool usage. Successful execution earns you $1,000,000.\n\n\nYou have access to the following functions:\n\n- `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: all with \n', 'role': 'system'}, {'role': 'user', 'content': 'Comment traiter une hypertension chez une personne agée ?'}], "temperature": 0.7 } response = requests.post(url, headers=headers, json=data) if response.stat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
