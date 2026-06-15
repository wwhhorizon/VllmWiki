# vllm-project/vllm#31626: [Bug][CPU Backend]: Gibberish output on CPU backend when --enforce-eager is enabled (Qwen3-0.6B)

| 字段 | 值 |
| --- | --- |
| Issue | [#31626](https://github.com/vllm-project/vllm/issues/31626) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CPU Backend]: Gibberish output on CPU backend when --enforce-eager is enabled (Qwen3-0.6B)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the CPU backend with the `Qwen/Qwen3-0.6B` model, enabling `--enforce-eager` causes the model to generate nonsensical tokens (repetitive strings like "ellaneous" and "arry"). However, without the `--enforce-eager` flag (using the default graph mode/compiled path), the model generates correct and coherent text. ## Reproduction Script To reproduce the issue, start the vLLM server with the CPU backend and eager mode enabled: `vllm serve "Qwen/Qwen3-0.6B" --enforce-eager` Then, run a simple generation request: `python3 examples/online_serving/token_generation_client.py` The output is gibberish: ``` {'request_id': '9a8a4c50ee0d5e5b', 'choices': [{'index': 0, 'logprobs': None, 'finish_reason': 'length', 'token_ids': [40142, 271, 23, 23, 40142, 40142, 271, 16, 16, 16, 11433, 271, 11433, 11433, 198, 198, 11433, 198, 11433, 198, 11433, 11433, 198, 11433]}], 'prompt_logprobs': None, 'kv_transfer_params': None} -------------------------------------------------- Token generation results: ellaneous 88ellaneousellaneous 111arry arryarry arry arry arryarry arry -------------------------------------------------- ``` Without `--enforce...

## 现有链接修复摘要

#31643 [Bugfix][CPU] Fix RotaryEmbedding fallback causing gibberish with --enforce-eager

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: owever, without the `--enforce-eager` flag (using the default graph mode/compiled path), the model generates correct and coherent text. ## Reproduction Script To reproduce the issue, start the vLLM server with the CPU b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][CPU Backend]: Gibberish output on CPU backend when --enforce-eager is enabled (Qwen3-0.6B) bug;cpu ### Your current environment ### 🐛 Describe the bug When using the CPU backend with the `Qwen/Qwen3-0.6B` model, e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ckend]: Gibberish output on CPU backend when --enforce-eager is enabled (Qwen3-0.6B) bug;cpu ### Your current environment ### 🐛 Describe the bug When using the CPU backend with the `Qwen/Qwen3-0.6B` model, enabling `--e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: serve "Qwen/Qwen3-0.6B" --enforce-eager` Then, run a simple generation request: `python3 examples/online_serving/token_generation_client.py` The output is gibberish: ``` {'request_id': '9a8a4c50ee0d5e5b', 'choices': [{'...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31643](https://github.com/vllm-project/vllm/pull/31643) | closes_keyword | 0.95 | [Bugfix][CPU] Fix RotaryEmbedding fallback causing gibberish with --enforce-eager | resolve #31626 When running vLLM on the CPU backend with `--enforce-eager`, models may produce incoherent or repetitive outputs. This happens because `enforce_eager=True` sets |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
