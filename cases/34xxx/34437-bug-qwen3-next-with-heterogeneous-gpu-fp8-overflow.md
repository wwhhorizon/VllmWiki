# vllm-project/vllm#34437: [Bug]: Qwen3 Next with heterogeneous GPU (FP8 overflow?)

| 字段 | 值 |
| --- | --- |
| Issue | [#34437](https://github.com/vllm-project/vllm/issues/34437) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Next with heterogeneous GPU (FP8 overflow?)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have 3x3090 and 1x4090, all cards have 24Gb VRAM. I'm experimenting with Qwen3 Coder models and able to run either Qwen3 Coder 30B at BF16 precision, or Qwen3 Coder Next 80B at FP8 precision. As I can understand, FP8 running fine on RTX 3090 with Marlin kernel - and it's running! Now, I'm trying to compare models performance - both 30B and 80B have 3B active params, so they are close in inference speed. But I'm facing issues, example - https://huggingface.co/unsloth/Qwen3-Coder-Next-FP8-Dynamic/discussions/2 Output of 80B FP8 is not consistent, while 30B bf16 is always perfect. Now I spent few hours investigating possible issues and found culprit. If I run with --tensor-parallel-size 4, then output inconsistent. If I run with --pipeline-parallel-size 4, AND RTX 4090 is last in CUDA_VISIBLE_DEVICES, then output CONSISTENT If I run with --pipeline-parallel-size 4, AND RTX 4090 is not last in CUDA_VISIBLE_DEVICES, then output inconsistent If I run with --pipeline-parallel-size 4, AND RTX 4090 is first in CUDA_VISIBLE_DEVICES, then vllm decided to use native FP8 and engine crashes. If I run with --enforce-eager and --tp 4, then loo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3 Next with heterogeneous GPU (FP8 overflow?) bug;stale ### Your current environment ### 🐛 Describe the bug I have 3x3090 and 1x4090, all cards have 24Gb VRAM. I'm experimenting with Qwen3 Coder models and ab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ith Qwen3 Coder models and able to run either Qwen3 Coder 30B at BF16 precision, or Qwen3 Coder Next 80B at FP8 precision. As I can understand, FP8 running fine on RTX 3090 with Marlin kernel - and it's running! Now, I'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: der Next 80B at FP8 precision. As I can understand, FP8 running fine on RTX 3090 with Marlin kernel - and it's running! Now, I'm trying to compare models performance - both 30B and 80B have 3B active params, so they are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 Next with heterogeneous GPU (FP8 overflow?) bug;stale ### Your current environment ### 🐛 Describe the bug I have 3x3090 and 1x4090, all cards have 24Gb VRAM. I'm experimenting with Qwen3 Coder models and ab...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 Next with heterogeneous GPU (FP8 overflow?) bug;stale ### Your current environment ### 🐛 Describe the bug I have 3x3090 and 1x4090, all cards have 24Gb VRAM. I'm experimenting with Qwen3 Coder models and ab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
