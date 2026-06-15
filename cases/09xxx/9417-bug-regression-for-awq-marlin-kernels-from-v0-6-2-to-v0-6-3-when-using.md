# vllm-project/vllm#9417: [Bug]: Regression ~~for AWQ marlin kernels~~ from v0.6.2 to v0.6.3 when using CUDA Graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#9417](https://github.com/vllm-project/vllm/issues/9417) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression ~~for AWQ marlin kernels~~ from v0.6.2 to v0.6.3 when using CUDA Graphs

### Issue 正文摘录

### Your current environment First of all: fantastic project :-) Thank you for everything. I would like to fix this bug. But I just do not have the capacity now. So I just thought I would try to make a good bug report. ### Model Input Dumps _No response_ ### 🐛 Describe the bug If I run this model in `v0.6.2`: ```bash vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 -tp 4 --gpu-memory-utilization 0.90 --max-model-len 32768 ``` All works well and good :-) If I run it in `v0.6.3` ```bash vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 -tp 4 --gpu-memory-utilization 0.90 --max-model-len 32768 --enforce-eager ``` All works well and good with enforce eager :-) If I drop the `enforce-eager` ```bash vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 -tp 4 --gpu-memory-utilization 0.90 --max-model-len 32768 ``` I get random repetition on large prompts 6000+ token. Or if I do multiple request in parallel I get `CUDA: illegal memory access` My guess is that there is something dynamic in the updated `awq_marlin` kernels. My hunch (this is untested): #8973 but I am not fully understanding how my non MoE should be affected by this. ### Before submitting...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: be the bug If I run this model in `v0.6.2`: ```bash vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 -tp 4 --gpu-memory-utilization 0.90 --max-model-len 32768 ``` All works well and good :-) If I run it in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : Regression ~~for AWQ marlin kernels~~ from v0.6.2 to v0.6.3 when using CUDA Graphs bug ### Your current environment First of all: fantastic project :-) Thank you for everything. I would like to fix this bug. But I jus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: acity now. So I just thought I would try to make a good bug report. ### Model Input Dumps _No response_ ### 🐛 Describe the bug If I run this model in `v0.6.2`: ```bash vllm serve hugging-quants/Meta-Llama-3.1-70B-Instru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Regression ~~for AWQ marlin kernels~~ from v0.6.2 to v0.6.3 when using CUDA Graphs bug ### Your current environment First of all: fantastic project :-) Thank you for everything. I would like to fix this bug. But...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: verything. I would like to fix this bug. But I just do not have the capacity now. So I just thought I would try to make a good bug report. ### Model Input Dumps _No response_ ### 🐛 Describe the bug If I run this model i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
