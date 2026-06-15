# vllm-project/vllm#590: GPTJ output not consistent with that of transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#590](https://github.com/vllm-project/vllm/issues/590) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GPTJ output not consistent with that of transformers

### Issue 正文摘录

Hey guys, I've been trying to get the base GPT-J model (EleutherAI/gpt-j-6b) served using vLLM, but I am running into issues with the quality of the output. Using the same offline inference code as in https://github.com/vllm-project/vllm/blob/main/examples/offline_inference.py, here is what I obtain from the model (running on an RTX A5000): ``` python3 from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=128) llm = LLM(model="EleutherAI/gpt-j-6b") prompts = ["AI is going to"] * 4 outputs = [t.outputs[0].text for t in llm.generate(prompts, sampling_params)] output = [" get a lot of new stuff. A lot of other new stuff\nthat's been added and things are going to come out.\nthat you know, it's going to be implemented, that's coming out.\nin the\nand we've got like a lot of stuff coming out, and things in the like AI stuff. So we're going to be doing.\nbefore the new stuff\nand some of the AI, the future.\nthe AI\nis added in the next year and we're going to the next year.\nthat's going to be in the next gen.\nand it's going to be added", " change the way we work, not just the way we do business, but also how we work and we live....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: obtain from the model (running on an RTX A5000): ``` python3 from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=128) llm = LLM(model="EleutherAI/gpt-j-6b") prom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ffline_inference.py, here is what I obtain from the model (running on an RTX A5000): ``` python3 from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=128) llm = L...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: that," said Peter Lee, vice president of Google\'s self-driving cars and mapping division.\n\n"It will allow us to make the most efficient use of public roads that are more congested and have more traffic," Lee told the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at of transformers bug Hey guys, I've been trying to get the base GPT-J model (EleutherAI/gpt-j-6b) served using vLLM, but I am running into issues with the quality of the output. Using the same offline inference code a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: del.generate(inputs["input_ids"], **params) outputs.append(tokenizer.decode(out[0])) outputs = [ 'AI is going to be our future and this is going to be a big part of that," said Peter Lee, vice president of Google\'s sel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
