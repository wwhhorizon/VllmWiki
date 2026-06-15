# vllm-project/vllm#15131: [Usage]: relationship between embedding size and vocab_size

| 字段 | 值 |
| --- | --- |
| Issue | [#15131](https://github.com/vllm-project/vllm/issues/15131) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: relationship between embedding size and vocab_size

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I’ve noticed that the embedding size is always smaller than the vocab_size. Additionally, sometimes the `prompt_token_ids` are larger than the embedding size. ​Is there a way to map the embedding vector to each of the prompt tokens so that I can retrieve the logit of a prompt token like this: `embeds[i, labels[i]]`? ```python outputs = llm.encode(prompts) print(f'vocab_size: {llm.get_tokenizer().vocab_size}') for i in range(len(outputs)): labels = outputs[i].prompt_token_ids[1:] embeds = outputs[i].outputs.data print(f'{i}-th prompt_token_ids: {labels}') print(f'{i}-th embeddings: {embeds.shape}') ``` ```log Processed prompts: 100%|██████████| 4/4 [00:00<00:00, 55.18it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s] vocab_size: 50254 0-th prompt_token_ids: [4007, 273, 253, 1986, 2077, 310] 0-th embeddings: torch.Size([7, 2560]) 1-th prompt_token_ids: [13, 619, 1416, 310] 1-th embeddings: torch.Size([5, 2560]) 2-th prompt_token_ids: [5347, 273, 6181, 310] 2-th embeddings: torch.Size([5, 2560]) 3-th prompt_token_ids: [2852, 273, 14980, 310] 3-th embeddings: torch....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: relationship between embedding size and vocab_size usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I’ve noticed that the embedding s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: relationship between embedding size and vocab_size usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I’ve noticed that the embedding s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
