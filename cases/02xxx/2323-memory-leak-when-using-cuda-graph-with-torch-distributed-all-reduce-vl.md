# vllm-project/vllm#2323: Memory leak when using CUDA Graph with torch.distributed.all_reduce (vLLM default config)

| 字段 | 值 |
| --- | --- |
| Issue | [#2323](https://github.com/vllm-project/vllm/issues/2323) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Memory leak when using CUDA Graph with torch.distributed.all_reduce (vLLM default config)

### Issue 正文摘录

Running the following on the latest vLLM master ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 8 --max-num-batched-tokens 32768 --max-num-seqs 192 ``` and then ``` git clone https://github.com/ray-project/llmperf cd llmperf export OPENAI_API_KEY="EMPTY" export OPENAI_API_BASE="http://localhost:8000/v1" python token_benchmark_ray.py --model "mistralai/Mixtral-8x7B-Instruct-v0.1" --num-concurrent-requests 192 --max-num-completed-requests 100000 --timeout 3600 ``` (you will need to apply the following patch to avoid 400 errors: ``` diff --git a/src/llmperf/ray_clients/openai_chat_completions_client.py b/src/llmperf/ray_clients/openai_chat_completions_client.py index f2e0a91252..0f95e30a71 100644 --- a/src/llmperf/ray_clients/openai_chat_completions_client.py +++ b/src/llmperf/ray_clients/openai_chat_completions_client.py @@ -20,7 +20,7 @@ class OpenAIChatCompletionsClient(LLMClient): prompt, prompt_len = prompt message = [ - {"role": "system", "content": ""}, + # {"role": "system", "content": ""}, {"role": "user", "content": prompt}, ] model = request_config.model ``` ) produces a pretty big CPU memory leak. This c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trypoints/openai/api_server.py @@ -18,6 +18,8 @@ from fastapi.exceptions import RequestValidationError from fastapi.middleware.cors import CORSMiddleware from fastapi.responses import JSONResponse, StreamingResponse, Re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Memory leak when using CUDA Graph with torch.distributed.all_reduce (vLLM default config) bug Running the following on the latest vLLM master ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ak when using CUDA Graph with torch.distributed.all_reduce (vLLM default config) bug Running the following on the latest vLLM master ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: uted.all_reduce (vLLM default config) bug Running the following on the latest vLLM master ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 8 --max-num-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: k_ray.py --model "mistralai/Mixtral-8x7B-Instruct-v0.1" --num-concurrent-requests 192 --max-num-completed-requests 100000 --timeout 3600 ``` (you will need to apply the following patch to avoid 400 errors: ``` diff --gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
