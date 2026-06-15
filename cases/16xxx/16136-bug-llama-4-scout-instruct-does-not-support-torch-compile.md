# vllm-project/vllm#16136: [Bug]: llama 4 scout instruct does not support torch.compile

| 字段 | 值 |
| --- | --- |
| Issue | [#16136](https://github.com/vllm-project/vllm/issues/16136) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama 4 scout instruct does not support torch.compile

### Issue 正文摘录

### Your current environment CUDA 12.6 Python 3.12 vllm 0.8.3 transformers 4.5.1 2 x h100 ### 🐛 Describe the bug I'm running version `v0.8.3` of vllm and `v4.5.1` transformers. Trying to bootstrap `meta-llama/Llama-4-Scout-17B-16E-Instruct` with "fp8" quant, and 128K context length on 2 x H100. I keep receiving the following error: ``` [dckr]: (VllmWorker rank=0 pid=1004) WARNING 04-06 10:20:04 [config.py:3785] `torch.compile` is turned on, but the model meta-llama/Llama-4-Scout-17B-16E does not support it. Please open an issue on GitHub if you want it to be supported. [dckr]: (VllmWorker rank=0 pid=1004) WARNING 04-06 10:20:04 [config.py:3785] `torch.compile` is turned on, but the model meta-llama/Llama-4-Scout-17B-16E does not support it. Please open an issue on GitHub if you want it to be supported. [dckr]: (VllmWorker rank=1 pid=1031) WARNING 04-06 10:20:04 [config.py:3785] `torch.compile` is turned on, but the model meta-llama/Llama-4-Scout-17B-16E does not support it. Please open an issue on GitHub if you want it to be supported. [dckr]: (VllmWorker rank=1 pid=1031) WARNING 04-06 10:20:04 [config.py:3785] `torch.compile` is turned on, but the model meta-llama/Llama-4-Scout-1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: llama 4 scout instruct does not support torch.compile bug ### Your current environment CUDA 12.6 Python 3.12 vllm 0.8.3 transformers 4.5.1 2 x h100 ### 🐛 Describe the bug I'm running version `v0.8.3` of vllm and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: . Trying to bootstrap `meta-llama/Llama-4-Scout-17B-16E-Instruct` with "fp8" quant, and 128K context length on 2 x H100. I keep receiving the following error: ``` [dckr]: (VllmWorker rank=0 pid=1004) WARNING 04-06 10:20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nstruct does not support torch.compile bug ### Your current environment CUDA 12.6 Python 3.12 vllm 0.8.3 transformers 4.5.1 2 x h100 ### 🐛 Describe the bug I'm running version `v0.8.3` of vllm and `v4.5.1` transformers....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: llama 4 scout instruct does not support torch.compile bug ### Your current environment CUDA 12.6 Python 3.12 vllm 0.8.3 transformers 4.5.1 2 x h100 ### 🐛 Describe the bug I'm running version `v0.8.3` of vllm and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;model_support;quantization cuda;fp8;quantization build_error dty...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
