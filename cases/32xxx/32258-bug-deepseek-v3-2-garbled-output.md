# vllm-project/vllm#32258: [Bug]: DeepSeek v3.2 garbled output

| 字段 | 值 |
| --- | --- |
| Issue | [#32258](https://github.com/vllm-project/vllm/issues/32258) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek v3.2 garbled output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Recipe: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html Serving: ``` python -m vllm.entrypoints.openai.api_server \ --model /mnt/local/models/deepseek-ai/DeepSeek-V3.2 \ --tensor-parallel-size 4 \ --enforce-eager \ --no-enable-prefix-caching \ --max-model-len 4096 \ --tokenizer-mode deepseek_v32 \ --served_model_name ds32 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --max-num-seqs 1 \ --reasoning-parser deepseek_v3 ``` Request: ``` curl -X 'POST' \ 'http://127.0.0.1:8000/v1/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "prompt": "hello", "model": "ds32" }' ``` Response: ``` { "id": "cmpl-a8a271d26c770c79", "object": "text_completion", "created": 1768306542, "model": "ds32", "choices": [ { "index": 0, "text": "{$domain}\"\n );\n }\n\n /**\n * @param $provider\n", "logprobs": null, "finish_reason": "length", "stop_reason": null, "token_ids": null, "prompt_logprobs": null, "prompt_token_ids": null } ], "service_tier": null, "system_fingerprint": null, "usage": { "prompt_tokens": 1, "total_tokens": 17, "completion_tokens": 16, "prompt_tokens_d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed output bug ### Your current environment ### 🐛 Describe the bug Recipe: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html Serving: ``` python -m vllm.entrypoints.openai.api_server \ --model /...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uto-tool-choice \ --max-num-seqs 1 \ --reasoning-parser deepseek_v3 ``` Request: ``` curl -X 'POST' \ 'http://127.0.0.1:8000/v1/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: culative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
