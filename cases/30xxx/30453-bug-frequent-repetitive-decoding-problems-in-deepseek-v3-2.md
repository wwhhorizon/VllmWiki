# vllm-project/vllm#30453: [Bug]: Frequent Repetitive Decoding Problems in DeepSeek-V3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#30453](https://github.com/vllm-project/vllm/issues/30453) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Frequent Repetitive Decoding Problems in DeepSeek-V3.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My launch command is ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --tensor-parallel-size 8 --served-model-name deepseek_v3_2 --tokenizer-mode deepseek_v32 --reasoning-parser deepseek_v3 --max-num-seqs 1024 --trust-remote-code --max-model-len 131072 ``` During the testing of the CNN/Daily Mail dataset, there are many cases of repetitive decoding. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cribe the bug My launch command is ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --tensor-parallel-size 8 --served-model-name deepseek_v3_2 --tokenizer-mode deepseek_v32 --reasoning-parser deepseek_v3 --max-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nment ### 🐛 Describe the bug My launch command is ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --tensor-parallel-size 8 --served-model-name deepseek_v3_2 --tokenizer-mode deepseek_v32 --reasoning-parser dee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
