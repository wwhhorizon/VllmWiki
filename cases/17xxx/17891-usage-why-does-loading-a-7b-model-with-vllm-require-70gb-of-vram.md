# vllm-project/vllm#17891: [Usage]: Why does loading a 7b model with VLLM require 70GB of vram?

| 字段 | 值 |
| --- | --- |
| Issue | [#17891](https://github.com/vllm-project/vllm/issues/17891) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why does loading a 7b model with VLLM require 70GB of vram?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ```python from vllm import LLM, SamplingParams LLM("Qwen/Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) ``` it seems kv cache used a lot of vram? how can i close it? ![Image](https://github.com/user-attachments/assets/2dac4e0c-0fdd-49f8-8031-4aff10634e93) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Why does loading a 7b model with VLLM require 70GB of vram? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ```python from vllm import LLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ect_env.py` ``` ### How would you like to use vllm ```python from vllm import LLM, SamplingParams LLM("Qwen/Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) ``` it seems kv cache used a lot of vram? how can i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 93) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) ``` it seems kv cache used a lot of vram? how can i close it? ![Image](https://github.com/user-attachments/assets/2dac4e0c-0fdd-49f8-8031-4aff10634e93) ### Bef...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
