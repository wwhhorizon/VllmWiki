# vllm-project/vllm#37359: Guidance backend structured output doesn't work with openai_gptoss reasoning parser (offline LLM.generate)

| 字段 | 值 |
| --- | --- |
| Issue | [#37359](https://github.com/vllm-project/vllm/issues/37359) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Guidance backend structured output doesn't work with openai_gptoss reasoning parser (offline LLM.generate)

### Issue 正文摘录

## Summary When using `LLM.generate()` (offline/batch mode) with `openai/gpt-oss-20b` and the `guidance` structured output backend, the guidance FSM never activates. The model generates free-form text ignoring the JSON schema. ## Environment - vLLM v0.17.2rc1 (commit 3ec8ae438) - `LLM.generate()` offline path (not OpenAI API server) - `structured_outputs_config = {"backend": "guidance", "reasoning_parser": "openai_gptoss"}` ## Root Cause In `vllm/v1/structured_output/__init__.py`, `should_fill_bitmask()` calls `self.reasoner.is_reasoning_end(request.prompt_token_ids)` on the **prompt** tokens before any generation occurs. Since the prompt doesn't contain Harmony channel markers (` final `), `is_reasoning_end()` returns False, and the guidance FSM is never activated. This works correctly for ` `-based models (Qwen, DeepSeek) because the prompt contains ` ` when thinking is enabled, so the parser can find the end marker once ` ` is generated. But GPT-OSS uses Harmony channel tokens that only appear in the **model output**, not the prompt. ## Expected Behavior The guidance FSM should activate once the model generates the content channel markers (` final `), constraining subsequent ou...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: # Summary When using `LLM.generate()` (offline/batch mode) with `openai/gpt-oss-20b` and the `guidance` structured output backend, the guidance FSM never activates. The model generates free-form text ignoring the JSON s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Guidance backend structured output doesn't work with openai_gptoss reasoning parser (offline LLM.generate) ## Summary When using `LLM.generate()` (offline/batch mode) with `openai/gpt-oss-20b` and the `guidance` structu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sequent output to the JSON schema. ## Reproduction ```python from vllm import LLM, SamplingParams llm = LLM( model="openai/gpt-oss-20b", enforce_eager=True, trust_remote_code=True, structured_outputs_config={ "backend":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gpt-oss-20b` and the `guidance` structured output backend, the guidance FSM never activates. The model generates free-form text ignoring the JSON schema. ## Environment - vLLM v0.17.2rc1 (commit 3ec8ae438) - `LLM.genera...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tain Harmony channel markers (` final `), `is_reasoning_end()` returns False, and the guidance FSM is never activated. This works correctly for ` `-based models (Qwen, DeepSeek) because the prompt contains ` ` when thin...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
