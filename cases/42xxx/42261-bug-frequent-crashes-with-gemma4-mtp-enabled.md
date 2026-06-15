# vllm-project/vllm#42261: [Bug]: Frequent crashes with gemma4 MTP enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#42261](https://github.com/vllm-project/vllm/issues/42261) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Frequent crashes with gemma4 MTP enabled

### Issue 正文摘录

gemma4:31b on H200 with MTP enabled regularly crashes with `torch.AcceleratorError: CUDA error: device-side assert triggered` . I am generating 8 spec tokens for MTP. Shutting down and starting vLLM "fixes" the issue for a period of a few hours. I have 3 instances of vllm running, with gemma4:26b running on two RTX 6000s which do not experience this issue. Only gemma4:31b on the H200 has this issue. ### Your current environment ### 🐛 Describe the bug ``` /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [117,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [118,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [119,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [120,0,0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 5: indexSelectSmallIndex: block: [1,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [117,0,0] A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: on H200 with MTP enabled regularly crashes with `torch.AcceleratorError: CUDA error: device-side assert triggered` . I am generating 8 spec tokens for MTP. Shutting down and starting vLLM "fixes" the issue for a period...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: torch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [1,0,0], thread: [116,0,0] Assertion `srcIndex < srcSelectDimSize` failed. /pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Frequent crashes with gemma4 MTP enabled bug gemma4:31b on H200 with MTP enabled regularly crashes with `torch.AcceleratorError: CUDA error: device-side assert triggered` . I am generating 8 spec tokens for MTP....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -router_vllm-31b-h200-1 8d5aszha 0964fb3b-7457-415e-9448-5b9cda258cdc -- Request failed. Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/ray/serve/_private/replica.py", line 1310, in _ha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
