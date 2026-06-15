# vllm-project/vllm#17876: [Bug]: Speculative decode ngram ，logprobs is 0.0

| 字段 | 值 |
| --- | --- |
| Issue | [#17876](https://github.com/vllm-project/vllm/issues/17876) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speculative decode ngram ，logprobs is 0.0

### Issue 正文摘录

### Your current environment Description: When running speculative decoding with the N-Gram method in vLLM 0.7.3, the logprobs values in the generation results are consistently empty, even though logprobs=True is explicitly set. Steps to Reproduce: Configure N-Gram speculative decoding. Enable logprobs in SamplingParams. Generate text and check the output. Example Code: sampling_params = SamplingParams(temperature=0, top_p=1, repetition_penalty=1.1, max_tokens=256,logprobs=1) llm = LLM( model=model_path, tensor_parallel_size=2, enable_prefix_caching=True, speculative_model="[ngram]", num_speculative_tokens=5, ngram_prompt_lookup_max=2, # num_scheduler_steps=16, enable_chunked_prefill=True, use_v2_block_manager=True, ) output： ![Image](https://github.com/user-attachments/assets/2beb3502-4a34-4faa-a01c-1246c6665879) ### 🐛 Describe the bug VLLM version 0.7.3 i use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative decode ngram ，logprobs is 0.0 bug ### Your current environment Description: When running speculative decoding with the N-Gram method in vLLM 0.7.3, the logprobs values in the generation results are co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ration results are consistently empty, even though logprobs=True is explicitly set. Steps to Reproduce: Configure N-Gram speculative decoding. Enable logprobs in SamplingParams. Generate text and check the output. Examp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpty, even though logprobs=True is explicitly set. Steps to Reproduce: Configure N-Gram speculative decoding. Enable logprobs in SamplingParams. Generate text and check the output. Example Code: sampling_params = Sampli...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nsistently empty, even though logprobs=True is explicitly set. Steps to Reproduce: Configure N-Gram speculative decoding. Enable logprobs in SamplingParams. Generate text and check the output. Example Code: sampling_par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
