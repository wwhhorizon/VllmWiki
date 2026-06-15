# vllm-project/vllm#12052: [Bug]: PaliGemma2 not working with OpenAI Docker serve

| 字段 | 值 |
| --- | --- |
| Issue | [#12052](https://github.com/vllm-project/vllm/issues/12052) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PaliGemma2 not working with OpenAI Docker serve

### Issue 正文摘录

### Your current environment Just using Docker image 0.6.6post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Just try to run https://huggingface.co/google/paligemma2-3b-pt-896 using Docker vllm image. My docker compose follows: ``` services: app: image: vllm/vllm-openai:latest runtime: nvidia restart: unless-stopped ports: - "8000:8000" volumes: - ./cache:/root/.cache/huggingface environment: - HUGGING_FACE_HUB_TOKEN=hf_ ipc: host command: - --host - 0.0.0.0 - --model - google/paligemma2-3b-pt-896 - --limit-mm-per-prompt - 'image=1' - --trust-remote-code - --max-model-len - "8192" ``` It does NOT work, the issue is the same reported in the pull request here: https://github.com/vllm-project/vllm/pull/11142#issuecomment-2541342321 and is: `ValueError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: PaliGemma2 not working with OpenAI Docker serve bug;stale ### Your current environment Just using Docker image 0.6.6post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Just try to run https://hugging...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: PaliGemma2 not working with OpenAI Docker serve bug;stale ### Your current environment Just using Docker image 0.6.6post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Just try to run https://hugging...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: PaliGemma2 not working with OpenAI Docker serve bug;stale ### Your current environment Just using Docker image 0.6.6post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Just try to run https://hugging...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: PaliGemma2 not working with OpenAI Docker serve bug;stale ### Your current environment Just using Docker image 0.6.6post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Just try to run https://hugging...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
