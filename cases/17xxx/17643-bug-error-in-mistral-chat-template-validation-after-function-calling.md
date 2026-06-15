# vllm-project/vllm#17643: [Bug]: Error in Mistral chat template validation after function calling

| 字段 | 值 |
| --- | --- |
| Issue | [#17643](https://github.com/vllm-project/vllm/issues/17643) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | gemm |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error in Mistral chat template validation after function calling

### Issue 正文摘录

### Your current environment ## Description When using Mistral-Small-3.1-24B-Instruct-2503 with function calling (tools), the vLLM server crashes after a function/tool call completes and the assistant is expected to continue the conversation. ## Environment - Model: Mistral-Small-3.1-24B-Instruct-2503 - Chat template: tool_chat_template_mistral3.jinja - Running via Docker ## Docker Command I'm running vLLM with the following Docker command: ```bash docker run --rm --runtime nvidia --gpus all \ --name Mistral-Small-3.1-24B-Instruct-2503 \ -v ~/project/vllm/models/Mistral-Small-3.1-24B-Instruct-2503:/Mistral-Small-3.1-24B-Instruct-2503 \ -v ~/project/vllm/examples:/app/examples \ -p 80:8000 \ --env "TRANSFORMERS_OFFLINE=1" \ --env "HF_DATASET_OFFLINE=1" \ --env "PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True" \ --ipc=host \ vllm/vllm-openai:v0.8.5.post1 \ --model="/Mistral-Small-3.1-24B-Instruct-2503" \ --disable-mm-preprocessor-cache \ --disable-chunked-mm-input \ --limit-mm-per-prompt image=0 \ --max-model-len 8192 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --chat-template /app/examples/tool_chat_template_mistral3.jinja ``` ### 🐛 Describe the bug ## Reproduction...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ct-2503 - Chat template: tool_chat_template_mistral3.jinja - Running via Docker ## Docker Command I'm running vLLM with the following Docker command: ```bash docker run --rm --runtime nvidia --gpus all \ --name Mistral-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ling bug ### Your current environment ## Description When using Mistral-Small-3.1-24B-Instruct-2503 with function calling (tools), the vLLM server crashes after a function/tool call completes and the assistant is expect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he assistant is expected to continue the conversation. ## Environment - Model: Mistral-Small-3.1-24B-Instruct-2503 - Chat template: tool_chat_template_mistral3.jinja - Running via Docker ## Docker Command I'm running vL...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: quently asked questions. development ci_build;frontend_api;model_support gemm crash Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l calling enabled (see Docker command above). 2. Send a chat/completions request with a function call. 3. Wait for the tool call to complete. 4. Let the assistant try to respond. 5. Observe the crash. ## Error Message:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
