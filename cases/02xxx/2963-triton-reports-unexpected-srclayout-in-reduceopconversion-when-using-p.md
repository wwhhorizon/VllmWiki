# vllm-project/vllm#2963: Triton reports "Unexpected srcLayout in ReduceOpConversion" when using prefix

| 字段 | 值 |
| --- | --- |
| Issue | [#2963](https://github.com/vllm-project/vllm/issues/2963) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Triton reports "Unexpected srcLayout in ReduceOpConversion" when using prefix

### Issue 正文摘录

code: ```python from vllm import LLM from vllm import SamplingParams import torch model = "01-ai/Yi-6B" # Create an LLM. llm = LLM(model=model,dtype=torch.float16) # get prompts prompts = ["这是一个 Prefix 功能使用的示例，因为 Prefix 的存储以物理块为单位，所以 Prompt 的长度需要至少大于等于一个物理块，这是第一句话", "这是一个 Prefix 功能使用的示例，因为 Prefix 的存储以物理块为单位，所以 Prompt 的长度需要至少大于等于一个物理块，这是第二句话"] # set SamplingParams sampling_params = SamplingParams(temperature=0, max_tokens=100, ) outputs = llm.generate(prompts=[prompts[0]], sampling_params=sampling_params, prefix_pos=[16]) outputs = llm.generate(prompts=[prompts[1]], sampling_params=sampling_params, prefix_pos=[16]) ``` output: ![QQ截图20240222002714](https://github.com/vllm-project/vllm/assets/52339737/5ab59d94-08f5-4fa7-aca3-559ccbdb7b30) environment: RTX6000 Linux cuda12.1 I have tried build vllm from source and just `pip install vllm`, but the result is the same. Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Triton reports "Unexpected srcLayout in ReduceOpConversion" when using prefix stale code: ```python from vllm import LLM from vllm import SamplingParams import torch model = "01-ai/Yi-6B" # Create an LLM. llm = LLM(mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: port torch model = "01-ai/Yi-6B" # Create an LLM. llm = LLM(model=model,dtype=torch.float16) # get prompts prompts = ["这是一个 Prefix 功能使用的示例，因为 Prefix 的存储以物理块为单位，所以 Prompt 的长度需要至少大于等于一个物理块，这是第一句话", "这是一个 Prefix 功能使用的示例，因为...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vllm/assets/52339737/5ab59d94-08f5-4fa7-aca3-559ccbdb7b30) environment: RTX6000 Linux cuda12.1 I have tried build vllm from source and just `pip install vllm`, but the result is the same. Thank you!
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Triton reports "Unexpected srcLayout in ReduceOpConversion" when using prefix stale code: ```python from vllm import LLM from vllm import SamplingParams import torch model = "01-ai/Yi-6B" # Create an LLM. llm = LLM(mode
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Triton reports "Unexpected srcLayout in ReduceOpConversion" when using prefix stale code: ```python from vllm import LLM from vllm import SamplingParams import torch model = "01-ai/Yi-6B" # Create an LLM. llm = LLM(mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
