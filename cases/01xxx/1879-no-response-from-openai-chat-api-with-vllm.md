# vllm-project/vllm#1879: No response from OpenAI Chat API with vLLM 

| 字段 | 值 |
| --- | --- |
| Issue | [#1879](https://github.com/vllm-project/vllm/issues/1879) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> No response from OpenAI Chat API with vLLM 

### Issue 正文摘录

Hello, I have been trying to work with OpenAI Chat API with vLLM. I've launched the server as follow: python -m vllm.entrypoints.openai.api_server --model codellama/CodeLlama-13b-Instruct-hf --tensor-parallel-size=2 --dtype='float16' --host `hostname` --tokenizer='hf-internal-testing/llama-tokenizer' --max-model-len=1600 this works with my limited GPU resources and the result in the server side as follow: WARNING 12-01 06:25:41 config.py:346] Casting torch.bfloat16 to torch.float16. 2023-12-01 06:25:44,410 INFO worker.py:1673 -- Started a local Ray instance. INFO 12-01 06:25:45 llm_engine.py:72] Initializing an LLM engine with config: model='codellama/CodeLlama-13b-Instruct-hf', tokenizer='hf-internal-testing/llama-tokenizer', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1600, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) INFO 12-01 06:28:04 llm_engine.py:207] # GPU blocks: 37, # CPU blocks: 655 INFO: Started server process [4527] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://instance-4:8000 (Press CTRL+C t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: hed the server as follow: python -m vllm.entrypoints.openai.api_server --model codellama/CodeLlama-13b-Instruct-hf --tensor-parallel-size=2 --dtype='float16' --host `hostname` --tokenizer='hf-internal-testing/llama-toke...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: r --model codellama/CodeLlama-13b-Instruct-hf --tensor-parallel-size=2 --dtype='float16' --host `hostname` --tokenizer='hf-internal-testing/llama-tokenizer' --max-model-len=1600 this works with my limited GPU resources...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 37, # CPU blocks: 655 INFO: Started server process [4527] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://instance-4:8000 (Press CTRL+C to quit) On the client s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1600, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) INFO 12-01 06:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: as follow: """Example Python client for vllm.entrypoints.api_server""" import argparse import json from typing import Iterable, List import requests def clear_line(n: int = 1) -> None: LINE_UP = '\033[1A' LINE_CLEAR = '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
