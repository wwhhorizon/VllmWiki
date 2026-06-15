# vllm-project/vllm#19665: [Bug]: Phi-3-Small model reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata'

| 字段 | 值 |
| --- | --- |
| Issue | [#19665](https://github.com/vllm-project/vllm/issues/19665) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-3-Small model reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata'

### Issue 正文摘录

### Your current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 pip install flash-attn --no-build-isolation` ### 🐛 Describe the bug When I try to run Phi-3 Small models (both 8k and 128k), it would throw an error of ``` AttributeError: 'NoneType' object has no attribute 'prefill_metadata' ``` specifically in `vllm/attention/backends/blocksparse_attn.py` line 416, where the code tries to access `prefill_metadata` by calling `if prefill_meta := attn_metadata.prefill_metadata:`. I tried to trace the error myself, it went all the way in the `phi3_small.py` where the model calls the `self.attn` in the pass, but I cannot find where the model fills the `attn_metadata`, I saw from other posts that the model is using the context manager to handle this, which I am not quite familiar with. Also, other models such as Llama would not have such an issue, I suspect this to be related to the attention type, as for phi 3 small, it would run the `torch.ops.vllm.unified_attention` in `vllm/attention/layer.py`, but Llama model would not touch such a line. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ur current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 pip install flash-attn --no-build-isolation` ### 🐛 Describe the bug When I try to run Phi-3 Small models (both 8k and 128k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Phi-3-Small model reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug;stale ### Your current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: el reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug;stale ### Your current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 pip install flash-attn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Phi-3-Small model reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug;stale ### Your current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mall model reporting AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug;stale ### Your current environment I am using `VLLM 0.9.1`, and the flash_attention installed by `MAX_JOBS=4 pip install fla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
