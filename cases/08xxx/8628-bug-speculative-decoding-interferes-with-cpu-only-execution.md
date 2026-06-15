# vllm-project/vllm#8628: [Bug]: Speculative decoding interferes with CPU-only execution 

| 字段 | 值 |
| --- | --- |
| Issue | [#8628](https://github.com/vllm-project/vllm/issues/8628) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding interferes with CPU-only execution 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know, speculative decoding isn't (rightfully) implemented on CPU, as the `SpecDecodeWorker` in only instantiated in `GPUExecutor`. Nevertheless, when enabling spec decoding on a cpu build, parameter `n` appears to be ignored and only 1 completion is returned. Here's a simple snippet to quickly reproduce the issue: ```python import argparse from typing import List, Tuple from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.utils import FlexibleArgumentParser def create_test_prompts() -> List[Tuple[str, SamplingParams]]: """Create a list of test prompts with their sampling parameters.""" return [ ("A robot may not injure a human being", SamplingParams(temperature=0.1, n=2, top_p=0.8, seed=42)), ("To be or not to be,", SamplingParams(temperature=0.1, n=2, top_p=0.8, seed=42)), ] def process_requests(engine: LLMEngine, test_prompts: List[Tuple[str, SamplingParams]]): """Continuously process a list of prompts and handle the outputs.""" request_id = 0 while test_prompts or engine.has_unfinished_requests(): if test_prompts: prompt, sampling_params = test_prompts....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Speculative decoding interferes with CPU-only execution bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know, speculative decoding isn't (rightfully)
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed in `GPUExecutor`. Nevertheless, when enabling spec decoding on a cpu build, parameter `n` appears to be ignored and only 1 completion is returned. Here's a simple snippet to quickly reproduce the issue: ```python imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hen spec decoding is enabled on CPU to point out it's ignored, just like CUDA graphs and a ton of other features. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g.py --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 \ --seed 44 --use-v2-block-manager # n ignored python bug.py --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 \ --seed 44 --use-v2-block-manager --speculative_model TinyLlama/Ti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: with CPU-only execution bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know, speculative decoding isn't (rightfully) implemented on CPU, as the `SpecDecodeW...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
