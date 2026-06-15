# vllm-project/vllm#11783: [Bug]: Continuing a generation is not deterministic

| 字段 | 值 |
| --- | --- |
| Issue | [#11783](https://github.com/vllm-project/vllm/issues/11783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Continuing a generation is not deterministic

### Issue 正文摘录

I know there are many determinism issues in this repo already but they looked different so opening this one; sorry if it is a duplicate. If there is any way I can make the below be the same, I'd appreciate it! It may look like a small difference but snowballs into very large differences. ```python from transformers import AutoTokenizer tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-32B-Instruct") from vllm import LLM, SamplingParams model = LLM("Qwen/Qwen2.5-32B-Instruct", tensor_parallel_size=2) prompt = "Let $x,y$ and $z$ be positive real numbers that satisfy the following system of equations: \n\\[\\log_2\\left({x \\over yz}\\right) = {1 \\over 2}\\]\n\\[\\log_2\\left({y \\over xz}\\right) = {1 \\over 3}\\]\n\\[\\log_2\\left({z \\over xy}\\right) = {1 \\over 4}\\]\nThen the value of $\\left|\\log_2(x^4y^3z^2)\\right|$ is $\\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$." prompt = " system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant. \n user\n" + prompt + " \n assistant\n" prompt_token_ids = tok.encode(prompt, add_special_tokens=False) sampling_params = SamplingParams(temperature=0, max_tokens=32000, skip_special_to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: uplicate. If there is any way I can make the below be the same, I'd appreciate it! It may look like a small difference but snowballs into very large differences. ```python from transformers import AutoTokenizer tok = Au...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m transformers import AutoTokenizer tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-32B-Instruct") from vllm import LLM, SamplingParams model = LLM("Qwen/Qwen2.5-32B-Instruct", tensor_parallel_size=2) prompt = "Let $x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Continuing a generation is not deterministic bug;stale I know there are many determinism issues in this repo already but they looked different so opening this one; sorry if it is a duplicate. If there is any way...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: assistant\n" prompt_token_ids = tok.encode(prompt, add_special_tokens=False) sampling_params = SamplingParams(temperature=0, max_tokens=32000, skip_special_tokens=False) out1 = model.generate(prompt_token_ids=prompt_tok...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Continuing a generation is not deterministic bug;stale I know there are many determinism issues in this repo already but they looked different so opening this one; sorry if it is a duplicate. If there is any way...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
