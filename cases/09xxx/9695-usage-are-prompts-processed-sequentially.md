# vllm-project/vllm#9695: [Usage]: Are prompts processed sequentially?

| 字段 | 值 |
| --- | --- |
| Issue | [#9695](https://github.com/vllm-project/vllm/issues/9695) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Are prompts processed sequentially?

### Issue 正文摘录

### Your current environment ```text Running `python collect_env.py` throws this error: ``` Collecting environment information... Traceback (most recent call last): File "path/collect_env.py", line 743, in main() File patcollect_env.py", line 722, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "path/collect_env.py", line 717, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "path/collect_env.py", line 549, in get_env_info vllm_version = get_vllm_version() ^^^^^^^^^^^^^^^^^^ File "path/collect_env.py", line 270, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version_tuple__' from 'vllm' (/path/lib/python3.11/site-packages/vllm/__init__.py) ### How would you like to use vllm I am running Llama 3 8B Instruct using vLLM as follows: ``` llm = LLM(model=config.model, max_logprobs=1000) sampling_params = SamplingParams(temperature=config.temperature, max_tokens=config.max_tokens, n=1, stop=config.stop_strings, logprobs=config.logprobs, skip_special_tokens=config.skip_special_tokens, top_k=config.top_k ) outputs = llm.generate(prompts, sampling_params) ``` In the output, I notice this: `...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `python collect_env.py` throws this error: ``` Collecting environment information... Traceback (most recent call last): File "path/collect_env.py", line 743, in main() File patcollect_env.py", line 722, in main output =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ^^^^^^^ File "path/collect_env.py", line 549, in get_env_info vllm_version = get_vllm_version() ^^^^^^^^^^^^^^^^^^ File "path/collect_env.py", line 270, in get_vllm_version from vllm import __version__, __version_tuple_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Are prompts processed sequentially? usage;stale ### Your current environment ```text Running `python collect_env.py` throws this error: ``` Collecting environment information... Traceback (most recent call last...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
