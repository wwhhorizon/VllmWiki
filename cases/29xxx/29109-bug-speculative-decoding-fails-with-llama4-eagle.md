# vllm-project/vllm#29109: [Bug]: Speculative decoding fails with Llama4-eagle

| 字段 | 值 |
| --- | --- |
| Issue | [#29109](https://github.com/vllm-project/vllm/issues/29109) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Speculative decoding fails with Llama4-eagle

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run cmd: `VLLM_USE_V1=1 python examples/offline_inference/spec_decode.py --num_spec_tokens 7 --num_prompts 1 --method eagle --model_dir meta-llama/Llama-4-Scout-17B-16E-Instruct --eagle_dir morgendave/EAGLE-Llama-4-Scout-17B-16E-Instruct --tp 4 2>&1 | tee logs_specdecode_llama4.txt` Error: `AttributeError: 'EagleLlama4ForCausalLM' object has no attribute 'lm_head' ` Full error logs attached below [logs_specdecode_llama4.txt](https://github.com/user-attachments/files/23661358/logs_specdecode_llama4.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Speculative decoding fails with Llama4-eagle bug ### Your current environment ### 🐛 Describe the bug Run cmd: `VLLM_USE_V1=1 python examples/offline_inference/spec_decode.py --num_spec_tokens 7 --num_prompts 1 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative decoding fails with Llama4-eagle bug ### Your current environment ### 🐛 Describe the bug Run cmd: `VLLM_USE_V1=1 python examples/offline_inference/spec_decode.py --num_spec_tokens 7 --num_prompts 1 --
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
