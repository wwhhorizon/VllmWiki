# vllm-project/vllm#1673: llm.generate hangs for long prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#1673](https://github.com/vllm-project/vllm/issues/1673) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> llm.generate hangs for long prompt

### Issue 正文摘录

I'm using the latest vllm (0.2.1.post1) and `TheBloke/vicuna-13B-v1.5-16K-AWQ` model and it seems that llm.generate will hang when the length of prompt token ids >= 5985. ``` from vllm import LLM, SamplingParams llm = LLM(model="TheBloke/vicuna-13B-v1.5-16K-AWQ", quantization="awq") tokenizer = llm.get_tokenizer() prompt1 = "xxx..." print(len(tokenizer.encode(prompt1))) # 5984 sampling_params = SamplingParams(temperature=0.8, top_p=0.95) outputs = llm.generate([prompt1], sampling_params) Processed prompts: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:04<00:00, 4.92s/it] prompt2 = prompt1 + "\n" print(len(tokenizer.encode(prompt2))) # 5985 outputs = llm.generate([prompt2], sampling_params) Processed prompts: 0%| | 0/1 [00:00<?, ?it/s] ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: te will hang when the length of prompt token ids >= 5985. ``` from vllm import LLM, SamplingParams llm = LLM(model="TheBloke/vicuna-13B-v1.5-16K-AWQ", quantization="awq") tokenizer = llm.get_tokenizer() prompt1 = "xxx.....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: LLM, SamplingParams llm = LLM(model="TheBloke/vicuna-13B-v1.5-16K-AWQ", quantization="awq") tokenizer = llm.get_tokenizer() prompt1 = "xxx..." print(len(tokenizer.encode(prompt1))) # 5984 sampling_params = SamplingParam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing the latest vllm (0.2.1.post1) and `TheBloke/vicuna-13B-v1.5-16K-AWQ` model and it seems that llm.generate will hang when the length of prompt token ids >= 5985. ``` from vllm import LLM, SamplingParams llm = LLM(mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: llm.generate hangs for long prompt bug I'm using the latest vllm (0.2.1.post1) and `TheBloke/vicuna-13B-v1.5-16K-AWQ` model and it seems that llm.generate will hang when the length of prompt token ids >= 5985. ``` from...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
