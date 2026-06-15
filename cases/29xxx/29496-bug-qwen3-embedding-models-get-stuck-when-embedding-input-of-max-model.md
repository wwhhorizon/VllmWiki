# vllm-project/vllm#29496: [Bug]: Qwen3-Embedding models get stuck when embedding input of max-model-len

| 字段 | 值 |
| --- | --- |
| Issue | [#29496](https://github.com/vllm-project/vllm/issues/29496) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Embedding models get stuck when embedding input of max-model-len

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment tldr: - model Qwen3-Embedding-8B - vllm v0.11.2 - gpu NVIDIA RTX 4000 SFF Ada Generation ### Issue description I serve the Qwen3-Embedding-8B model via vllm. When I send a request with input of the max-model-len (16384 in my case), it gets stuck without logging any error. When I reduce the length of input by 1 to 16383, it works fine and returns the embedding in a few seconds. Had the same issue also for smaller Qwen3-Embedding-0.6B and also in v0.10.0. Attaching code to reproduce below. ### How I run vllm ``` docker run -d \ --gpus device=0 \ --name qwen3_embedding_8b \ -p 8080:8000 \ --ipc=host \ -v "hf_cache:/root/.cache/huggingface" \ vllm/vllm-openai:v0.11.2 \ --trust-remote-code \ --model Qwen/Qwen3-Embedding-8B \ --runner pooling \ --convert embed \ --gpu-memory-utilization 0.9 \ --max-model-len 16384 \ --enable-prefix-caching \ --dtype auto \ --kv-cache-dtype auto \ --scheduling-policy priority \ --enable-chunked-prefill \ --max-num-batched-tokens 1024 \ --max-num-seqs 10 ``` ### Minimal code to reproduce ``` import time from openai import OpenAI from transformers import AutoTokenizer def get_embedding(mod...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: en3-Embedding models get stuck when embedding input of max-model-len bug;stale ### Your current environment ### 🐛 Describe the bug ### Environment tldr: - model Qwen3-Embedding-8B - vllm v0.11.2 - gpu NVIDIA RTX 4000 SF...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: in v0.10.0. Attaching code to reproduce below. ### How I run vllm ``` docker run -d \ --gpus device=0 \ --name qwen3_embedding_8b \ -p 8080:8000 \ --ipc=host \ -v "hf_cache:/root/.cache/huggingface" \ vllm/vllm-openai:v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: nvironment tldr: - model Qwen3-Embedding-8B - vllm v0.11.2 - gpu NVIDIA RTX 4000 SFF Ada Generation ### Issue description I serve the Qwen3-Embedding-8B model via vllm. When I send a request with input of the max-model-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-Embedding models get stuck when embedding input of max-model-len bug;stale ### Your current environment ### 🐛 Describe the bug ### Environment tldr: - model Qwen3-Embedding-8B - vllm v0.11.2 - gpu NVIDIA RTX
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
