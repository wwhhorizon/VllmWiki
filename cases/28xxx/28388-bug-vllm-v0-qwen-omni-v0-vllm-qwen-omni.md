# vllm-project/vllm#28388: [Bug]: 新版的vllm已经废弃了v0代码，而对qwen-omni系列的模型支持仅限于v0，似乎是因为这个原因，我们无法使用最新版的vllm推理qwen-omni模型

| 字段 | 值 |
| --- | --- |
| Issue | [#28388](https://github.com/vllm-project/vllm/issues/28388) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 新版的vllm已经废弃了v0代码，而对qwen-omni系列的模型支持仅限于v0，似乎是因为这个原因，我们无法使用最新版的vllm推理qwen-omni模型

### Issue 正文摘录

### Your current environment Name: vllm Version: 0.10.2 ### 🐛 Describe the bug 下面的官方样例代码似乎是无法运行的，会对其中的音频使用参数 "mm_processor_kwargs": { "use_audio_in_video": True, }, 进行报错： ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project """ This example shows how to use vLLM for running offline inference with the correct prompt format on Qwen2.5-Omni (thinker only). """ from typing import NamedTuple import vllm.envs as envs from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset from vllm.assets.image import ImageAsset from vllm.assets.video import VideoAsset from vllm.multimodal.image import convert_image_mode from vllm.utils import FlexibleArgumentParser class QueryResult(NamedTuple): inputs: dict limit_mm_per_prompt: dict[str, int] # NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on # lower-end GPUs. # Unless specified, these settings have been tested to work on a single L4. default_system = ( "You are Qwen, a virtual human developed by the Qwen Team, Alibaba " "Group, capable of perceiving auditory and visual inputs, as well as " "generating text and speech." ) def get_mixed_modali...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 新版的vllm已经废弃了v0代码，而对qwen-omni系列的模型支持仅限于v0，似乎是因为这个原因，我们无法使用最新版的vllm推理qwen-omni模型 bug;stale ### Your current environment Name: vllm Version: 0.10.2 ### 🐛 Describe the bug 下面的官方样例代码似乎是无法运行的，会对其中的音频使用参数 "mm_processor_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 最新版的vllm推理qwen-omni模型 bug;stale ### Your current environment Name: vllm Version: 0.10.2 ### 🐛 Describe the bug 下面的官方样例代码似乎是无法运行的，会对其中的音频使用参数 "mm_processor_kwargs": { "use_audio_in_video": True, }, 进行报错： ```python # SPDX...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t] # NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on # lower-end GPUs. # Unless specified, these settings have been tested to work on a single L4. default_system = ( "You are Qwen, a virtual hu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 弃了v0代码，而对qwen-omni系列的模型支持仅限于v0，似乎是因为这个原因，我们无法使用最新版的vllm推理qwen-omni模型 bug;stale ### Your current environment Name: vllm Version: 0.10.2 ### 🐛 Describe the bug 下面的官方样例代码似乎是无法运行的，会对其中的音频使用参数 "mm_processor_kwargs": { "use_a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
