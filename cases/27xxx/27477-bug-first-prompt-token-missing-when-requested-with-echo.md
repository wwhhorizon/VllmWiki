# vllm-project/vllm#27477: [Bug]: First prompt token missing when requested with "echo"

| 字段 | 值 |
| --- | --- |
| Issue | [#27477](https://github.com/vllm-project/vllm/issues/27477) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: First prompt token missing when requested with "echo"

### Issue 正文摘录

### Your current environment vllm installed from main: `vllm 0.11.1rc3.dev23+g61089465a.precompiled` ### 🐛 Describe the bug Is it expected behavior that echo isn't returning the first token of the prompt? I am trying to collect exact prompt_token_ids which went into the model served with vllm serve , so I am doing this: ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve openai/gpt-oss-20b -tp 1 --enforce-eager --return-tokens-as-token-ids --enable-log-requests --enable-prompt-tokens-details ``` and with this snippet: ```python from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1" ) messages = [ {"role": "user", "content": "Continue: The quick brown fox"}, ] response = client.chat.completions.create( model="openai/gpt-oss-20b", messages=messages, temperature=0.0, max_tokens=1024, logprobs=True, extra_body={ "echo": True, } ) print(response.model_extra['prompt_logprobs']) ``` I am seeing: `[None, 17360, 200008, ...]` whereas the vllm server logs are printing this: `[200006, 17360, 200008, ...]` which is correct as the first token is and should be `200006` == ` ` . Not sure why is it `None` in the ChatCompletion object ### Before submitting a new is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: issing when requested with "echo" bug ### Your current environment vllm installed from main: `vllm 0.11.1rc3.dev23+g61089465a.precompiled` ### 🐛 Describe the bug Is it expected behavior that echo isn't returning the fir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rompt? I am trying to collect exact prompt_token_ids which went into the model served with vllm serve , so I am doing this: ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve openai/gpt-oss-20b -tp 1 --enforce-eager --return-t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ect ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: First prompt token missing when requested with "echo" bug ### Your current environment vllm installed from main: `vllm 0.11.1rc3.dev23+g61089465a.precompiled` ### 🐛 Describe the bug Is it expected behavior that e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
