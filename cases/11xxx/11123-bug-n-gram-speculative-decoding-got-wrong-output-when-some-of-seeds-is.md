# vllm-project/vllm#11123: [Bug]: N-gram speculative decoding got wrong output when some of seeds is None in a batch 

| 字段 | 值 |
| --- | --- |
| Issue | [#11123](https://github.com/vllm-project/vllm/issues/11123) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: N-gram speculative decoding got wrong output when some of seeds is None in a batch 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams prompt=""" user\n你是一个assistant，给定一个query，按json格式返回query，例如query是今天天气怎么样，你的返回格式为{ "query": "今天天气怎么样"} ，当前query是：煎饼果子怎么做\n \n assistant\n""" prompts = [prompt, prompt] sampling_params = [SamplingParams(temperature=0.7, seed=42), SamplingParams(temperature=0.7, seed=None)] llm = LLM(model="Qwen/Qwen1.5-MoE-A2.7B-Chat", tensor_parallel_size=2, num_speculative_tokens=5, ngram_prompt_lookup_max=4, speculative_model="[ngram]", trust_remote_code=True) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` The outputs are The second output is totally wrong. However when set all seeds to None or set all seeds to 42, we got correct outputs: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams prompt=""" user\n你是一个assistant，给定一个query，按json格式返回query，例如query是今天天气怎么样，你的返回格式为{ "query": "今天天气怎么样"} ，当前query是：煎饼果子怎么做\n \n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: seeds is None in a batch bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams prompt=""" user\n你是一个assistant，给定一个query，按json格式返...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: N-gram speculative decoding got wrong output when some of seeds is None in a batch bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;triton build_error;mismatch env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
