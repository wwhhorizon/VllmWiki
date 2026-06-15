# vllm-project/vllm#34106: [Bug]: MLP Speculator AttributeError: 'MLPSpeculatorConfig' object has no attribute 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#34106](https://github.com/vllm-project/vllm/issues/34106) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MLP Speculator AttributeError: 'MLPSpeculatorConfig' object has no attribute 'num_attention_heads'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug MLP speculation using the `ibm-ai-platform/llama3-70b-accelerator` models seems to be broken. Attempting to run the following code using `method="mlp_speculator"` or `method="draft_model"` results in the following traceback: ```python3 from vllm import LLM, SamplingParams prompts = ["The future of AI is"] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="meta-llama/Meta-Llama-3.1-70B-Instruct", tensor_parallel_size=4, speculative_config={ "model": "ibm-ai-platform/llama3-70b-accelerator", "draft_tensor_parallel_size": 1, "method": "mlp_speculator", }, ) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ``` AttributeError: 'MLPSpeculatorConfig' object has no attribute 'num_attention_heads' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questi...

## 现有链接修复摘要

#34163 [Bug] Fix MLPSpeculatorConfig missing num_attention_heads attribute

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: "draft_model"` results in the following traceback: ```python3 from vllm import LLM, SamplingParams prompts = ["The future of AI is"] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="meta-l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: MLP Speculator AttributeError: 'MLPSpeculatorConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment ### 🐛 Describe the bug MLP speculation using the `ibm-ai-platform/llama3-7...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 'MLPSpeculatorConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment ### 🐛 Describe the bug MLP speculation using the `ibm-ai-platform/llama3-70b-accelerator` models seems to be bro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #34163 [Bug] Fix MLPSpeculatorConfig missing num_attention_heads attribute Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34163](https://github.com/vllm-project/vllm/pull/34163) | closes_keyword | 0.95 | [Bug] Fix MLPSpeculatorConfig missing num_attention_heads attribute | Fixes #34106 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
