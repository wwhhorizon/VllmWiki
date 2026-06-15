# vllm-project/vllm#22518: [Bug]: Fine-tuned DeepSeek-R1-Distill-Qwen-1.5B generates only exclamation marks (token 0) on Ascend NPU

| 字段 | 值 |
| --- | --- |
| Issue | [#22518](https://github.com/vllm-project/vllm/issues/22518) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fine-tuned DeepSeek-R1-Distill-Qwen-1.5B generates only exclamation marks (token 0) on Ascend NPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After fine-tuning DeepSeek-R1-Distill-Qwen-1.5B model using SFT, vLLM generates only exclamation marks (`!!!!!!!!!!...`) for all prompts on Ascend 910B NPU environment. The same model works correctly when using PyTorch as inference backend. ``` Actual Behavior Prompt: 'Hello, my name is' Generated: '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' --- Prompt: 'What is 2+2?' Generated: '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' --- Prompt: 'The capital of France is' Generated: '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' --- ``` The issue appears to be related to tokenizer handling or vocab mapping after fine-tuning, where vLLM might be incorrectly mapping all tokens to token ID 0 (which corresponds to exclamation mark !).The model was fine-tuned using standard SFT techniques,no custom tokenizer modifications were made during fine-tuning and issue is reproducible across different prompts and sampling parameters. ### Before submitting a new issue... - [x] Make sur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tokenizer modifications were made during fine-tuning and issue is reproducible across different prompts and sampling parameters. ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ironment. The same model works correctly when using PyTorch as inference backend. ``` Actual Behavior Prompt: 'Hello, my name is' Generated: '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;kernel;operator;quantization;sampling;triton build_error;import_error dtype;env_depen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Fine-tuned DeepSeek-R1-Distill-Qwen-1.5B generates only exclamation marks (token 0) on Ascend NPU bug ### Your current environment ### 🐛 Describe the bug After fine-tuning DeepSeek-R1-Distill-Qwen-1.5B model usin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
