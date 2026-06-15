# vllm-project/vllm#15294: [Bug]: Critical Memory Leak in vLLM V1 Engine: 200+ GB RAM Usage from Image Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#15294](https://github.com/vllm-project/vllm/issues/15294) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Critical Memory Leak in vLLM V1 Engine: 200+ GB RAM Usage from Image Inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are using vLLM in production and yesterday upgraded to version 0.8.1. After switching to the new V1 engine, we observed a significant RAM memory leak during image inference requests, even though the model runs on the GPU. In our production environment, RAM usage ballooned to over 200 GB. Upon further investigation, we reproduced the issue using a minimal example (provided below). With V1 engine, each image inference request increases system memory usage, whereas V0 engine does not have this issue. **Summary:** 1. Issue only occurs in V1 engine. 2. Memory leak is tied to image inference requests. 3. Behavior is not present in V0. We’d greatly appreciate it if you could investigate and let us know if you need any additional information. We’re happy to assist in resolving this important issue as soon as possible. vLLM serve command (using V1): ```bash vllm serve mistralai/Pixtral-12B-2409 --tokenizer_mode mistral --limit_mm_per_prompt 'image=4' --disable-mm-preprocessor-cache ``` Initial memory usage (3209 MB): ![Image](https://github.com/user-attachments/assets/dc0a6a37-30c4-46e0-a067-24517a6bd1b7) Run image inference 100 times:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cribe the bug We are using vLLM in production and yesterday upgraded to version 0.8.1. After switching to the new V1 engine, we observed a significant RAM memory leak during image inference requests, even though the mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ificant RAM memory leak during image inference requests, even though the model runs on the GPU. In our production environment, RAM usage ballooned to over 200 GB. Upon further investigation, we reproduced the issue usin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d2) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine, we observed a significant RAM memory leak during image inference requests, even though the model runs on the GPU. In our production environment, RAM usage ballooned to over 200 GB. Upon further investigation, we...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
