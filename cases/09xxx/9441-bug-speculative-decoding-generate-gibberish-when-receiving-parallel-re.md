# vllm-project/vllm#9441: [Bug]: Speculative decoding generate gibberish when receiving parallel requests with different seeds

| 字段 | 值 |
| --- | --- |
| Issue | [#9441](https://github.com/vllm-project/vllm/issues/9441) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding generate gibberish when receiving parallel requests with different seeds

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was doing some experiments with speculative decoding and found an strange behavior when the engine process request in parallel, there are some requests generated with gibberish. Here's the script to reproduce the bug: ```py import asyncio import tempfile import uuid from tests.mq_llm_engine.utils import RemoteMQLLMEngine from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.multiprocessing.client import MQLLMEngineClient DEFAULT_SEED=0 async def generate_repeated(client : MQLLMEngineClient, seed=None): params = SamplingParams(temperature=0, stop=['20:'], seed=seed, max_tokens=220) prompt = 'Write the following phrase exactly 20 times: I will never miss any tokens.\n1: I will never miss any tokens.\n2: ' async for r in client.generate(prompt=prompt, sampling_params=params, request_id=uuid.uuid4()): if r.finished: txt = r.outputs[0].text n = len(txt.split('I will never miss any tokens.')) print(r.request_id, f'Has {n} occurrences') if n != 19: print(txt) # print(txt) async def generate_other(client : MQLLMEngineClient, seed: int): params = SamplingPa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nerated with gibberish. Here's the script to reproduce the bug: ```py import asyncio import tempfile import uuid from tests.mq_llm_engine.utils import RemoteMQLLMEngine from vllm import SamplingParams from vllm.engine.a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;oom;slowdown dtype;env_dependency;s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: l requests with different seeds bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was doing some experiments with speculative decoding and found an strange behavior when the e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative decoding generate gibberish when receiving parallel requests with different seeds bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was doing some experiment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
