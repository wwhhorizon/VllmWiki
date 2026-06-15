# vllm-project/vllm#17543: [Bug]: cached_get_processor is not actually cached

| 字段 | 值 |
| --- | --- |
| Issue | [#17543](https://github.com/vllm-project/vllm/issues/17543) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: cached_get_processor is not actually cached

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I'm using PDB debug this project, during the Initialization I noticed this question In File: `vllm/transformers_utils/processor.py` The function `cached_get_processor` is defined as: ```python cached_get_processor = lru_cache(get_processor) ``` This line does not create a cached version of get_processor. Instead, it passes `get_processor` as an argument to `functools.lru_cache`, which simply returns a decorator function — not a wrapped version of the original function. This results in: `cached_get_processor(...)` behaving exactly like `get_processor(...)` I also tried this minimal reproduction ``` from functools import lru_cache def get_processor(name): print(f"Loading {name}") return name cached_get_processor = lru_cache(get_processor) cached_get_processor("clip") cached_get_processor("clip") # Expected no print, but prints again ``` No caching takes place So I'm wondering if this is designed to be like this or is just a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cessor = lru_cache(get_processor) ``` This line does not create a cached version of get_processor. Instead, it passes `get_processor` as an argument to `functools.lru_cache`, which simply returns a decorator function —...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
