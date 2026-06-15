# vllm-project/vllm#19481: [Bug]: EAGLE in v1with FlashInfer backend, AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens'.

| 字段 | 值 |
| --- | --- |
| Issue | [#19481](https://github.com/vllm-project/vllm/issues/19481) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE in v1with FlashInfer backend, AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running EAGLE on V1 with FlashInfer backend and encounter the following error ``` AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens' ... ``` The issue might stem from the fact that [Eagle proposer creates `FlashAttentionMetadata` by default](https://github.com/vllm-project/vllm/blob/main/vllm/v1/spec_decode/eagle.py#L121). ### Code to Reproduce ```python # SPDX-License-Identifier: Apache-2.0 import argparse import json import os # set envs os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.v1.metrics.reader import Counter, Vector def load_prompts(dataset_path, num_prompts): if os.path.exists(dataset_path): prompts = [] try: with open(dataset_path) as f: for line in f: data = json.loads(line) prompts.append(data["turns"][0]) except Exception as e: print(f"Error reading dataset: {e}") return [] else: prompts = ["The future of AI is", "The president of the United States is"] return prompts[:num_prompts] def parse_args(): parser = ar...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: d, AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens'. bug;stale ### Your current environment ### 🐛 Describe the bug Running EAGLE on V1 with FlashInfer backend and encounter the follow...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: EAGLE in v1with FlashInfer backend, AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens'. bug;stale ### Your current environment ### 🐛 Describe the bug Running EAGLE on V1 with Fla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Code to Reproduce ```python # SPDX-License-Identifier: Apache-2.0 import argparse import json import os # set envs os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: "--dataset", type=str, default="./examples/data/gsm8k.jsonl", help="downloaded from the eagle repo " "https://github.com/SafeAILab/EAGLE/blob/main/eagle/data/", ) parser.add_argument( "--method", type=str, default="eagl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: Bug]: EAGLE in v1with FlashInfer backend, AttributeError: 'FlashAttentionMetadata' object has no attribute 'num_decode_tokens'. bug;stale ### Your current environment ### 🐛 Describe the bug Running EAGLE on V1 with Flas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
