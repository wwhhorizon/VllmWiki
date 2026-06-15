# vllm-project/vllm#6416: [Feature]: Apply chat template through `LLM` class

| 字段 | 值 |
| --- | --- |
| Issue | [#6416](https://github.com/vllm-project/vllm/issues/6416) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Apply chat template through `LLM` class

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We do not have a way to apply the chat template to a model via the `LLM` class, so we often see patterns like this ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams max_model_len, tp_size = 8192, 1 model_name = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_name) llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True, enforce_eager=True) messages_list = [ [{"role": "user", "content": "Who are you?"}], [{"role": "user", "content": "write a quick sort algorithm in python."}], [{"role": "user", "content": "Write a piece of quicksort code in C++."}], ] prompt_token_ids = [tokenizer.apply_chat_template(messages, add_generation_prompt=True) for messages in messages_list] outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params) generated_text = [output.outputs[0].text for output in outputs] print(generated_text) ``` ### Pass list of messages and apply chat template ```python from vllm import LLM model = LLM("...") messages_list = [ [{"role": "user", "content": "Who are you?"}], [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ` class, so we often see patterns like this ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams max_model_len, tp_size = 8192, 1 model_name = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pply_chat_template(messages_list, add_generation_prompt=True, tokenize=False) ``` ### Alternatives _No response_ ### Additional context _No response_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tivation and pitch We do not have a way to apply the chat template to a model via the `LLM` class, so we often see patterns like this ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Apply chat template through `LLM` class good first issue;feature request ### 🚀 The feature, motivation and pitch We do not have a way to apply the chat template to a model via the `LLM` class, so we often see pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
