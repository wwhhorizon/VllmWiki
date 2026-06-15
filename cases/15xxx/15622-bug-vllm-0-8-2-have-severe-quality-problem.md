# vllm-project/vllm#15622: [Bug]: vllm 0.8.2 have severe quality problem

| 字段 | 值 |
| --- | --- |
| Issue | [#15622](https://github.com/vllm-project/vllm/issues/15622) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.2 have severe quality problem

### Issue 正文摘录

### Your current environment I just downgraded vllm to 0.7.2, so pytorch is 2.5.1, but I'm sure that the environment when I was using 0.8.2 is fine. ### 🐛 Describe the bug the quality of model decreases incredibly, for example the model used to output well in 0.7.2 can't output correct LaTeX formulas at 0.8.2, besides it often stuck in a loop. I noticed this problem when using Qwen2.5-VL-32B AWQ, firstly I thought it was something about quantization but soon I found fp16 version also performs badly, and I tested Qwen2.5-VL-72B and I found it can't output correctly as used to be. so this is definitely a problem with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stly I thought it was something about quantization but soon I found fp16 version also performs badly, and I tested Qwen2.5-VL-72B and I found it can't output correctly as used to be. so this is definitely a problem with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: when using Qwen2.5-VL-32B AWQ, firstly I thought it was something about quantization but soon I found fp16 version also performs badly, and I tested Qwen2.5-VL-72B and I found it can't output correctly as used to be. so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: when I was using 0.8.2 is fine. ### 🐛 Describe the bug the quality of model decreases incredibly, for example the model used to output well in 0.7.2 can't output correct LaTeX formulas at 0.8.2, besides it often stuck i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
