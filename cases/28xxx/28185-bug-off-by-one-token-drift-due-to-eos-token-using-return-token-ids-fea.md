# vllm-project/vllm#28185: [Bug]: Off-by-one token drift due to EOS token using "return_token_ids" feature

| 字段 | 值 |
| --- | --- |
| Issue | [#28185](https://github.com/vllm-project/vllm/issues/28185) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Off-by-one token drift due to EOS token using "return_token_ids" feature

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying out `return_token_ids` feature suggested by blog article https://blog.vllm.ai/2025/10/22/agent-lightning.html In a multi-turn agentic setting, at any turn other than the first one, `token_ids` might include an EOS token at the end when `finish_reason` is `stop`, while `prompt_token_ids` wouldn't include the EOS tokens from previous turns This causes trouble in masking and/or counting and concatenating token ids because we need to decide whether we shall truncate the last token from `token_ids`. Using `finish_reason` seems viable but I am not sure if this is a reliable way. So maybe this is not a bug report but a feature/doc request to clarify. Example code to demonstrate: ```python if __name__ == '__main__': from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125m") tokenizer = llm.get_tokenizer() eos_token_id = tokenizer.eos_token_id print(f"EOS token ID: {eos_token_id}") print(f"EOS token: {tokenizer.decode([eos_token_id])!r}\n") print("=" * 80) prompts1 = ["Is 1+1=2? Answer yes or no"] sampling_params1 = SamplingParams( temperature=0.8, max_tokens=500, include_stop_str_in_output=False # Default: EOS...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: masking and/or counting and concatenating token ids because we need to decide whether we shall truncate the last token from `token_ids`. Using `finish_reason` seems viable but I am not sure if this is a reliable way. So...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: is a reliable way. So maybe this is not a bug report but a feature/doc request to clarify. Example code to demonstrate: ```python if __name__ == '__main__': from vllm import LLM, SamplingParams llm = LLM(model="facebook...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Off-by-one token drift due to EOS token using "return_token_ids" feature bug ### Your current environment ### 🐛 Describe the bug I was trying out `return_token_ids` feature suggested by blog article https://blog....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rature=0.8, max_tokens=500, include_stop_str_in_output=False # Default: EOS excluded from text ) outputs1 = llm.generate(prompts1, sampling_params1) for output in outputs1: result = output.outputs[0] print(f"Prompt: {ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
