# vllm-project/vllm#29863: [Bug]: fails to inference prompt ends with '.' ':' for video inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#29863](https://github.com/vllm-project/vllm/issues/29863) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: fails to inference prompt ends with '.' ':' for video inputs

### Issue 正文摘录

### Your current environment **vllm version v0.11.0** **model Qwen/Qwen3-VL-4B-Instruct** **model args** ``` {'model': 'Qwen3-VL-4B-Instruct', 'gpu_memory_utilization': 0.9, 'trust_remote_code': True, 'tensor_parallel_size': 1, 'pipeline_parallel_size': 1, 'max_model_len': 8192, 'swap_space': 4, 'enable_lora': False, 'enforce_eager': True, 'disable_custom_all_reduce': True, 'disable_cascade_attn': True, 'mm_processor_kwargs': {'max_pixels': 1572864, 'do_sample_frames': False}, 'mm_processor_cache_gb': 0} ``` ### 🐛 Describe the bug i came to same issue https://github.com/vllm-project/vllm/issues/26195 so i tried **mm_processor_cache_gb=0** to workaround it. It works with my image input but fails on video input. The trace is following: **Error stack trace** i tried **mm_processor_cache_gb=128**, with same video input, it works well. **Input prompt after chat template** ```text ' user\nplease describe this video in details. \n assistant\n' ``` **other prompt for comparing** ```text # this one works well please describe this video in details ``` ```text # this one also breaks please describe this video in details: ``` **Possible Root Cause** i did some debugging and think it should be...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ts bug;stale ### Your current environment **vllm version v0.11.0** **model Qwen/Qwen3-VL-4B-Instruct** **model args** ``` {'model': 'Qwen3-VL-4B-Instruct', 'gpu_memory_utilization': 0.9, 'trust_remote_code': True, 'tens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ' ':' for video inputs bug;stale ### Your current environment **vllm version v0.11.0** **model Qwen/Qwen3-VL-4B-Instruct** **model args** ``` {'model': 'Qwen3-VL-4B-Instruct', 'gpu_memory_utilization': 0.9, 'trust_remot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :'. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: allel_size': 1, 'max_model_len': 8192, 'swap_space': 4, 'enable_lora': False, 'enforce_eager': True, 'disable_custom_all_reduce': True, 'disable_cascade_attn': True, 'mm_processor_kwargs': {'max_pixels': 1572864, 'do_sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: fails to inference prompt ends with '.' ':' for video inputs bug;stale ### Your current environment **vllm version v0.11.0** **model Qwen/Qwen3-VL-4B-Instruct** **model args** ``` {'model': 'Qwen3-VL-4B-Instruct'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
