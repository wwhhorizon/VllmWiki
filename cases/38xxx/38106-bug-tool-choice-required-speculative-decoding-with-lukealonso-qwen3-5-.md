# vllm-project/vllm#38106: [Bug]: tool_choice="required" + speculative decoding with lukealonso/Qwen3.5-397B-A17B-NVFP4 leads to failed tool calls.

| 字段 | 值 |
| --- | --- |
| Issue | [#38106](https://github.com/vllm-project/vllm/issues/38106) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tool_choice="required" + speculative decoding with lukealonso/Qwen3.5-397B-A17B-NVFP4 leads to failed tool calls.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, ## Setup I'm sending requests that want structured outputs, as such I set tool_choice="required" and have a tool that enforces the output structure. Example config, without prompts: Now what happens is that the speculative decoding model of qwen3.5 (haven't tested if quantization is partly to blame) is generating tool calls as xml instead of json. This leads to an error in https://github.com/vllm-project/vllm/blob/bcf2be96120005e9aea171927f85055a6a5c0cf6/vllm/entrypoints/openai/engine/serving.py#L1132 since it expects json, which gets suppressed, which leads to an empty tool call list, but with finish_reason="tool_calls" in https://github.com/vllm-project/vllm/blob/bcf2be96120005e9aea171927f85055a6a5c0cf6/vllm/entrypoints/openai/chat_completion/serving.py#L1445. I.e. an output like this (not from vllm, but from my client library, but you get the point): ### Secondary bug Imo finish_reason="tool_calls" without any tool called is another bug, but realistically one that can only happen if another bug is happening. You could put some check in the tool_choice="required" path, if there were actually any tool calls and if no, the...

## 现有链接修复摘要

#43691 [SpecDec + Reasoning] Fix race condition when <channel|> reasoning-end

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: arguments=json.dumps(tool_call.parameters, ensure_ascii=False), ) ) # content = None # Clear content since tool is called. if len(content) > 0 and len(tool_calls) == 0: print("Using alternative r
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oice="required" + speculative decoding with lukealonso/Qwen3.5-397B-A17B-NVFP4 leads to failed tool calls. bug ### Your current environment ### 🐛 Describe the bug Hello, ## Setup I'm sending requests that want structure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: tool_choice="required" + speculative decoding with lukealonso/Qwen3.5-397B-A17B-NVFP4 leads to failed tool calls. bug ### Your current environment ### 🐛 Describe the bug Hello, ## Setup I'm sending requests that...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ly generate json as tool calls 2. I also added the tool call parser as a fallback for tool_choice="required" and it worked, i.e. this patch at https://github.com/vllm-project/vllm/blob/bcf2be96120005e9aea171927f85055a6a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: me. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43691](https://github.com/vllm-project/vllm/pull/43691) | closes_keyword | 0.95 | [SpecDec + Reasoning] Fix race condition when <channel\|> reasoning-end | Fix race condition when <channel\|> reasoning-end Hello, ### Setup I investigated further from my issue #38106. It's actually the combination of speculative decoding, reasonin |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
