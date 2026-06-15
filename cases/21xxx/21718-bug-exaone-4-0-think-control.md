# vllm-project/vllm#21718: [Bug] Exaone 4.0 – “think” control

| 字段 | 值 |
| --- | --- |
| Issue | [#21718](https://github.com/vllm-project/vllm/issues/21718) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug] Exaone 4.0 – “think” control

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am reporting an issue because the desired “think” behavior cannot be triggered when using the Exaone 4.0 model in PR https://github.com/vllm-project/vllm/pull/21060. As @blakkd pointed out in the comment https://github.com/vllm-project/vllm/pull/21060#issuecomment-3119957596, even after modifying the Jinja template described in the PR, I confirmed that think-mode is still not executed. 1. Using the default template ```bash #!/bin/bash source .venv/bin/activate pip list | grep vllm wget -qO - https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B/resolve/main/chat_template.jinja > chat_template.jinja vllm serve \ LGAI-EXAONE/EXAONE-4.0-32B \ --tensor-parallel-size 2 \ --chat-template chat_template.jinja 1>/dev/null 2>&1 & VLLM_PID=$! export OPENAI_API_KEY="EMPTY" until curl -sf -o /dev/null http://localhost:8000/health ; do echo "Waiting for vLLM server to be ready..." sleep 5 done echo "vLLM server is ready." curl -X POST http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "LGAI-EXAONE/EXAONE-4.0-32B", "messages": [{"role": "user", "content": "What is the capital of France?"}], "max_token...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: istant","content":"The capital of France is **Paris**. It is the largest city in France and a major global center for art, fashion, gastronomy, and culture. Paris is also home to iconic landmarks such as the **Eiffel To...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: " until curl -sf -o /dev/null http://localhost:8000/health ; do echo "Waiting for vLLM server to be ready..." sleep 5 done echo "vLLM server is ready." curl -X POST http://localhost:8000/v1/chat/completions \ -H "Conten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 835 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e desired “think” behavior cannot be triggered when using the Exaone 4.0 model in PR https://github.com/vllm-project/vllm/pull/21060. As @blakkd pointed out in the comment https://github.com/vllm-project/vllm/pull/21060...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
