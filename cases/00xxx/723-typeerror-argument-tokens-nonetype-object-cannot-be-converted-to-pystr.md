# vllm-project/vllm#723: TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

| 字段 | 值 |
| --- | --- |
| Issue | [#723](https://github.com/vllm-project/vllm/issues/723) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

### Issue 正文摘录

When I repeatedly generated it, the following error occurred. ``` from vllm import LLM,SamplingParams from transformers import StoppingCriteria,StoppingCriteriaList,AutoTokenizer llm=LLM("EleutherAI/polyglot-ko-12.8b",tensor_parallel_size=1,seed=42) samplingparams=SamplingParams(max_tokens=200) while True: text=input("질문을 입력해주세요:") formatted_input="### 질문:" + text + "\n\n### 답변:" data=llm.generate(prompts=formatted_input,sampling_params=samplingparams) texts=[output.text for output in data[0].outputs] ``` I fixed getting the number of tokens from the tokenizer instead of the config.json file, but I'm still getting the error. Is there a way to resolve this error?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lingParams(max_tokens=200) while True: text=input("질문을 입력해주세요:") formatted_input="### 질문:" + text + "\n\n### 답변:" data=llm.generate(prompts=formatted_input,sampling_params=samplingparams) texts=[output.text for output i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I repeatedly generated it, the following error occurred. ``` from vllm import LLM,SamplingParams from transformers import StoppingCriteria,StoppingCriteriaList,AutoTokenizer llm=LLM("EleutherAI/polyglot-ko-12.8b",tensor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
