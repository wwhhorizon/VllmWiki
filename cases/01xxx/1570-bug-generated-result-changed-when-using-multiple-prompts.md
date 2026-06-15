# vllm-project/vllm#1570: [Bug] generated result changed when using multiple prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#1570](https://github.com/vllm-project/vllm/issues/1570) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] generated result changed when using multiple prompts

### Issue 正文摘录

branch: main commit: 8516999495114926c9838c2d6e0feb580d4d983f test gpu: Nvidia A10 test code: ```python from vllm import LLM, SamplingParams prompts = [ "Quartz is one of the most common", "Building a successful software platform is", # "Justice studies is an", # "In 1997 Ronald Phillips published", ] model_path = "huggyllama/llama-7b" llm = LLM(model=model_path) sampling_params = SamplingParams(max_tokens=128, temperature=0) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"[Prompt]\n{prompt}\n\n") print(f"[Generated text]\n{generated_text}\n\n") ``` result: ```text [Prompt] Quartz is one of the most common [Generated text] most abundant minerals on Earth. It is found in many different colors and is used in many different ways. Quartz is a crystalline mineral that is found in many different colors. It is a very common mineral and is found in many different places. Quartz is a very common mineral and is found in many different places. Quartz is a mineral that is found in many different colors. It is a very common mineral and is found in many different places. Quartz is a very common minera...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: c2d6e0feb580d4d983f test gpu: Nvidia A10 test code: ```python from vllm import LLM, SamplingParams prompts = [ "Quartz is one of the most common", "Building a successful software platform is", # "Justice studies is an",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: any different forms, including crystals, amethyst, rose quartz, citrine, smoky quartz, and rock [Prompt] Building a successful software platform is [Generated text] . Building a successful software platform is. Building...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ustice studies is an", # "In 1997 Ronald Phillips published", ] model_path = "huggyllama/llama-7b" llm = LLM(model=model_path) sampling_params = SamplingParams(max_tokens=128, temperature=0) outputs = llm.generate(promp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rompts bug branch: main commit: 8516999495114926c9838c2d6e0feb580d4d983f test gpu: Nvidia A10 test code: ```python from vllm import LLM, SamplingParams prompts = [ "Quartz is one of the most common", "Building a success...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
