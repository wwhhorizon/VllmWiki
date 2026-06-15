# vllm-project/vllm#9111: [Bug]: AMD MultiStep Feature Issue. Missing argument: 'turn_prefills_into_decodes' in `advance_step()`

| 字段 | 值 |
| --- | --- |
| Issue | [#9111](https://github.com/vllm-project/vllm/issues/9111) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AMD MultiStep Feature Issue. Missing argument: 'turn_prefills_into_decodes' in `advance_step()`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Cause There is a change in advance_step API in PR #8378 . The changed is made to `flash_attn.py` and `flashinfer.py` but not other backend. ## Code Snippet to highlight the difference in `advance_step` API `flash_attn.py` ``` def advance_step(self, model_input: "ModelInputForGPUWithSamplingMetadata", sampled_token_ids: Optional[torch.Tensor], block_size: int, num_seqs: int, num_queries: int, turn_prefills_into_decodes: bool = False): ``` `rocm_flash_attn.py` ``` def advance_step(self, model_input: "ModelInputForGPUWithSamplingMetadata", sampled_token_ids: Optional[torch.Tensor], block_size: int, num_seqs: int, num_queries: int): ``` # Confusion whether this is a bug or because multistep feature is not supported on AMD I saw there are other PR that is stating that multi steps feature are working on AMD e.g. #8474 . # Logs The error logs and traceback is as follows: ``` ERROR 10-06 16:38:45 engine.py:157] (VIImWorkerProcess pid=207827) ERROR 10-06 16:38:45 multiproc_worker_utils . py : 231 rker_base.py", line 327, in execute_model ERROR 10-06 16:38:45 engine.py:157] TypeError("advance_step() go...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tep(self, model_input: "ModelInputForGPUWithSamplingMetadata", sampled_token_ids: Optional[torch.Tensor], block_size: int, num_seqs: int, num_queries: int, turn_prefil
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AMD MultiStep Feature Issue. Missing argument: 'turn_prefills_into_decodes' in `advance_step()` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Cause There is a chang...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vance_step API in PR #8378 . The changed is made to `flash_attn.py` and `flashinfer.py` but not other backend. ## Code Snippet to highlight the difference in `advance_step` API `flash_attn.py` ``` def advance_step(self,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t, turn_prefills_into_decodes: bool = False): ``` `rocm_flash_attn.py` ``` def advance_step(self, model_input: "ModelInputForGPUWithSamplingMetadata", sampled_token_ids: Optional[torch.Tensor], block_size: int, num_seqs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: to_decodes' in `advance_step()` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Cause There is a change in advance_step API in PR #8378 . The changed is made to `flash_attn....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
