# vllm-project/vllm#37362: Guidance structured output blocked during thinking with nemotron_v3 reasoning parser (offline LLM.generate)

| 字段 | 值 |
| --- | --- |
| Issue | [#37362](https://github.com/vllm-project/vllm/issues/37362) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Guidance structured output blocked during thinking with nemotron_v3 reasoning parser (offline LLM.generate)

### Issue 正文摘录

## Summary When using `LLM.generate()` (offline/batch mode) with `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` and the `guidance` structured output backend + `nemotron_v3` reasoning parser, the guidance FSM appears to constrain output from the first token instead of waiting for thinking to end (` `). The model generates 8192 tokens but only produces `{` as visible content. ## Environment - vLLM v0.17.2rc1 (commit 3ec8ae438) - `LLM.generate()` offline path - `structured_outputs_config = {"backend": "guidance", "reasoning_parser": "nemotron_v3"}` - `enable_thinking=True` via chat template ## Behavior - **Thinking OFF + structured output: WORKS** — model produces valid JSON in 34 tokens - **Thinking ON + free-form: WORKS** — thinking extracted correctly, correct answer - **Thinking ON + structured output: FAILS** — 8192 tokens generated, visible text is just `{` This suggests the guidance FSM constrains during the thinking phase rather than waiting for ` `. The model's thinking tokens are forced into JSON-conforming patterns, producing garbage. ## Related Similar to #37359 (GPT-OSS + `openai_gptoss` parser), but different reasoning parser and different model architecture (`NemotronHFo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t from the first token instead of waiting for thinking to end (` `). The model generates 8192 tokens but only produces `{` as visible content. ## Environment - vLLM v0.17.2rc1 (commit 3ec8ae438) - `LLM.generate()` offli...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e model's thinking tokens are forced into JSON-conforming patterns, producing garbage. ## Related Similar to #37359 (GPT-OSS + `openai_gptoss` parser), but different reasoning parser and different model architecture (`N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tructured output backend + `nemotron_v3` reasoning parser, the guidance FSM appears to constrain output from the first token instead of waiting for thinking to end (` `). The model generates 8192 tokens but only produce...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: VIDIA-Nemotron-3-Nano-30B-A3B-BF16` and the `guidance` structured output backend + `nemotron_v3` reasoning parser, the guidance FSM appears to constrain output from the first token instead of waiting for thinking to end...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rate()` (offline/batch mode) with `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` and the `guidance` structured output backend + `nemotron_v3` reasoning parser, the guidance FSM appears to constrain output from the first t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
