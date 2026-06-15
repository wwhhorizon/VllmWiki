# vllm-project/vllm#19491: [Bug]: vLLM outputs are not reproducible

| 字段 | 值 |
| --- | --- |
| Issue | [#19491](https://github.com/vllm-project/vllm/issues/19491) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM outputs are not reproducible

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `AsyncLLM`, the outputs are not reproducible, even when following the instructions in the documentation (https://docs.vllm.ai/en/stable/usage/reproducibility.html). For example, running the below script multiple times and diff-ing the outputs reveals differences in the logprobs even for outputs that are identical (which shouldn't be the case) and in some cases changed outputs. It seems like it's necessary to make a larger number of requests at the same time to observe the effect (possibly it's related to the scheduling, so a certain pressure is required). When setting `temperature=0`, I expect totally deterministic output from the model, and this is extremely important to our use cases, where we might need to debug problematic model outputs for particular inputs. For this small Qwen2 model, the effect is relatively minor, but for larger models I observed much larger differences. ```python import asyncio import itertools from hashlib import sha1 import datasets import vllm from vllm.v1.engine.async_llm import AsyncLLM async def main(): # 198 prompts, actual contents don't matter prompts = datasets.load_dataset("cais/mml...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vLLM outputs are not reproducible bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When using `AsyncLLM`, the outputs are not reproducible, even when following the instructions in the d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM outputs are not reproducible bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When using `AsyncLLM`, the outputs are not reproducible, even when following the instructions in the d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: vLLM outputs are not reproducible bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When using `AsyncLLM`, the outputs are not reproducible, even when following the instructions in the d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: need to debug problematic model outputs for particular inputs. For this small Qwen2 model, the effect is relatively minor, but for larger models I observed much larger differences. ```python import asyncio import iterto...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: setting `temperature=0`, I expect totally deterministic output from the model, and this is extremely important to our use cases, where we might need to debug problematic model outputs for particular inputs. For this sma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
