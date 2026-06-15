# vllm-project/vllm#19337: [Bug]: mamba models don't seem to respect `max_model_len`

| 字段 | 值 |
| --- | --- |
| Issue | [#19337](https://github.com/vllm-project/vllm/issues/19337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mamba models don't seem to respect `max_model_len`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A few models with mamba layers I've tried don't seem to respect `max_model_len` passed into `LLM()` ```py from vllm import LLM, SamplingParams llm = LLM( #model="facebook/opt-125m", # ok: 20 model="nvidia/Nemotron-H-8B-Base-8K", # bad: 21 #model="meta-llama/Llama-3.1-8B-Instruct", # ok: 20 #model="meta-llama/Meta-Llama-3-8B", # ok: 20 #model="ibm-ai-platform/Bamba-9B-v1", # bad:21 max_model_len=20, # total tokens = prompt + generated trust_remote_code=True, ) prompt = "Hello, this is a test prompt." sampling_params = SamplingParams(max_tokens=20) outputs = llm.generate([prompt], sampling_params) for output in outputs: print(f"Prompt tokens: {len(output.prompt_token_ids)}") print(f"Generated tokens: {len(output.outputs[0].token_ids)}") print(f"Total tokens: {len(output.prompt_token_ids) + len(output.outputs[0].token_ids)}") ``` I expect to see `Total tokens: 20` for all of them, but `nvidia/Nemotron-H-8B-Base-8K` and `ibm-ai-platform/Bamba-9B-v1` both output 21, causing some off-by-one issues in downstream code. Is this expected? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n't seem to respect `max_model_len` passed into `LLM()` ```py from vllm import LLM, SamplingParams llm = LLM( #model="facebook/opt-125m", # ok: 20 model="nvidia/Nemotron-H-8B-Base-8K", # bad: 21 #model="meta-llama/Llama...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: mamba models don't seem to respect `max_model_len` bug ### Your current environment ### 🐛 Describe the bug A few models with mamba layers I've tried don't seem to respect `max_model_len` passed into `LLM()` ```py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
