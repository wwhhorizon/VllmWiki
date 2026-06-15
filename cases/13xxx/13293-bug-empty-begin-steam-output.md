# vllm-project/vllm#13293: [Bug]: empty begin steam output

| 字段 | 值 |
| --- | --- |
| Issue | [#13293](https://github.com/vllm-project/vllm/issues/13293) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: empty begin steam output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash image: docker.io/vllm/vllm-openai:0.7.2 environment: - VLLM_LOGGING_LEVEL=DEBUG command: - "--model=/data1/checkpoints/20250210/checkpoint-31322" - "--max-model-len=8000" - "--host=0.0.0.0" - "--served-model-name=qwen2.5" - "--tensor-parallel-size=2" - "--gpu-memory-utilization=0.8 ``` I used the docker-compose to run the finetuned qwen2.5-14b model. then, i used the code below the call the llm. ```python from openai import OpenAI client = OpenAI(api_key="123", base_url="http://localhost:30253/v1") for i in client.chat.completions.create( messages=[{"role": "user", "content": query}], model="qwen2.5", stream=True, max_tokens=200 ): print(i) ``` while i got a lot of empty content at the begining of the stream. here is the log of the docker container. ```bash INFO 02-14 05:41:15 logger.py:39] Received request chatcmpl-6bef81cb4de24787a00de2ff383b76e1: prompt: ' system\nYou are a helpful assistant. \n user\n你好 \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[' ', ' '], stop_token_ids=[], bad_word...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug ```bash image: docker.io/vllm/vllm-openai:0.7.2 environment: - VLLM_LOGGING_LEVEL=DEBUG command: - "--model=/data1/checkpoints/20250210/checkpoint-31322" - "--max-model-le...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: empty begin steam output bug;stale ### Your current environment ### 🐛 Describe the bug ```bash image: docker.io/vllm/vllm-openai:0.7.2 environment: - VLLM_LOGGING_LEVEL=DEBUG command: - "--model=/data1/checkpoint...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment: - VLLM_LOGGING_LEVEL=DEBUG command: - "--model=/data1/checkpoints/20250210/checkpoint-31322" - "--max-model-len=8000" - "--host=0.0.0.0" - "--served-model-name=qwen2.5" - "--tensor-parallel-size=2" - "--gpu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
