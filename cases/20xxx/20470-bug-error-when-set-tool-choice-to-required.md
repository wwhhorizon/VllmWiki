# vllm-project/vllm#20470: [Bug]: error when set tool_choice to "required"

| 字段 | 值 |
| --- | --- |
| Issue | [#20470](https://github.com/vllm-project/vllm/issues/20470) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error when set tool_choice to "required"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve "Qwen3-14B-AWQ" \ --enable-auto-tool-choice \ --enable-reasoning \ --reasoning-parser qwen3 \ --guided-decoding-backend xgrammar \ --tool-call-parser hermes \ --gpu-memory-utilization 0.8 \ --max-model-len 15000 \ when set tool_choice={"type": "function", "function": {"name": "UpdateTasks"}}, returns the corrent response. But if set tool_choice="required", it returns error ![Image](https://github.com/user-attachments/assets/af56e51b-97d8-49e4-bed7-7d31202a8fd1) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --enable-reasoning \ --reasoning-parser qwen3 \ --guided-decoding-backend xgrammar \ --tool-call-parser hermes \ --gpu-memory-utilization 0.8 \ --max-model-len 15000 \ when set tool_choice={"type": "function", "function...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d1) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g ### Your current environment ### 🐛 Describe the bug vllm serve "Qwen3-14B-AWQ" \ --enable-auto-tool-choice \ --enable-reasoning \ --reasoning-parser qwen3 \ --guided-decoding-backend xgrammar \ --tool-call-parser herm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
