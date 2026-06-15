# vllm-project/vllm#19174: [Bug]: EAGLE-3 loading error for Llama 3.3 70b

| 字段 | 值 |
| --- | --- |
| Issue | [#19174](https://github.com/vllm-project/vllm/issues/19174) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;speculative_decoding |
| 子分类 | edge_case |
| Operator 关键词 | kernel;operator |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE-3 loading error for Llama 3.3 70b

### Issue 正文摘录

### Your current environment I am pulling latest vllm `v0.9.0.1` and installing the [latest fixed PR for EAGLE-3](https://github.com/vllm-project/vllm/pull/19033). Instance is 8*H100. ### 🐛 Describe the bug Using serving command. The EAGLE-3 head for llama 3.3 70B is from its [official release](https://huggingface.co/yuhuili/EAGLE3-LLaMA3.3-Instruct-70B) ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.3-70B-Instruct --seed 42 --tensor-parallel-size 8 --max-model-len 131072 --max-num-batched-tokens 131072 --max-num-seqs 100 --max_seq_len_to_capture 131072 --gpu_memory_utilization 0.9 --no-enable-prefix-caching --speculative_config '{ "model": "yuhuili/EAGLE3-LLaMA3.3-Instruct-70B", "draft_tensor_parallel_size": 8, "num_speculative_tokens":5, "method": "eagle3" }' ``` Then I hit this error. ``` (VllmWorker rank=2 pid=1204085) ERROR 06-05 02:08:42 [multiproc_executor.py:522] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=2 pid=1204085) ERROR 06-05 02:08:42 [multiproc_executor.py:522] File "/opt/pytorch/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl (VllmWorker rank=2 pid=1204085) ERROR 06-05 02:08:42 [multiproc_execut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: le ### Your current environment I am pulling latest vllm `v0.9.0.1` and installing the [latest fixed PR for EAGLE-3](https://github.com/vllm-project/vllm/pull/19033). Instance is 8*H100. ### 🐛 Describe the bug Using ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: AGLE-3](https://github.com/vllm-project/vllm/pull/19033). Instance is 8*H100. ### 🐛 Describe the bug Using serving command. The EAGLE-3 head for llama 3.3 70B is from its [official release](https://huggingface.co/yuhuil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: EAGLE-3 loading error for Llama 3.3 70b bug;stale ### Your current environment I am pulling latest vllm `v0.9.0.1` and installing the [latest fixed PR for EAGLE-3](https://github.com/vllm-project/vllm/pull/19033)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: EAGLE-3 loading error for Llama 3.3 70b bug;stale ### Your current environment I am pulling latest vllm `v0.9.0.1` and installing the [latest fixed PR for EAGLE-3](https://github.com/vllm-project/vllm/pull/19033)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 204085) ERROR 06-05 02:08:42 [multiproc_executor.py:522] assert_size_stride(arg2_1, (16032, 8192), (8192, 1)) (VllmWorker rank=2 pid=1204085) ERROR 06-05 02:08:42 [multiproc_executor.py:522] AssertionError: expected siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
