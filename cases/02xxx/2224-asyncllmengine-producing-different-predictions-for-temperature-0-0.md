# vllm-project/vllm#2224: AsyncLLMEngine producing different predictions for temperature=0.0

| 字段 | 值 |
| --- | --- |
| Issue | [#2224](https://github.com/vllm-project/vllm/issues/2224) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncLLMEngine producing different predictions for temperature=0.0

### Issue 正文摘录

Hello and thank you for this amazing software. I have noticed that when sending parallel requests to vllm server sometimes same prompt returns different predictions when using greedy decoding. Issue is not reproducible using any prompt. Unfortunately I can not share the one I am using right now. I've also reproduced the issue with this script: ``` from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.sampling_params import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs import argparse import uuid import asyncio engine = None def random_uuid() -> str: return str(uuid.uuid4().hex) async def generate(prompt: str, semaphore: asyncio.Semaphore): async with semaphore: sampling_params = SamplingParams(temperature=0.0, max_tokens=2000, stop=["\n\n"], use_beam_search=False) request_id = random_uuid() results_generator = engine.generate(prompt, sampling_params, request_id) async for request_output in results_generator: final_output = request_output assert final_output is not None text_outputs = [output.text for output in final_output.outputs] return text_outputs[0] async def main(): with open("badprompt.txt", "r") as file: prompt = file.read() semaphore = async...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: AsyncLLMEngine producing different predictions for temperature=0.0 Hello and thank you for this amazing software. I have noticed that when sending parallel requests to vllm server sometimes same prompt returns different...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: mplingParams(temperature=0.0, max_tokens=2000, stop=["\n\n"], use_beam_search=False) request_id = random_uuid() results_generator = engine.generate(prompt, sampling_params, request_id) async for request_output in result...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: returns different predictions when using greedy decoding. Issue is not reproducible using any prompt. Unfortunately I can not share the one I am using right now. I've also reproduced the issue with this script: ``` from...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: arams(temperature=0.0, max_tokens=2000, stop=["\n\n"], use_beam_search=False) request_id = random_uuid() results_generator = engine.generate(prompt, sampling_params, request_id) async for request_output in results_gener...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ) ``` script started with: ``` CUDA_VISIBLE_DEVICES=1 python atest.py --model deepseek-ai/deepseek-coder-6.7b-base ``` Running on: NVIDIA RTX A5000 NVIDIA-SMI 535.104.12 Driver Version: 535.104.12 CUDA Version: 12.2 Env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
