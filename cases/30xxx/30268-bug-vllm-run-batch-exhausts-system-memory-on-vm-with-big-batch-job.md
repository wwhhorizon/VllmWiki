# vllm-project/vllm#30268: [Bug]: vllm run-batch exhausts system memory on VM with big batch job

| 字段 | 值 |
| --- | --- |
| Issue | [#30268](https://github.com/vllm-project/vllm/issues/30268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm run-batch exhausts system memory on VM with big batch job

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a big batch job on an embedding model (a fine tuned Qwen/Qwen3-Embedding-8B) on a GCP VM (g4-standard-48) which has 177 GB of system memory, vLLM allocates so much memory (tries to allocate more then the 177GB available) that eventually my VM crashed. Interestingly this happens right towards the end of the job when the progress bar already shows 100% completed. ## Reproduction instructions Generate a big batch file like this: ```python import json import uuid NUM_LINES = 500_000 FILLER = "test " * 24000 # ~32k tokens with open("batch.jsonl", "w") as f: for _ in range(NUM_LINES): line = { "custom_id": str(uuid.uuid4()), "method": "POST", "url": "/v1/embeddings", "body": { "encoding_format": "float", "input": FILLER, "truncate_prompt_tokens": 32000 } } f.write(json.dumps(line) + "\n") ``` Then run vllm like this: ```bash vllm run-batch --model Qwen/Qwen3-Embedding-8B --runner pooling --convert embed -i batch.jsonl -o output.jsonl --max-model-len 32000 ``` And you will see that the system memory continues to rise until it eventually exhausts your resources. (and it practically doesn't use the GPU while doing it). ## Wor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eproduction instructions Generate a big batch file like this: ```python import json import uuid NUM_LINES = 500_000 FILLER = "test " * 24000 # ~32k tokens with open("batch.jsonl", "w") as f: for _ in range(NUM_LINES): l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: This can be worked around by splitting up the batch file into multiple smaller ones but this still causes frustration when it happens to you the first time. ## Effort to solve the problem I have tried to solve the probl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug When running a big batch job on an embedding model (a fine tuned Qwen/Qwen3-Embedding-8B) on a GCP VM (g4-standard-48) which has 177 GB of system memory, vLLM allocates so much memory (tries to al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: vllm run-batch exhausts system memory on VM with big batch job bug;stale ### Your current environment ### 🐛 Describe the bug When running a big batch job on an embedding model (a fine tuned Qwen/Qwen3-Embedding-8B...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
