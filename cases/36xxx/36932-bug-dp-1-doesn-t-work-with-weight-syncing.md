# vllm-project/vllm#36932: [Bug]: DP>1 doesn't work with weight syncing

| 字段 | 值 |
| --- | --- |
| Issue | [#36932](https://github.com/vllm-project/vllm/issues/36932) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DP>1 doesn't work with weight syncing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` VLLM_SERVER_DEV_MODE=1 vllm serve facebook/opt-125m \ --enforce-eager \ --data-parallel-size 2 \ --weight-transfer-config '{"backend": "nccl"}' \ --load-format dummy ``` Note that changing to `--data-parallel-size 1` would make everything work just fine. ```python # weight_sync_demo.py import threading import requests import torch from openai import OpenAI from transformers import AutoModelForCausalLM from vllm.distributed.weight_transfer.nccl_engine import NCCLTrainerSendWeightsArgs, NCCLWeightTransferEngine from vllm.utils.network_utils import get_ip, get_open_port BASE_URL = "http://localhost:8000" MODEL = "facebook/opt-125m" def generate(client, prompt): return client.completions.create(model=MODEL, prompt=prompt, max_tokens=32, temperature=0).choices[0].text def main(): # Load transformers model on the GPU (idx=2) model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16, device_map="cuda:0") client = OpenAI(base_url=f"{BASE_URL}/v1", api_key="EMPTY") prompt = "The capital of France is" print("Before:", generate(client, prompt)) master_address, master_port = get_ip(), get_open_port() server_world_size = re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: DP>1 doesn't work with weight syncing bug ### Your current environment ### 🐛 Describe the bug ``` VLLM_SERVER_DEV_MODE=1 vllm serve facebook/opt-125m \ --enforce-eager \ --data-parallel-size 2 \ --weight-transfer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: r \ --data-parallel-size 2 \ --weight-transfer-config '{"backend": "nccl"}' \ --load-format dummy ``` Note that changing to `--data-parallel-size 1` would make everything work just fine. ```python # weight_sync_demo.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: the GPU (idx=2) model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16, device_map="cuda:0") client = OpenAI(base_url=f"{BASE_URL}/v1", api_key="EMPTY") prompt = "The capital of France is" print("Befor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ork just fine. ```python # weight_sync_demo.py import threading import requests import torch from openai import OpenAI from transformers import AutoModelForCausalLM from vllm.distributed.weight_transfer.nccl_engine impo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: force-eager \ --data-parallel-size 2 \ --weight-transfer-config '{"backend": "nccl"}' \ --load-format dummy ``` Note that changing to `--data-parallel-size 1` would make everything work just fine. ```python # weight_syn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
