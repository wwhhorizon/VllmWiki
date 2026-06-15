# vllm-project/vllm#831: Compatibility with togethercomputer/Llama-2-7B-32K-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#831](https://github.com/vllm-project/vllm/issues/831) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Compatibility with togethercomputer/Llama-2-7B-32K-Instruct

### Issue 正文摘录

Since it's a LLama V2 model I assumed them to be compatible, but it seems like the model doesn't behave correctly (nonsensical output, repeating symbols, nothing useful) when I run it with vLLM, in addition to the fact that it's impossible to run it sharded without downgrading certain pip packages (using the OpenAI version): `pip install typing-inspect==0.8.0 typing_extensions==4.5.0` <- This fixes the running issue, so I can run and shard it This is how I run the model: `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --model togethercomputer/Llama-2-7B-32K-Instruct --tensor-parallel-size 4 --download-dir /data` This is how I test it: ```python from langchain.llms import VLLMOpenAI llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="ip_address/v1", model_name="togethercomputer/Llama-2-7B-32K-Instruct", max_tokens=128, top_p=0.7, top_k=50, frequency_penalty=1.1, temperature=0.7 ) print(llm("[INST]\nWrite a poem about cats\n[/INST]\n\n")) ``` This produces a bunch of nonsensical output. When I run it with TGI with identical parameters, it works as expected and produces reasonable text. I tested it over multiple attempts to make sure it isn't a fluke....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: un it sharded without downgrading certain pip packages (using the OpenAI version): `pip install typing-inspect==0.8.0 typing_extensions==4.5.0` <- This fixes the running issue, so I can run and shard it This is how I ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Compatibility with togethercomputer/Llama-2-7B-32K-Instruct Since it's a LLama V2 model I assumed them to be compatible, but it seems like the model doesn't behave correctly (nonsensical output, repeating symbols, nothi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: multiple attempts to make sure it isn't a fluke. Could anyone test and reproduce, to make sure it isn't just something on my side?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: K-Instruct --tensor-parallel-size 4 --download-dir /data` This is how I test it: ```python from langchain.llms import VLLMOpenAI llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="ip_address/v1", model_name="tog...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
