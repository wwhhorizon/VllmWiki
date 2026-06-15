# vllm-project/vllm#1573: Load AWQ quantization model OOM !!!

| 字段 | 值 |
| --- | --- |
| Issue | [#1573](https://github.com/vllm-project/vllm/issues/1573) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | quantization |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Load AWQ quantization model OOM !!!

### Issue 正文摘录

example: - https://huggingface.co/TheBloke/CodeLlama-7B-AWQ: physical size is 4GB but use VRAM about 20GB - https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-AWQ: physical size is 17GB but can not run on a dual-A100(40G) server. > `--tensor-parallel-size 2` is configured Why is that? Is it related to the model AWQ process or my VLLM usage? @TheBloke May you please help me with this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Load AWQ quantization model OOM !!! example: - https://huggingface.co/TheBloke/CodeLlama-7B-AWQ: physical size is 4GB but use VRAM about 20GB - https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-AWQ: physical s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Load AWQ quantization model OOM !!! example: - https://huggingface.co/TheBloke/CodeLlama-7B-AWQ: physical size is 4GB but use VRAM about 20GB - https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-AWQ: physical s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -coder-33B-instruct-AWQ: physical size is 17GB but can not run on a dual-A100(40G) server. > `--tensor-parallel-size 2` is configured Why is that? Is it related to the model AWQ process or my VLLM usage? @TheBloke May y...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Load AWQ quantization model OOM !!! example: - https://huggingface.co/TheBloke/CodeLlama-7B-AWQ: physical size is 4GB but use VRAM about 20GB - https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-AWQ: physical s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
