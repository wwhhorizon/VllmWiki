# vllm-project/vllm#2255: When we loaded chatglm2 with vllm, the output became garbled.

| 字段 | 值 |
| --- | --- |
| Issue | [#2255](https://github.com/vllm-project/vllm/issues/2255) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When we loaded chatglm2 with vllm, the output became garbled.

### Issue 正文摘录

I tested this code with the input question "请你列举20条关于零点不好的建议", but I didn't get a normal output? ``` def test_vllm(prompts): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGLM2_6B, trust_remote_code=True, tensor_parallel_size=4, gpu_memory_utilization=0.6, enforce_eager=True ) sampling_params = SamplingParams(n=1, temperature=0.6, max_tokens=8129) for i, p in enumerate(prompts): p = llm.get_tokenizer().build_prompt(p) print(p) prompts[i] = p responses = llm.generate(prompts, sampling_params=sampling_params) def process_response(response): response = response.strip() response = response.replace("[[训练时间]]", "2023年") return response # print(responses) for i, response in enumerate(responses): response = process_response(response.outputs[0].text) print(repr(response)) ``` The output of the above code is ``` 答： Processed prompts: 100%|██████████████████████████| 2/2 [00:02<00:00, 1.42s/it] 'L 1. 000000000000000\n\n\n11500000000000001\n\n\n\n0\n0\n\n\n\n\n灭' ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: I didn't get a normal output? ``` def test_vllm(prompts): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGLM2_6B, trust_remote_code=True, tensor_parallel_size=4, gpu_mem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ompts): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGLM2_6B, trust_remote_code=True, tensor_parallel_size=4, gpu_memory_utilization=0.6, enforce_eager=True ) sampling...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: When we loaded chatglm2 with vllm, the output became garbled. I tested this code with the input question "请你列举20条关于零点不好的建议", but I didn't get a normal output? ``` def test_vllm(prompts): from vllm import LLM, SamplingPa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
