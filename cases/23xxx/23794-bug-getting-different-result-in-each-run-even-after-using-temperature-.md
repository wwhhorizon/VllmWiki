# vllm-project/vllm#23794: [Bug]: Getting different result in each run even after using temperature=0 in instruction finetuned Gemma-3-270m-it

| 字段 | 值 |
| --- | --- |
| Issue | [#23794](https://github.com/vllm-project/vllm/issues/23794) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Getting different result in each run even after using temperature=0 in instruction finetuned Gemma-3-270m-it

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug import json, pandas as pd from vllm import LLM, SamplingParams from transformers import AutoTokenizer checkpoint_dir = "gemma-ner" tok = AutoTokenizer.from_pretrained(checkpoint_dir) llm = LLM(model=checkpoint_dir, dtype="auto", max_model_len=4096) prompts = [tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages_list] params = SamplingParams(max_tokens=256, temperature=0) outs = llm.generate(prompts, params) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sult in each run even after using temperature=0 in instruction finetuned Gemma-3-270m-it bug;stale ### Your current environment ### 🐛 Describe the bug import json, pandas as pd from vllm import LLM, SamplingParams from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0m-it bug;stale ### Your current environment ### 🐛 Describe the bug import json, pandas as pd from vllm import LLM, SamplingParams from transformers import AutoTokenizer checkpoint_dir = "gemma-ner" tok = AutoTokenizer....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: okenizer.from_pretrained(checkpoint_dir) llm = LLM(model=checkpoint_dir, dtype="auto", max_model_len=4096) prompts = [tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages_list] params...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ms) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ", max_model_len=4096) prompts = [tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages_list] params = SamplingParams(max_tokens=256, temperature=0) outs = llm.generate(prompts, params...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
