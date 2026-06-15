# vllm-project/vllm#2946: unittest test_prefix_caching failed when initialize LLM with small max_num_seqs

| 字段 | 值 |
| --- | --- |
| Issue | [#2946](https://github.com/vllm-project/vllm/issues/2946) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> unittest test_prefix_caching failed when initialize LLM with small max_num_seqs

### Issue 正文摘录

I just want to run the utest below, with model 01-ai/Yi-6B-Chat, a list of prompts with length=3. `pytest -s tests/prefix_caching/test_prefix_caching.py` if I use the default argument(max_num_seqs=256) while initializing LLM instance, it looks good and all tests passed. ![image](https://github.com/vllm-project/vllm/assets/142368437/d41a96d3-26b9-45e0-9046-969bd95c8114) but if I set max_num_seqs=1 ( **or a value smaller than len(prompts)** ), this utest run failed. ![image](https://github.com/vllm-project/vllm/assets/142368437/84d4d91e-9c54-42fc-8a96-c4234e57be0f) In addition, I add one-line log at model_runner.py:253 to show the block_tables after _prepare_prompt. ![image](https://github.com/vllm-project/vllm/assets/142368437/724232ea-5d5c-4ac3-be33-d250e2e67dd1) It shows that if I use the default argument(max_num_seqs=256), the block_tables are empty since it run all 3 prompts simultaneously. (so maybe prefix caching does not work in this case) ![image](https://github.com/vllm-project/vllm/assets/142368437/67e88757-770f-49c5-8f1f-7029fa75d05d) when set max_num_seqs=1, the block_tables are empty at the first time, but the 2nd and 3rd times it contains values, in which it output wr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: unittest test_prefix_caching failed when initialize LLM with small max_num_seqs stale I just want to run the utest below, with model 01-ai/Yi-6B-Chat, a list of prompts with length=3. `pytest -s tests/prefix_caching/tes...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e0f) In addition, I add one-line log at model_runner.py:253 to show the block_tables after _prepare_prompt. ![image](https://github.com/vllm-project/vllm/assets/142368437/724232ea-5d5c-4ac3-be33-d250e2e67dd1) It shows t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: M with small max_num_seqs stale I just want to run the utest below, with model 01-ai/Yi-6B-Chat, a list of prompts with length=3. `pytest -s tests/prefix_caching/test_prefix_caching.py` if I use the default argument(max...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t test_prefix_caching failed when initialize LLM with small max_num_seqs stale I just want to run the utest below, with model 01-ai/Yi-6B-Chat, a list of prompts with length=3. `pytest -s tests/prefix_caching/test_prefi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: unittest test_prefix_caching failed when initialize LLM with small max_num_seqs stale I just want to run the utest below, with model 01-ai/Yi-6B-Chat, a list of prompts with length=3. `pytest -s tests/prefix_caching/tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
