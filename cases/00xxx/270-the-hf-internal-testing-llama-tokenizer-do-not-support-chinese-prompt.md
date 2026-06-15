# vllm-project/vllm#270: The hf-internal-testing/llama-tokenizer do not support Chinese prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#270](https://github.com/vllm-project/vllm/issues/270) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The hf-internal-testing/llama-tokenizer do not support Chinese prompt

### Issue 正文摘录

I wonder whether the vllm support Chinese or other language, because I can successfully inference with English prompt, but when I use Chinese prompt, exception raised: ``` INFO 06-27 11:11:16 tokenizer_utils.py:30] Using the LLaMA fast tokenizer in 'hf-internal-testing/llama-tokenizer' to avoid potential protobuf errors. INFO 06-27 11:13:57 llm_engine.py:128] # GPU blocks: 247, # CPU blocks: 327 Processed prompts: 0%| | 0/1 [00:00 outputs = llm.generate(prompts, sampling_params) File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 114, in generate return self._run_engine(use_tqdm) File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 134, in _run_engine step_outputs = self.llm_engine.step() File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 242, in step self._decode_sequences(seq_groups) File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 259, in _decode_sequences new_token, new_output_text = detokenize_incrementally( File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/engine/tokeniz...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: The hf-internal-testing/llama-tokenizer do not support Chinese prompt I wonder whether the vllm support Chinese or other language, because I can successfully inference with English prompt, but when I use Chinese prompt,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on_utils_fast.py", line 536, in convert_tokens_to_string return self.backend_tokenizer.decoder.decode(tokens) TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString' ``` And I also want to know...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: potential protobuf errors. INFO 06-27 11:13:57 llm_engine.py:128] # GPU blocks: 247, # CPU blocks: 327 Processed prompts: 0%| | 0/1 [00:00 outputs = llm.generate(prompts, sampling_params) File "/mnt/cache/sunyuhan/minic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 10/site-packages/vllm/engine/llm_engine.py", line 242, in step self._decode_sequences(seq_groups) File "/mnt/cache/sunyuhan/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 259, in _decode_sequen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: The hf-internal-testing/llama-tokenizer do not support Chinese prompt I wonder whether the vllm support Chinese or other language, because I can successfully inference with English prompt, but when I use Chinese prompt,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
