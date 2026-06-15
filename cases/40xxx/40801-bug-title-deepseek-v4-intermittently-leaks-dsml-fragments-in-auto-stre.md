# vllm-project/vllm#40801: [Bug]: Title: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#40801](https://github.com/vllm-project/vllm/issues/40801) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Title: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Title: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing Description When serving DeepSeek V4 through vLLM OpenAI-compatible APIs, tool calling behaves inconsistently across modes: 1. `tool_choice=required` is generally stable and returns structured `tool_calls`. 2. `tool_choice=auto` with `stream=true` can intermittently leak DSML marker fragments into normal content. 3. After one leaked turn, subsequent turns are more likely to fail (conversation-state contamination risk). Impact 1. Upstream agents may treat DSML fragments as normal assistant text. 2. Tool-state machines can desynchronize (tool branch expected, text branch taken). 3. The issue is intermittent in streaming mode, making it hard to detect and debug. Reproduction Conditions 1. Model: DeepSeek V4 family 2. Server: vLLM OpenAI-compatible endpoint 3. Server flags include: - `--enable-auto-tool-choice` - `--tool-call-parser deepseek_v4` 4. Request parameters: - non-empty tools - `tool_choice=auto` - `stream=true` 5. Repeating requests eventually shows DSML fragments in streamed `content`. Observed Comparison 1....

## 现有链接修复摘要

#40805 fix/deepseekv4: prevent DSML marker leakage in streaming auto mode(v32 parser only)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Title: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing bug;DSv4 ### Your current environment ### 🐛 Describe the bug Title: DeepSeek V4 intermittently l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: d` significantly reduces or removes the issue. 2. Switching to `stream=false` significantly reduces or removes the issue. 3. This strongly suggests the problem is in the auto streaming parse path. Expected Behavior 1. D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: - `--enable-auto-tool-choice` - `--tool-call-parser deepseek_v4` 4. Request parameters: - non-empty tools - `tool_choice=auto` - `stream=true` 5. Repeating requests eventually shows DSML fragments in streamed `content`....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: erhead: tiny short-lived buffer (bounded by marker length). Recommended Regression Tests 1. Start marker split across chunks at multiple boundaries. 2. Mixed plain-text prefix followed by tool call block. 3. Multi-turn...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40805](https://github.com/vllm-project/vllm/pull/40805) | closes_keyword | 0.95 | fix/deepseekv4: prevent DSML marker leakage in streaming auto mode(v32 parser only) | Fix #40801: DeepSeek V4 may leak DSML marker fragments in `tool_choice=auto` + `stream=true` mode due to split start-token handling in streaming parsing. This PR provides a focu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
