# vllm-project/vllm#14280: [Bug]: V1 still sample n=1 when set n>1 in samplingparam

| 字段 | 值 |
| --- | --- |
| Issue | [#14280](https://github.com/vllm-project/vllm/issues/14280) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 still sample n=1 when set n>1 in samplingparam

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer import pandas as pd import os os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" llm = LLM(model="/yijian/hf_models/deepseek-ai__DeepSeek-R1-Distill-Qwen-32B", enable_prefix_caching=True, max_model_len=4096, tensor_parallel_size=2, gpu_memory_utilization=0.8) out = llm.generate( ['Hello'], SamplingParams(n=10, temperature=0.6, top_p=1, repetition_penalty=1.05, max_tokens=30)) print(out) ``` Expect sample 10 outputs, but only 1 response in RequestOutput ```print [RequestOutput(request_id=0, prompt='Hello', prompt_token_ids=[151646, 9707], encoder_prompt=None, encoder_prompt_token_ids=None, prompt_logprobs=None, outputs=[CompletionOutput(index=0, text="! I'm DeepSeek-R1, an artificial intelligence assistant created by DeepSeek. For comprehensive details about our models and products, we invite you to", token_ids=[0, 358, 2776, 18183, 39350, 10911, 16, 11, 458, 20443, 11229, 17847, 3465, 553, 18183, 39350, 13, 1752, 15817, 3565, 911, 1039, 4119, 323, 3871, 11, 582, 21399, 498, 311], cumulative_logprob=None, logprob...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer import pandas as pd import os os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_WORKER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: "] = "1" os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" llm = LLM(model="/yijian/hf_models/deepseek-ai__DeepSeek-R1-Distill-Qwen-32B", enable_prefix_caching=True, max_model_len=4096, tensor_parallel_size=2, gpu_me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: V1 still sample n=1 when set n>1 in samplingparam bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer import pandas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ar;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
