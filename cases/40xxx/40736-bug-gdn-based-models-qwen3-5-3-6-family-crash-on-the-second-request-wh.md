# vllm-project/vllm#40736: [Bug]: GDN-based models (Qwen3.5/3.6 family) crash on the second request when running on multi-GPU XPU with prefix caching enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#40736](https://github.com/vllm-project/vllm/issues/40736) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GDN-based models (Qwen3.5/3.6 family) crash on the second request when running on multi-GPU XPU with prefix caching enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GDN-based models (Qwen3.5/3.6 family) crash on the second request when running on multi-GPU XPU with prefix caching enabled. The first request always succeeds. The crash happens when prefix caching activates the Mamba state copy path on the second turn. **To reproduce**: serve any Qwen3.5/3.6 model on multi-GPU XPU with --enable-prefix-caching and send two requests back to back. **Error**: File "vllm/v1/worker/mamba_utils.py", line 128, in collect_mamba_copy_meta src_ptrs_np[offset] = copy_spec.start_addr OverflowError: Python int too large to convert to C long File "vllm/v1/worker/mamba_utils.py", line 130, in collect_mamba_copy_meta dst_ptrs_np[offset] = state[dest_block_id].data_ptr() OverflowError: Python int too large to convert to C long **Root cause**: On multi-GPU XPU, data_ptr() returns unsigned 64-bit memory addresses that can exceed signed int64 range (2^63 - 1). Direct assignment into the numpy array (which is signed int64) overflows. **Fix** - reinterpret the pointer bits as signed int64 via ctypes in mamba_utils.py: import ctypes # line 128 - was: src_ptrs_np[offset] = copy_spec.start_addr src_ptrs_np[offset] = ctyp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: GDN-based models (Qwen3.5/3.6 family) crash on the second request when running on multi-GPU XPU with prefix caching enabled bug ### Your current environment ### 🐛 Describe the bug GDN-based models (Qwen3.5/3.6 fa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ix caching activates the Mamba state copy path on the second turn. **To reproduce**: serve any Qwen3.5/3.6 model on multi-GPU XPU with --enable-prefix-caching and send two requests back to back. **Error**: File "vllm/v1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pret the pointer bits as signed int64 via ctypes in mamba_utils.py: import ctypes # line 128 - was: src_ptrs_np[offset] = copy_spec.start_addr src_ptrs_np[offset] = ctypes.c_int64(copy_spec.start_addr).value # line 130...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 50. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 130, in collect_mamba_copy_meta dst_ptrs_np[offset] = state[dest_block_id].data_ptr() OverflowError: Python int too large to convert to C long **Root cause**: On multi-GPU XPU, data_ptr() returns unsigned 64-bit memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
