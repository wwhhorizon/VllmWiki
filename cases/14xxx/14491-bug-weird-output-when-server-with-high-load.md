# vllm-project/vllm#14491: [Bug]: Weird output when server with high load

| 字段 | 值 |
| --- | --- |
| Issue | [#14491](https://github.com/vllm-project/vllm/issues/14491) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Weird output when server with high load

### Issue 正文摘录

### Your current environment I'm using a docker compose to manage the openai server, i'll collect the env next week. The startup command: ``` vllm-openai: command: --model /model -tp 2 --served-model-name Qwen2.5-72B-Instruct --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.85 --enable-chunked-prefill --max-num-seqs 128 --enable-prefix-caching --override-generation-config {\"max_new_tokens\":8192} --generation-config auto -q gptq --max-long-partial-prefills=4 ``` ### 🐛 Describe the bug After update to v0.7.3, server generate wrong data in high load. During a high load, 100% cache and over 500 waiting requests, all the request generate grabage data, like this image. After the high load, the results keep grabage. ![Image](https://github.com/user-attachments/assets/571252f8-c455-4587-946e-91b86f71acf4) Here's a grafana dashboard during the high load. ![Image](https://github.com/user-attachments/assets/5a405131-5413-4d31-be4e-d860f303f827) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Weird output when server with high load bug;stale ### Your current environment I'm using a docker compose to manage the openai server, i'll collect the env next week. The startup command: ``` vllm-openai: command...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er with high load bug;stale ### Your current environment I'm using a docker compose to manage the openai server, i'll collect the env next week. The startup command: ``` vllm-openai: command: --model /model -tp 2 --serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e env next week. The startup command: ``` vllm-openai: command: --model /model -tp 2 --served-model-name Qwen2.5-72B-Instruct --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.85 --enable-ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 27) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
