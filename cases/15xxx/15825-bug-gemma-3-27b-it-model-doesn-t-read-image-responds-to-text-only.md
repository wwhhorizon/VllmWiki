# vllm-project/vllm#15825: [Bug]: Gemma 3 27B IT Model Doesn't Read Image (Responds To Text Only)

| 字段 | 值 |
| --- | --- |
| Issue | [#15825](https://github.com/vllm-project/vllm/issues/15825) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 3 27B IT Model Doesn't Read Image (Responds To Text Only)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma 3 27B IT model doesn't read image (responds to text only) I'm using V1 Output: ``` {'id': 'cmpl-aea585dd23754337929edcab4dcd23d4', 'object': 'text_completion', 'created': 1743435279, 'model': '/temp/local-ssd/models/gemma-3-27b-it/', 'choices': [{'index': 0, 'text': "Okay, I'm ready! Please provide me with the image you would like me to describe. I can analyze the image and tell you about:\n\n* **Objects:** What things are present in the image?\n* **Colors:** What are the dominant and notable colors?\n* **Composition:** How are the elements arranged? Is it a close-up, wide shot, etc.?\n* **People/Animals:** Are there any people or animals, and what are they doing?\n* **Overall Impression:** What is the general mood or feeling conveyed by the image?\n* **Details:** Any other interesting or noteworthy details.\n\nJust paste the image link or upload the image, and I'll do my best to provide a detailed and helpful description!\n", 'logprobs': None, 'finish_reason': 'stop', 'stop_reason': 106, 'prompt_logprobs': None}], 'usage': {'prompt_tokens': 23, 'total_tokens': 186, 'completion_tokens': 163, 'prompt_tokens_details': None}}...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: :** Any other interesting or noteworthy details.\n\nJust paste the image link or upload the image, and I'll do my best to provide a detailed and helpful description!\n", 'logprobs': None, 'finish_reason': 'stop', 'stop_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 3 27B IT Model Doesn't Read Image (Responds To Text Only) bug ### Your current environment ### 🐛 Describe the bug Gemma 3 27B IT model doesn't read image (responds to text only) I'm using V1 Output: ``` {'i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma 3 27B IT Model Doesn't Read Image (Responds To Text Only) bug ### Your current environment ### 🐛 Describe the bug Gemma 3 27B IT model doesn't read image (responds to text only) I'm using V1 Output: ``` {'i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
