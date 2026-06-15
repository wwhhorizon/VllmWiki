# vllm-project/vllm#2227: mistralai/Mistral-7B-Instruct-v0.2 throws error, why?

| 字段 | 值 |
| --- | --- |
| Issue | [#2227](https://github.com/vllm-project/vllm/issues/2227) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> mistralai/Mistral-7B-Instruct-v0.2 throws error, why?

### Issue 正文摘录

code ```python # - Test model def test_model(): """ top_p := vocab frac used until the prob of vocab is top_p temp := score/temp so 0 is deterministic. """ from vllm import LLM, SamplingParams import torch sampling_params = SamplingParams(temperature=1.0, top_p=1.0) # llm = LLM(model="mistralai/Mixtral-8x7B-Instruct-v0.1") # llm = LLM(model="mistralai/Mixtral-8x7B-Instruct-v0.1", dtype=torch.bfloat16) llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.2", dtype=torch.bfloat16) # llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1", dtype=torch.bfloat16) output = llm.generate("Hello, my name is") print(output) if __name__ == '__main__': test_model() print('Done!\a') ``` error was too many re-tries to get model? ```python Exception has occurred: ConnectTimeout (MaxRetryError("HTTPSConnectionPool(host='cdn-lfs-us-1.huggingface.co', port=443): Max retries exceeded with url: /repos/25/f2/25f242d117fa40b7cc0b5e85e97135c923bc5665bde4204e7fabadb99a561eab/5f86e15cb3ed9078e30ae6e72445e109d0e337d9cde59b9aeea4ce8e44e54a5d?response-content-disposition=attachment%3B+filename*%3DUTF-8%27%27model-00003-of-00003.safetensors%3B+filename%3D%22model-00003-of-00003.safetensors%22%3B&Expires=1703395913&...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uct-v0.1") # llm = LLM(model="mistralai/Mixtral-8x7B-Instruct-v0.1", dtype=torch.bfloat16) llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.2", dtype=torch.bfloat16) # llm = LLM(model="mistralai/Mistral-7B-Instruct-v0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: TuVB11Ers6fC9z3VUcy62O9WRgBxhk-WOf9Mz85iiwGKAr7LMqstpzIHynqYU1e7s7qczbL8iSmOTMFMV-bdfTTLgMDH8xsPYbs28SfltQoGv7G3Hqm3YxLQE~tu9oI30EDF2SbofB1Biar74yvjQNyzVLD1-07b1EYFZOWhcJMlw__&Key-Pair-Id=KCD77M1F0VK2B (Caused by Connec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: alai/Mistral-7B-Instruct-v0.2 throws error, why? code ```python # - Test model def test_model(): """ top_p := vocab frac used until the prob of vocab is top_p temp := score/temp so 0 is deterministic. """ from vllm impo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mistralai/Mistral-7B-Instruct-v0.2 throws error, why? code ```python # - Test model def test_model(): """ top_p := vocab frac used until the prob of vocab is top_p temp := score/temp so 0 is deterministic. """ from vllm...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rac used until the prob of vocab is top_p temp := score/temp so 0 is deterministic. """ from vllm import LLM, SamplingParams import torch sampling_params = SamplingParams(temperature=1.0, top_p=1.0) # llm = LLM(model="m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
