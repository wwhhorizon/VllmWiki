# vllm-project/vllm#38897: [Bug] DS conv state layout does not support speculative decoding with mamba_cache_mode='align'

| 字段 | 值 |
| --- | --- |
| Issue | [#38897](https://github.com/vllm-project/vllm/issues/38897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] DS conv state layout does not support speculative decoding with mamba_cache_mode='align'

### Issue 正文摘录

## Problem `get_conv_copy_spec` in `vllm/model_executor/layers/mamba/mamba_utils.py` assumes the SD layout `(num_blocks, state_len, dim)` where slicing `state[block, offset:]` along `state_len` yields a contiguous view because `dim` is the innermost (contiguous) axis. With the DS layout `(num_blocks, dim, state_len)`, slicing along the last dim (`state_len`) when `num_accepted_tokens > 1` (i.e. `offset > 0`) produces a **non-contiguous** view because `dim` is strided by `state_len`: ```python def get_conv_copy_spec( state: torch.Tensor, block_ids: list[int], cur_block_idx: int, num_accepted_tokens: int, ) -> MambaCopySpec: """Return a MambaCopySpec for copying a convolutional state slice. Works for both SD layout (num_blocks, state_len, dim) and DS layout (num_blocks, dim, state_len). """ src_block_id = block_ids[cur_block_idx] offset = num_accepted_tokens - 1 if is_conv_state_dim_first(): # DS layout: (num_blocks, dim, state_len) — state_len is last. if offset > 0: # Slicing along the last dim yields a non-contiguous view # because features (dim) are strided by state_len. raise NotImplementedError( "DS conv state layout does not yet support speculative " "decoding with mamba_cach...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: [Bug] DS conv state layout does not support speculative decoding with mamba_cache_mode='align' ## Problem `get_conv_copy_spec` in `vllm/model_executor/layers/mamba/mamba_utils.py` assumes the SD layout `(num_blocks, sta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _utils.py` assumes the SD layout `(num_blocks, state_len, dim)` where slicing `state[block, offset:]` along `state_len` yields a contiguous view because `dim` is the innermost (contiguous) axis. With the DS layout `(num...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: resented. ## Impact This blocks using the DS conv state layout (`VLLM_SSM_CONV_STATE_LAYOUT=DS`) with speculative decoding when prefix caching align mode is active (`mamba_cache_mode='align'`). DS layout is the preferre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: with mamba_cache_mode='align' ## Problem `get_conv_copy_spec` in `vllm/model_executor/layers/mamba/mamba_utils.py` assumes the SD layout `(num_blocks, state_len, dim)` where slicing `state[block, offset:]` along `state_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug] DS conv state layout does not support speculative decoding with mamba_cache_mode='align' ## Problem `get_conv_copy_spec` in `vllm/model_executor/layers/mamba/mamba_utils.py` assumes the SD layout `(num_blocks, sta...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
