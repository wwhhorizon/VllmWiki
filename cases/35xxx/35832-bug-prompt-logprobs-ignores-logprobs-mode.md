# vllm-project/vllm#35832: [Bug]: `prompt_logprobs` ignores `logprobs_mode`

| 字段 | 值 |
| --- | --- |
| Issue | [#35832](https://github.com/vllm-project/vllm/issues/35832) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `prompt_logprobs` ignores `logprobs_mode`

### Issue 正文摘录

### Your current environment ``` vLLM Version : 0.16.1rc1.dev148+g53700bf49 (git sha: 53700bf49) ``` ### 🐛 Describe the bug The [documentation](https://github.com/vllm-project/vllm/blob/c21d0039ecc85b06617034ff2166a1fb79309d53/vllm/config/model.py#L206-L213) of `logprobs_mode` states: `Indicates the content returned in the logprobs and prompt_logprobs.` However, it does not seem to apply to `prompt_logprobs`: ```python from vllm import LLM, SamplingParams def test(logprobs_mode: str): llm = LLM("facebook/opt-125m", logprobs_mode=logprobs_mode) (output,) = llm.generate("Hello", SamplingParams(max_tokens=1, prompt_logprobs=0)) return output.prompt_logprobs[1] print(test("raw_logits")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} print(test("raw_logprobs")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} print(test("processed_logits")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} print(test("processed_logprobs")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: robs` ignores `logprobs_mode` bug ### Your current environment ``` vLLM Version : 0.16.1rc1.dev148+g53700bf49 (git sha: 53700bf49) ``` ### 🐛 Describe the bug The [documentation](https://github.com/vllm-project/vllm/blob...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/c21d0039ecc85b06617034ff2166a1fb79309d53/vllm/config/model.py#L206-L213) of `logprobs_mode` states: `Indicates the content returned in the logprobs and prompt_logprobs.` However, it does not s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ("raw_logits")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} print(test("raw_logprobs")) # {31414: Logprob(logprob=-10.197416305541992, rank=636, decoded_token='Hello')} print(test("p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: `prompt_logprobs`: ```python from vllm import LLM, SamplingParams def test(logprobs_mode: str): llm = LLM("facebook/opt-125m", logprobs_mode=logprobs_mode) (output,) = llm.generate("Hello", SamplingParams(max_tokens=1,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
