# vllm-project/vllm#32822: [Bug]: When the temperature is set to 0 in qwen3-235B-A22B-Instruct-2507, there is still randomness.

| 字段 | 值 |
| --- | --- |
| Issue | [#32822](https://github.com/vllm-project/vllm/issues/32822) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When the temperature is set to 0 in qwen3-235B-A22B-Instruct-2507, there is still randomness.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the temperature is set to 0 in qwen3-235b, there is still randomness. The startup command for vllm is as follows: python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen3/model/Qwen3-235B-A22B-Instruct-2507 --served-model-name qwen3-moe-235b --gpu-memory-utilization=0.9 -tp 8 --enable-auto-tool-choice --tool-call-parser hermes --enable-log-requests The curl command is as follows: curl --location --request POST 'http://10.17.61.32:38080/Qwen3-moe-235b/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "qwen3-moe-235b", "temperature": 0, "top_p": 1, "seed": 42, "use_beam_search": false, "top_k": -1, "logprobs": true, "top_logprobs": 4, "stream":true, "messages": [ { "role": "user", "content": "Answer the following multiple choice question. The last line of your response should be of the following format: \"ANSWER: $LETTER\" (without quotes) where LETTER is one of ABCD. Think step by step before answering.\n\nYou want to create a mouse embryonic chimera with induced pluripotent stem cells from somatic cells of various tissues. You are interested in the iPSCs fate in the embryo a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s. The iPSC cells are labeled with a mRaspberry fused under a lineage-specific promoter for each cell type. You inject the dedifferentiated cells into the 32-cell stage blastocyst and track them over 48. Every 12 h, you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: moe-235b", "temperature": 0, "top_p": 1, "seed": 42, "use_beam_search": false, "top_k": -1, "logprobs": true, "top_logprobs": 4, "stream":true, "messages": [ { "role": "user", "content": "Answer the following multiple c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: When the temperature is set to 0 in qwen3-235B-A22B-Instruct-2507, there is still randomness. bug ### Your current environment ### 🐛 Describe the bug When the temperature is set to 0 in qwen3-235b, there is still...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -tp 8 --enable-auto-tool-choice --tool-call-parser hermes --enable-log-requests The curl command is as follows: curl --location --request POST 'http://10.17.61.32:38080/Qwen3-moe-235b/chat/completions' \ --header 'Conte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
