# vllm-project/vllm#7956: [Performance]: some questions regarding the performance degradation between asyncLLMEngine and the LLM class when TP = 4

| 字段 | 值 |
| --- | --- |
| Issue | [#7956](https://github.com/vllm-project/vllm/issues/7956) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: some questions regarding the performance degradation between asyncLLMEngine and the LLM class when TP = 4

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I encountered this issue while conducting some experiments to test throughput. When using the same dataset, the performance of batch inference with the LLM class is three times higher than the performance of sending POST requests via api_server, even with the same dataset and GPU configuration (single node, 4A100, TP=4, the model is LLama2-70b AWQ). ## LLM class with TP=4 ```python def run_hf( requests: List[Tuple[str, int, int]], model: str, tokenizer: PreTrainedTokenizerBase, trust_remote_code: bool, ) -> float: llm = LLM( model, tensor_parallel_size=4, quantization="AWQ", max_num_batched_tokens=4096, ) tokenizer.pad_token = tokenizer.eos_token input_num_tokens = [] output_num_tokens = [] input_tokenized_prompt = [] sample_params = [] start = time.perf_counter() for i in tqdm(range(len(requests))): prompt, prompt_len, output_len = requests[i] # Generate the sequences. input_ids = tokenizer(prompt, padding=True).input_ids input_num_tokens.append(len(input_ids)) input_tokenized_prompt.append(input_ids) sampling_params = SamplingParams( temperature=1.0, top_p=1.0, max_tokens=output_len, detokeniz...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sending POST requests via api_server, even with the same dataset and GPU configuration (single node, 4A100, TP=4, the model is LLama2-70b AWQ). ## LLM class with TP=4 ```python def run_hf( requests: List[Tuple[str, int,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _server, even with the same dataset and GPU configuration (single node, 4A100, TP=4, the model is LLama2-70b AWQ). ## LLM class with TP=4 ```python def run_hf( requests: List[Tuple[str, int, int]], model: str, tokenizer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: adation between asyncLLMEngine and the LLM class when TP = 4 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I encountered this issue while conducting some experi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression I encountered this issue while conducting some experiments to test throughput. When using the same dataset, the performance of batch infe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tput) output = tokenizer.decode(output.prompt_token_ids, skip_special_tokens=True) # print(output) # print(type(output)) output_num_tokens.append(len(output)) end = time.perf_counter() return end - start, input_num_toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
