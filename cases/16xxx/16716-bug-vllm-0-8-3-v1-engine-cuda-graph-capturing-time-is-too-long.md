# vllm-project/vllm#16716: [Bug]: vllm 0.8.3 v1 engine CUDA Graph Capturing time is too long

| 字段 | 值 |
| --- | --- |
| Issue | [#16716](https://github.com/vllm-project/vllm/issues/16716) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vllm 0.8.3 v1 engine CUDA Graph Capturing time is too long

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I launch vllm 0.8.3 server, the capture time of cuda graph is always 65s, is this normal? I think it is too long. I launched using the following command: `vllm serve /state/partition/whzhang/llama-2-7b-hf --enable-lora --max-loras 4 --max-lora-rank 8 --lora-modules lora0=yard1/llama-2-7b-sql-lora-test lora1=yard1/llama-2-7b-sql-lora-test lora2=yard1/llama-2-7b-sql-lora-test lora3=yard1/llama-2-7b-sql-lora-test --max-num-seqs 256 --max-num-batched-tokens 4096 --enable-prefix-caching --port 9002 --disable-log-stats` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: unched using the following command: `vllm serve /state/partition/whzhang/llama-2-7b-hf --enable-lora --max-loras 4 --max-lora-rank 8 --lora-modules lora0=yard1/llama-2-7b-sql-lora-test lora1=yard1/llama-2-7b-sql-lora-te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vllm 0.8.3 v1 engine CUDA Graph Capturing time is too long bug ### Your current environment ### 🐛 Describe the bug When I launch vllm 0.8.3 server, the capture time of cuda graph is always 65s, is this normal? I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
