# vllm-project/vllm#10531: [Bug]: Authorization ignored when root_path is set

| 字段 | 值 |
| --- | --- |
| Issue | [#10531](https://github.com/vllm-project/vllm/issues/10531) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Authorization ignored when root_path is set

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running vllm behind a route based proxy (traefik) and noticed that I could use the API without any token. The problem seems to be because the API is still available on the default path `/v1/....` and not just on `/root_path/v1/....` but the key is only verified for `root_path/v1/...`. I was stripping the prefix, so I was hitting the `/v1/...` endpoint but needed to set the root path to be able to fetch the OpenAPI schema for swagger. I was running the `vllm/vllm-openai:v0.6.4` image Here is a minimal example that reproduces the bug: ```yaml services: vllm: image: vllm/vllm-openai:v0.6.4 ports: - 8000:8000 environment: VLLM_API_KEY: ${VLLM_API_KEY:-secret-key} volumes: - $HOME/.cache/huggingface:/root/.cache/huggingface networks: - internal command: - "--model=meta-llama/Llama-3.1-70B-Instruct" - "--tensor-parallel-size=2" - "--gpu-memory-utilization=0.95" - "--disable_log_requests" - "--root-path=/llm" restart: always ipc: host deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] ``` Then the following request still works without authentication error `...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n ignored when root_path is set bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running vllm behind a route based proxy (traefik) and noticed that I could use the API wi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing the `vllm/vllm-openai:v0.6.4` image Here is a minimal example that reproduces the bug: ```yaml services: vllm: image: vllm/vllm-openai:v0.6.4 ports: - 8000:8000 environment: VLLM_API_KEY: ${VLLM_API_KEY:-secret-key}...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l-size=2" - "--gpu-memory-utilization=0.95" - "--disable_log_requests" - "--root-path=/llm" restart: always ipc: host deploy: resources: reservations: devices: - driver: nvidia count: all capabilitie
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
