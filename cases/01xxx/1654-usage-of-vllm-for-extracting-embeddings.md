# vllm-project/vllm#1654: usage of vllm for extracting embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#1654](https://github.com/vllm-project/vllm/issues/1654) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> usage of vllm for extracting embeddings

### Issue 正文摘录

Following is a little piece of code to extract embeddings from a certain layer of LLM: ``` def process_row(prompt: str, model, tokenizer, layers_to_use: list, remove_period: bool): """ Processes a row of data and returns the embeddings. """ if remove_period: prompt = prompt.rstrip(". ") inputs = tokenizer(prompt, return_tensors="pt") with torch.no_grad(): outputs = model.generate(inputs.input_ids, output_hidden_states=True, return_dict_in_generate=True, max_new_tokens=1, min_new_tokens=1) embeddings = {} for layer in layers_to_use: last_hidden_state = outputs.hidden_states[0][layer][0][-1] embeddings[layer] = [last_hidden_state.numpy().tolist()] return embeddings ``` It's pretty standard way, but it's pretty slow. Is there any way to use vllm to make it faster without needing to call generate function everytime? I've tried batching, but it's slow too. Any help is appreciated!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion everytime? I've tried batching, but it's slow too. Any help is appreciated!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: embeddings from a certain layer of LLM: ``` def process_row(prompt: str, model, tokenizer, layers_to_use: list, remove_period: bool): """ Processes a row of data and returns the embeddings. """ if remove_period: prompt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
