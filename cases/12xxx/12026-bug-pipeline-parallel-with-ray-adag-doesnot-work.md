# vllm-project/vllm#12026: [Bug]: Pipeline parallel with Ray ADAG doesnot work

| 字段 | 值 |
| --- | --- |
| Issue | [#12026](https://github.com/vllm-project/vllm/issues/12026) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallel with Ray ADAG doesnot work

### Issue 正文摘录

### Your current environment vllm version: vllm-0.6.6.post1 ```python from pathlib import Path import json import asyncio from vllm import LLM, AsyncLLMEngine, AsyncEngineArgs, SamplingParams import torch from transformers import AutoTokenizer from time import time from uuid import uuid4 import argparse models = { "llama2-7b": "/path/to/llama" } def example_to_prompt(tokenizer, ex) -> str: prompt = tokenizer.apply_chat_template( [{"role": "user", "content": ex["query"]}], add_generation_prompt=True, tokenize=False, ) return prompt async def run_query(engine, params, query: str): request_id = uuid4() outputs = engine.generate(query, params, request_id) async for output in outputs: final_output = output responses = [] for output in final_output.outputs: responses.append(output.text) return responses async def process(engine, params, queries): tasks = [asyncio.create_task(run_query(engine, params, q)) for q in queries] results = [] for task in asyncio.as_completed(tasks): result = await task results.append(result) return results def main(args): tp_size = args.tensor_parallel_size pp_size = args.pipeline_parallel_size print(f"tp_size: {tp_size} pp_size: {pp_size}") enforce_eager = arg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: el with Ray ADAG doesnot work bug;ray ### Your current environment vllm version: vllm-0.6.6.post1 ```python from pathlib import Path import json import asyncio from vllm import LLM, AsyncLLMEngine, AsyncEngineArgs, Samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: el_size=tp_size, pipeline_parallel_size=pp_size, dtype=torch.bfloat16, # *** for debug **** enforce_eager=enforce_eager, #max_num_seqs=32, disable_log_requests=True, disable_custom_all_reduce=True,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Dumps _No response_ ### 🐛 Describe the bug Sorry to bother you @ruisearch42 @rkooo567 We try to apply pipeline parallelism to llama2-7b in spmd mode, but found device placement error as follows: ![image](https://github....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Tokenizer from time import time from uuid import uuid4 import argparse models = { "llama2-7b": "/path/to/llama" } def example_to_prompt(tokenizer, ex) -> str: prompt = tokenizer.apply_chat_template( [{"role": "user", "c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: disable_custom_all_reduce=True, distributed_executor_backend="ray", gpu_memory_utilization=0.85, ) ) num_prompts = args.num_prompts sample = args.num_sampling params = SamplingParams(n=sample, temperature=1, skip_specia...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
