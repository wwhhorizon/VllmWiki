# vllm-project/vllm#27381: [Bug]: concurrent generation hangs in external_launcher model

| 字段 | 值 |
| --- | --- |
| Issue | [#27381](https://github.com/vllm-project/vllm/issues/27381) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: concurrent generation hangs in external_launcher model

### Issue 正文摘录

### Your current environment vllm=0.8.5.post1 ### 🐛 Describe the bug reproduce code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", ] model="xxx" sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model=model, tensor_parallel_size=8, distributed_executor_backend="external_launcher", seed=0, enforce_eager=False, disable_custom_all_reduce=True, skip_tokenizer_init=False, enable_prefix_caching=True, ) from concurrent.futures import ThreadPoolExecutor def task(name): outputs = llm.generate(prompts, sampling_params) # all ranks will have the same outputs for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Task {name} Prompt: {prompt!r}\n" f"Task {name} Generated text: {generated_text!r}") return f"Task {name} is done" with ThreadPoolExecutor(max_workers=5) as executor: results = executor.map(task, list(range(5))) for result in results: print(result) ``` Executing it via ``torchrun --nproc-per-node=8 torchrun_example.py`` and it hangs. Is this a bug or expected? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: g ### Your current environment vllm=0.8.5.post1 ### 🐛 Describe the bug reproduce code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", ] model="xxx...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: M( model=model, tensor_parallel_size=8, distributed_executor_backend="external_launcher", seed=0, enforce_eager=False, disable_custom_all_reduce=True, skip_tokenizer_init=False, enable_prefix_caching=True, ) from concur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0.8.5.post1 ### 🐛 Describe the bug reproduce code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", ] model="xxx" sampling_params = SamplingParams(t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ed_executor_backend="external_launcher", seed=0, enforce_eager=False, disable_custom_all_reduce=True, skip_tokenizer_init=False, enable_prefix_caching=True, ) from concurrent.futures import ThreadPoolExecutor def task(n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
