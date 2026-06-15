# vllm-project/vllm#11097: [Bug]: `mistral_tool_parser` Fails to Parse Parallel Function Calls

| 字段 | 值 |
| --- | --- |
| Issue | [#11097](https://github.com/vllm-project/vllm/issues/11097) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `mistral_tool_parser` Fails to Parse Parallel Function Calls

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` { "content": "[TOOL_CALLS] [{\"arguments\": {\"video_path\": \"/home/Desktop/vids/donald_fernando.mp4\", \"script\": \"Donald Drewski and Fernando Whitehall are having a conversation.\", \"base_img\": \"/home/stable_diffusion_output.jpg\", \"mp3_path\": \"\"}, \"name\": \"create_ai_video\", \"id\": \"fgGIFgbG4\"}]\n\n[TOOL_CALLS] [{\"arguments\": {\"content\": \"Donald Drewski and Fernando Whitehall are having a conversation.\", \"image_path\": \"/home/stable_diffusion_output.jpg\", \"video_path\": \"/home/Desktop/vids/donald_fernando.mp4\"}, \"name\": \"post_on_x\", \"id\": \"fgGIFgbG4\"}]", "source": "generate", "role": "assistant" } ``` ### 🐛 Describe the bug When deploying ministral-8b for tool calling tasks using the following command (`vllm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer-mode mistral --enable-auto-tool-choice --tool-call-parser mistral`), I encountered intermittent JSON decode errors during execution. ![image](https://github.com/user-attachments/assets/8e3726a5-4a21-4d46-81b0-299e9d0db5a2) Upon investigation, I found that these errors primarily occur when the model generates parallel function call...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: `mistral_tool_parser` Fails to Parse Parallel Function Calls bug;stale ### Your current environment ### Model Input Dumps ``` { "content": "[TOOL_CALLS] [{\"arguments\": {\"video_path\": \"/home/Desktop/vids/dona...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ts. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e Parallel Function Calls bug;stale ### Your current environment ### Model Input Dumps ``` { "content": "[TOOL_CALLS] [{\"arguments\": {\"video_path\": \"/home/Desktop/vids/donald_fernando.mp4\", \"script\": \"Donald Dr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
