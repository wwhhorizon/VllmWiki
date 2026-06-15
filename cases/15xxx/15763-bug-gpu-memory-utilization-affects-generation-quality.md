# vllm-project/vllm#15763: [Bug]: gpu_memory_utilization affects generation quality

| 字段 | 值 |
| --- | --- |
| Issue | [#15763](https://github.com/vllm-project/vllm/issues/15763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpu_memory_utilization affects generation quality

### Issue 正文摘录

### Your current environment vllm 0.7.3 python 3.11.5 torch 2.5.1 transformers 4.50.1 cuda/12.6 Using an Nvidia A100 with 40GB memory. ### 🐛 Describe the bug The parameter "gpu_memory_utilization" significantly affects the quality of generated response. mem_limit=0.2, pass@ 1 0.05 2 0.09 4 0.14 8 0.22 mem_limit=0.95, pass@ 1 0.11 2 0.20 4 0.33 8 0.52 ```python import os import argparse from tqdm import tqdm import torch import re from vllm import LLM, SamplingParams from datasets import load_dataset, Dataset from peft import PeftModel import datasets from transformers import BitsAndBytesConfig, AutoModelForCausalLM, AutoTokenizer, GenerationConfig import math from vllm.lora.request import LoRARequest parser = argparse.ArgumentParser() parser.add_argument('--precision', type=int, default=16) parser.add_argument('--greedy', type=bool, default=False, action=argparse.BooleanOptionalAction) parser.add_argument('--temperature', type=float, default=0.7) parser.add_argument('--model', type=str, default="Qwen/Qwen2.5-3B-Instruct") parser.add_argument('--max_len', type=int, default=2048) parser.add_argument('--lora', type=str, default=None) parser.add_argument('--mem_limit', type=float) arg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: .14 8 0.22 mem_limit=0.95, pass@ 1 0.11 2 0.20 4 0.33 8 0.52 ```python import os import argparse from tqdm import tqdm import torch import re from vllm import LLM, SamplingParams from datasets import load_dataset, Datas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: aset = eval_dataset.batch(batch_size=eval_batch_size//eval_shots) torch_dtype = torch.bfloat16 quant_storage_dtype = torch.bfloat16 if args.precision==4: quantization_config = BitsAndBytesConfig( load_in_4bit=True, bnb_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ngParams from datasets import load_dataset, Dataset from peft import PeftModel import datasets from transformers import BitsAndBytesConfig, AutoModelForCausalLM, AutoTokenizer, GenerationConfig import math from vllm.lor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt environment vllm 0.7.3 python 3.11.5 torch 2.5.1 transformers 4.50.1 cuda/12.6 Using an Nvidia A100 with 40GB memory. ### 🐛 Describe the bug The parameter "gpu_memory_utilization" significantly affects the quality of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gpu_memory_utilization affects generation quality bug;stale ### Your current environment vllm 0.7.3 python 3.11.5 torch 2.5.1 transformers 4.50.1 cuda/12.6 Using an Nvidia A100 with 40GB memory. ### 🐛 Describe th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
