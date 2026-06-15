# vllm-project/vllm#891: Nos of input passed does not matches with the output

| 字段 | 值 |
| --- | --- |
| Issue | [#891](https://github.com/vllm-project/vllm/issues/891) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Nos of input passed does not matches with the output

### Issue 正文摘录

I am using model **lmsys/vicuna-7b-v1.5**, but I am not getting a proper response. i.e. on passing 3 input prompts to the model with two prompts such that it exceeds the model's supported length. I am expecting vLLM to return 3 outputs from the model, but actually getting just 2 responses. We cannot map the response to the correct output if the order is not maintained. I also tried different combinations where the input prompt length exceeded the permissible limit, a similar response was observed there. As vLLM does not do truncation of the input, but actually it drops the request [#447](https://github.com/vllm-project/vllm/issues/447#issuecomment-1639571226), I believe in that case vLLM should return " " as an output. In some cases, we are getting an empty string as output, and in some cases, we don't. Can this be fixed? ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name = "lmsys/vicuna-7b-v1.5" tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, use_fast=True, ) llm = LLM(model=model_name, trust_remote_code = True, tensor_parallel_size=1, max_num_batched_tokens=4096 ) sampling_params = SamplingParams(max_tokens=10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and in some cases, we don't. Can this be fixed? ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name = "lmsys/vicuna-7b-v1.5" tokenizer = AutoTokenizer.from_pretrained(model_name, t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nse(text): outputs = llm.generate(text, sampling_params, use_tqdm=False) response = [] # Print the outputs. for output in outputs: response.append(output.outputs[0].text) return response prompt_list = [ " ", # Input tok...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Nos of input passed does not matches with the output I am using model **lmsys/vicuna-7b-v1.5**, but I am not getting a proper response. i.e. on passing 3 input prompts to the model with two prompts such that it exceeds...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . As vLLM does not do truncation of the input, but actually it drops the request [#447](https://github.com/vllm-project/vllm/issues/447#issuecomment-1639571226), I believe in that case vLLM should return " " as an outpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
