# vllm-project/vllm#19222: [Bug]: reasoning-parser=deepseek_r1 wrong output with enable_thinking=False

| 字段 | 值 |
| --- | --- |
| Issue | [#19222](https://github.com/vllm-project/vllm/issues/19222) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | sampling |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: reasoning-parser=deepseek_r1 wrong output with enable_thinking=False

### Issue 正文摘录

### Your current environment Standard vllm Docker Container 0.9.0.1 with setup ``` services: vllm-qwen3-32b: image: vllm/vllm-openai:v0.9.0.1 container_name: vllm-qwen3-32b environment: - HF_TOKEN=$HF_TOKEN - VLLM_NO_USAGE_STATS=1 ipc: host deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1'] capabilities: [ gpu ] network_mode: host volumes: - /mnt/sda/huggingface:/root/.cache/huggingface - .:/opt/vllm command: - --port=8000 - --disable-log-requests - --model=Qwen/Qwen3-32B - --tensor-parallel-size=2 - --gpu-memory-utilization=0.90 - --swap-space=5 - --reasoning-parser=deepseek_r1 restart: unless-stopped ``` ### 🐛 Describe the bug In a chatbot we can dynamically decide for Qwen3, if reasoning / thinking is necessary or not. We set "chat_template_kwargs": {"enable_thinking": false}, if we want to deactivate reasoning in request (we don't use nothink tag, it's not reliable) With enable_thinking=false and JSON guided sampling, the message.content is empty and the content goes misformatted into message.reasoning_content. Example: ```bash $ curl http://ai1.dev.init:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "Qwen/Qwen3-32B",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Standard vllm Docker Container 0.9.0.1 with setup ``` services: vllm-qwen3-32b: image: vllm/vllm-openai:v0.9.0.1 container_name: vllm-qwen3-32b environment: - HF_TOKEN=$HF_TOKEN - VLLM_NO_USAGE_STATS=1 ipc: host deploy:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ble_thinking=False bug;stale ### Your current environment Standard vllm Docker Container 0.9.0.1 with setup ``` services: vllm-qwen3-32b: image: vllm/vllm-openai:v0.9.0.1 container_name: vllm-qwen3-32b environment: - HF...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: reasoning-parser=deepseek_r1 wrong output with enable_thinking=False bug;stale ### Your current environment Standard vllm Docker Container 0.9.0.1 with setup ``` services: vllm-qwen3-32b: image: vllm/vllm-openai:v0.9.0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: distributed_parallel;frontend_api;model_support;sampling_logits sampling mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
