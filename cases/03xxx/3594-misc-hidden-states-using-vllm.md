# vllm-project/vllm#3594: [Misc]: hidden states using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3594](https://github.com/vllm-project/vllm/issues/3594) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: hidden states using vllm

### Issue 正文摘录

### Anything you want to discuss about vllm. Following is a little piece of code to extract embeddings from a certain layer of LLM: ```python def process_row(prompt: str, model, tokenizer, layers_to_use: list, remove_period: bool): """ Processes a row of data and returns the embeddings. """ if remove_period: prompt = prompt.rstrip(". ") inputs = tokenizer(prompt, return_tensors="pt") with torch.no_grad(): outputs = model.generate(inputs.input_ids, output_hidden_states=True, return_dict_in_generate=True, max_new_tokens=1, min_new_tokens=1) embeddings = {} for layer in layers_to_use: last_hidden_state = outputs.hidden_states[0][layer][0][-1] embeddings[layer] = [last_hidden_state.numpy().tolist()] return embeddings ``` It's pretty standard way, but it's pretty slow. Is there any way to use vllm to make it faster without needing to call generate function everytime? I've tried batching, but it's slow too. Any help is appreciated! One way to get last hidden state values using vllm is as follows: ```python from vllm import LLM, SamplingParams from vllm.sequence import (SamplerOutput, Sequence, SequenceGroup, SequenceData, SequenceGroupMetadata, SequenceStatus) from transformers import L...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ings from a certain layer of LLM: ```python def process_row(prompt: str, model, tokenizer, layers_to_use: list, remove_period: bool): """ Processes a row of data and returns the embeddings. """ if remove_period: prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: hidden states using vllm stale ### Anything you want to discuss about vllm. Following is a little piece of code to extract embeddings from a certain layer of LLM: ```python def process_row(prompt: str, model, to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tion everytime? I've tried batching, but it's slow too. Any help is appreciated! One way to get last hidden state values using vllm is as follows: ```python from vllm import LLM, SamplingParams from vllm.sequence import...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e, SequenceGroup, SequenceData, SequenceGroupMetadata, SequenceStatus) from transformers import LlamaModel, LlamaTokenizer from vllm import EngineArgs, LLMEngine, SamplingParams, RequestOutput from vllm.sequence import...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceData, SequenceGroupMetadata llm = LLM(model=path_to_llama2) # Enable top-k sampling to reflect the accurate memory usage. vocab_size = llm.llm_engine.workers[0].model.config.vocab_size sampling_params = SamplingParams...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
