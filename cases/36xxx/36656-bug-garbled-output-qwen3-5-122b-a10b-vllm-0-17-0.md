# vllm-project/vllm#36656: [Bug]: Garbled output Qwen3.5-122B-A10B VLLM 0.17.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36656](https://github.com/vllm-project/vllm/issues/36656) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Garbled output Qwen3.5-122B-A10B VLLM 0.17.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi there, I am trying to do offline inference with the new qwen model and vllm 0.17.0. below is the core of my code. Despite changing much of the different variables (changed max_model_len, removed/added prefix caching/chunking, tried mtp, different sampling params, installed nightly version of vllm and used llm.generate with the tokenizer, and apply_chat_template), no matter what i do the output is garbled, also see below (output:text='with\n0:'). I have tried to follow the guide on vllm and info on huggingface page. Thanks for any help. ``` def build_messages(items: list[dict]) -> list[list[dict]]: """Build chat messages for each item. vLLM's llm.chat() handles the template.""" return [ [{"role": "user", "content": PROMPT_TEMPLATE.format(text=item["text"])}] for item in items ] import shutil import time from vllm import LLM, SamplingParams llm = LLM( model=MODEL, tensor_parallel_size=1, gpu_memory_utilization=0.95, max_model_len=2048, enable_prefix_caching=True, trust_remote_code=True, language_model_only=True, reasoning_parser="qwen3", performance_mode="throughput", ) # --- Sampling params --- sampling_params = SamplingParams(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ved/added prefix caching/chunking, tried mtp, different sampling params, installed nightly version of vllm and used llm.generate with the tokenizer, and apply_chat_template), no matter what i do the output is garbled, a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Garbled output Qwen3.5-122B-A10B VLLM 0.17.0 bug ### Your current environment ### 🐛 Describe the bug Hi there, I am trying to do offline inference with the new qwen model and vllm 0.17.0. below is the core of my...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: index=0, text='with\\n0:', token_ids=[4058, 198, 15, 25, 248046], routed_experts=None, cumulative_logprob=None, logprobs=None, finish_reason=stop, stop_reason=None)], finished=True, metrics=None, lora_request=None, num_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: l_only=True, reasoning_parser="qwen3", performance_mode="throughput", ) # --- Sampling params --- sampling_params = SamplingParams( temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_pena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
