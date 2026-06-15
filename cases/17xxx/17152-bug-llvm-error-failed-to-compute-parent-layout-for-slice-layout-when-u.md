# vllm-project/vllm#17152: [Bug]: LLVM ERROR: Failed to compute parent layout for slice layout. when using fp16

| 字段 | 值 |
| --- | --- |
| Issue | [#17152](https://github.com/vllm-project/vllm/issues/17152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLVM ERROR: Failed to compute parent layout for slice layout. when using fp16

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is my demo code: ```python import json import torch from vllm import LLM, SamplingParams from datasets import load_dataset dataset = load_dataset("HuggingFaceH4/MATH-500", split="test") problems = [example["problem"] for example in dataset] answers = [example["answer"] for example in dataset] problem = problems[0] answer = answers[0] print(f"\n\n\nThe problem is: {problem}\n\n\n") prompt = f""" You are a math expert. Please solve the following problem: {problem}. put your reasoning process in and tags. That is when you start thinking about the problem. You should generate first, then generate your thinking, then generate when you stop thinking. Finally, put your answer between and tags. No more words after tags. """ sampling_params = SamplingParams( temperature=0.3, top_p=0.95, min_tokens=100, max_tokens=4096, ) llm = LLM( model="Qwen/QwQ-32B", dtype="half", tensor_parallel_size=torch.cuda.device_count(), ) outputs = llm.generate(prompt, sampling_params) # Prepare results for JSON results = [] for output in outputs: result = { "problem": output.prompt, "generated_solution": output.outputs[0].text, "answer": answer, } results...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: environment ### 🐛 Describe the bug This is my demo code: ```python import json import torch from vllm import LLM, SamplingParams from datasets import load_dataset dataset = load_dataset("HuggingFaceH4/MATH-500", split="...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: amplingParams from datasets import load_dataset dataset = load_dataset("HuggingFaceH4/MATH-500", split="test") problems = [example["problem"] for example in dataset] answers = [example["answer"] for example in dataset]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model="Qwen/QwQ-32B", dtype="half", tensor_parallel_size=torch.cuda.device_count(), ) outputs = llm.generate(prompt, sampling_params) # Prepare results for JSON results = [] for output in outputs: result = { "problem":...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: (f"\n\n\nThe problem is: {problem}\n\n\n") prompt = f""" You are a math expert. Please solve the following problem: {problem}. put your reasoning process in and tags. That is when you start thinking about the problem. Y...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: are_porting;model_support;moe;sampling_logits cuda;moe;operator;sampling;triton build_error dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
