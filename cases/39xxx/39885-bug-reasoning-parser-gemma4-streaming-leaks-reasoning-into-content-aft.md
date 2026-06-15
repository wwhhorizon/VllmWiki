# vllm-project/vllm#39885: [Bug]: --reasoning-parser gemma4: streaming leaks reasoning into content after tool results in multi-turn conversations

| 字段 | 值 |
| --- | --- |
| Issue | [#39885](https://github.com/vllm-project/vllm/issues/39885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --reasoning-parser gemma4: streaming leaks reasoning into content after tool results in multi-turn conversations

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description When using `--reasoning-parser gemma4` with streaming enabled, the reasoning content leaks into the `content` field instead of the `reasoning` field. This happens specifically in multi-turn conversations after a tool call result, when the model generates a new tool call in the following turn. The issue does NOT occur with `stream=False` (sync mode), where reasoning is correctly separated. ## How to reproduce ```python from openai import OpenAI import httpx client = OpenAI( base_url='http://localhost:8003/v1', api_key='your-key', http_client=httpx.Client(verify=False) ) tools = [ {"type":"function","function":{"name":"ToolA","description":"First tool","parameters":{"type":"object","properties":{"x":{"type":"string"}},"required":["x"]}}}, {"type":"function","function":{"name":"ToolB","description":"Second tool","parameters":{"type":"object","properties":{"query":{"type":"string"}},"required":["query"]}}}, ] # Simulate a conversation where turn 1 called ToolA, got a result, # and now the model should call ToolB in turn 2 messages = [ {"role": "system", "content": "You are a helpful assistant. Think step by step."}, {"...

## 现有链接修复摘要

#42875 [Bugfix] Fix Gemma4 streaming tool calls lost when entire call arrives in one delta

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: to the `content` field instead of the `reasoning` field. This happens specifically in multi-turn conversations after a tool call result, when the model generates a new tool call in the following turn. The issue does NOT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ful assistant. Think step by step."}, {"role": "user", "content": "Search for information about data protection laws"}, {"role": "assistant", "content": "", "tool_calls": [ {"id": "call_001", "type": "function", "functi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: sh python -m vllm.entrypoints.cli.main serve RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic \ --served_model_name my_model \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --enable_prefix_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: --reasoning-parser gemma4: streaming leaks reasoning into content after tool results in multi-turn conversations bug ### Your current environment ### 🐛 Describe the bug ## Description When using `--reasoning-pars...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: --reasoning-parser gemma4: streaming leaks reasoning into content after tool results in multi-turn conversations bug ### Your current environment ### 🐛 Describe the bug ## Description When using `--reasoning-pars...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42875](https://github.com/vllm-project/vllm/pull/42875) | closes_keyword | 0.95 | [Bugfix] Fix Gemma4 streaming tool calls lost when entire call arrives in one delta | closes #39885. Bug 1's fix changed `<\|tool_response>` handling from `return False` to `continue`. That is correct within a single turn, but on a **second** generation turn — after |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
