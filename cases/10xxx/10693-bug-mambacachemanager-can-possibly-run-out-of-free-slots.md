# vllm-project/vllm#10693: [Bug]: MambaCacheManager Can Possibly Run Out of Free Slots

| 字段 | 值 |
| --- | --- |
| Issue | [#10693](https://github.com/vllm-project/vllm/issues/10693) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MambaCacheManager Can Possibly Run Out of Free Slots

### Issue 正文摘录

### Your current environment _No response_ ### Model Input Dumps _No response_ ### 🐛 Describe the bug In the current implementation of `MambaCacheManager._assign_seq_id_to_cache_index`, if `cur_id` is not amongst the finished requests, it will try to pop a `free_cache_index`. - However, it seems there might be an edge case where the `_assign_seq_id_to_cache_index` tries to aggressively pop free indices before `_release_finished_requests` has a change to return them We have some private experiments involving mamba that we reuse the above `MambaCacheManager` implementation, but we have observed errors like below ``` File "/net/storage149/mnt/md0/nmg/miniconda3/envs/vllm-mamba/lib/python3.10/site-packages/vllm/model_executor/models/jamba.py", line 441, in forward ) = self.mamba_cache.current_run_tensors(input_ids, attn_metadata, File "/net/storage149/mnt/md0/nmg/miniconda3/envs/vllm-mamba/lib/python3.10/site-packages/vllm/model_executor/models/mamba_cache.py", line 54, in current_run_tensors state_indices = self._prepare_current_run_mamba_cache( File "/net/storage149/mnt/md0/nmg/miniconda3/envs/vllm-mamba/lib/python3.10/site-packages/vllm/model_executor/models/mamba_cache.py", line 1...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: MambaCacheManager Can Possibly Run Out of Free Slots bug ### Your current environment _No response_ ### Model Input Dumps _No response_ ### 🐛 Describe the bug In the current implementation of `MambaCacheManager._...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n Out of Free Slots bug ### Your current environment _No response_ ### Model Input Dumps _No response_ ### 🐛 Describe the bug In the current implementation of `MambaCacheManager._assign_seq_id_to_cache_index`, if `cur_i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ._assign_seq_id_to_cache_index`, if `cur_id` is not amongst the finished requests, it will try to pop a `free_cache_index`. - However, it seems there might be an edge case where the `_assign_seq_id_to_cache_index` tries...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: br ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
