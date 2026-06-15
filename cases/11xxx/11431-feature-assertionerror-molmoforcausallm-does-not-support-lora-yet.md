# vllm-project/vllm#11431: [Feature]: AssertionError: MolmoForCausalLM does not support LoRA yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#11431](https://github.com/vllm-project/vllm/issues/11431) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: AssertionError: MolmoForCausalLM does not support LoRA yet.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Apparently MolmoForCasualLM does not yet support Lora adapters, yielding an AssertionError on serving: `AssertionError: MolmoForCausalLM does not support LoRA yet.` I trained a Lora adapter with HF Trainer and would like to use it together with vLLM for fast inference. This seems not implemented yet. I tested this by trying to serve Molmo directly via: `vllm serve allenai/Molmo-7B-D-0924 --enable-lora --trust-remote-code --max-num-seqs 6 --tensor-parallel-size 1 --lora-modules test=$LORA_DIR/checkpoint-25` Are there any plans to get this working or is there a guide somewhere how i can enable lora for Molmo myself? If all works I'd be open to submit a PR but i'd need some guidance. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t support LoRA yet. feature request ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Apparently MolmoForCasualLM does not yet support Lora adapters, yielding an AssertionError on s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: AssertionError: MolmoForCausalLM does not support LoRA yet. feature request ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Apparently MolmoForCasualLM does not yet support L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
