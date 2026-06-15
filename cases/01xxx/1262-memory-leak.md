# vllm-project/vllm#1262: Memory leak

| 字段 | 值 |
| --- | --- |
| Issue | [#1262](https://github.com/vllm-project/vllm/issues/1262) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Memory leak

### Issue 正文摘录

This is my setup: Ubuntu 20.04.6 LTS Build cuda_11.8.r11.8/compiler.31833905_0 A10 NVIDIA python -m vllm.entrypoints.openai.api_server --model TheBloke/Wizard-Vicuna-13B-Uncensored-AWQ --quantization awq --host 0.0.0.0 --gpu-memory-utilization 0.50 Memory utilization starts at 50% but within a day it goes to 75%. Let me know if you need any other data from me. Thanks.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Memory leak This is my setup: Ubuntu 20.04.6 LTS Build cuda_11.8.r11.8/compiler.31833905_0 A10 NVIDIA python -m vllm.entrypoints.openai.api_server --model TheBloke/Wizard-Vicuna-13B-Uncensored-AWQ --quantization awq --h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ts.openai.api_server --model TheBloke/Wizard-Vicuna-13B-Uncensored-AWQ --quantization awq --host 0.0.0.0 --gpu-memory-utilization 0.50 Memory utilization starts at 50% but within a day it goes to 75%. Let me know if you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Memory leak This is my setup: Ubuntu 20.04.6 LTS Build cuda_11.8.r11.8/compiler.31833905_0 A10 NVIDIA python -m vllm.entrypoints.openai.api_server --model TheBloke/Wizard-Vicuna-13B-Uncensored-AWQ --quantization awq --h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ler.31833905_0 A10 NVIDIA python -m vllm.entrypoints.openai.api_server --model TheBloke/Wizard-Vicuna-13B-Uncensored-AWQ --quantization awq --host 0.0.0.0 --gpu-memory-utilization 0.50 Memory utilization starts at 50% b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
