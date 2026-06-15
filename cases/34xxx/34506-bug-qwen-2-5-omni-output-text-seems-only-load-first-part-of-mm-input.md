# vllm-project/vllm#34506: [Bug]: Qwen 2.5 Omni Output text seems only load first part of mm input

| 字段 | 值 |
| --- | --- |
| Issue | [#34506](https://github.com/vllm-project/vllm/issues/34506) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 2.5 Omni Output text seems only load first part of mm input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running in vllm v 0.16.0, vllm/examples/offline_inference/qwen2_5_omni/only_thinker.py, the output is: ```text I'm not sure what's recited in the audio. The image shows a baby with glasses sitting on a bed, reading a book. It's funny because it's so cute and unexpected to see a baby reading a book, especially with glasses on. It gives off a really adorable and humorous vibe. What do you ``` The v0.15.0 is like: ```text The first part of the audio recites "Mary had a little lamb". The image shows a baby wearing glasses sitting on a bed reading a book.The video might be considered funny because it's so unexpected to see a baby with glasses reading a book. Babies usually don't wear glasses or read books like that. It's just really cute and different from what you'd normally expect.If you have any other thoughts about these things, feel free to share! ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: en2_5_omni/only_thinker.py, the output is: ```text I'm not sure what's recited in the audio. The image shows a baby with glasses sitting on a bed, reading a book. It's funny because it's so cute and unexpected to see a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen 2.5 Omni Output text seems only load first part of mm input bug ### Your current environment ### 🐛 Describe the bug When running in vllm v 0.16.0, vllm/examples/offline_inference/qwen2_5_omni/only_thinker.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependen...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
