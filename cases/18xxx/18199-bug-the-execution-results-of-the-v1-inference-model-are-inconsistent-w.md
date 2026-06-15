# vllm-project/vllm#18199: [Bug]: The execution results of the v1 inference model are inconsistent with those of v0 and transformers.

| 字段 | 值 |
| --- | --- |
| Issue | [#18199](https://github.com/vllm-project/vllm/issues/18199) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: The execution results of the v1 inference model are inconsistent with those of v0 and transformers.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Just as described in the bug reported at [https://github.com/vllm-project/vllm/issues/18141](https://github.com/vllm-project/vllm/issues/18141), I found that the execution result of the example code for phi-4-reasoning-plus when run with transformers includes the tags. When I switched the vLLM engine back to v0 (VLLM\_USE\_V1=0), I found that its execution result also included the tags. However, vLLM v1 does not output the tags. This ultimately leads to the model's execution result not being correctly divided into reasoning\_content and content. After running it multiple times, the execution results are consistently like this. I have reason to believe that Microsoft has specifically trained this CoT model such that even if the chat\_template does not explicitly include , the model can still correctly generate as its first token. This is my transformers test code: ```python from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-reasoning-plus") model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-reasoning-plus", device_map="auto", torch_dtype="auto") messag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: consistently like this. I have reason to believe that Microsoft has specifically trained this CoT model such that even if the chat\_template does not explicitly include , the model can still correctly generate as its fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: inference model are inconsistent with those of v0 and transformers. bug;stale ### Your current environment ### 🐛 Describe the bug Just as described in the bug reported at [https://github.com/vllm-project/vllm/issues/181...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The execution results of the v1 inference model are inconsistent with those of v0 and transformers. bug;stale ### Your current environment ### 🐛 Describe the bug Just as described in the bug reported at [https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: still correctly generate as its first token. This is my transformers test code: ```python from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-reasoning...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
