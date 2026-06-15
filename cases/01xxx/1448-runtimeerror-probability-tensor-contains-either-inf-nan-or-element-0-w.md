# vllm-project/vllm#1448: “RuntimeError: probability tensor contains either `inf`, `nan` or element < 0” when use llama2-70B 

| 字段 | 值 |
| --- | --- |
| Issue | [#1448](https://github.com/vllm-project/vllm/issues/1448) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> “RuntimeError: probability tensor contains either `inf`, `nan` or element < 0” when use llama2-70B 

### Issue 正文摘录

When I use llama2-70B and set 'tensor_parallel_size=8' get “RuntimeError: probability tensor contains either `inf`, `nan` or element < 0”, but when I use same code but replace model to gpt-neox or llama2-7B it work. When I use llama2-70B but set 'tensor_parallel_size=4' it also work. And I use 8xA100 for my experiment. Can someone give me any ideas about llama2-70B? Here is my code: ```python from vllm import LLM, SamplingParams import torch prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0, max_tokens=300) model_dir = "../llama70B" llm = LLM(model=model_dir, trust_remote_code=True, tensor_parallel_size=8) outputs = llm.generate(prompts, sampling_params) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: probability tensor contains either `inf`, `nan` or element < 0” when use llama2-70B When I use llama2-70B and set 'tensor_parallel_size=8' get “RuntimeError: probability tensor contains either `inf`, `nan` or element <...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ve me any ideas about llama2-70B? Here is my code: ```python from vllm import LLM, SamplingParams import torch prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e llama2-70B but set 'tensor_parallel_size=4' it also work. And I use 8xA100 for my experiment. Can someone give me any ideas about llama2-70B? Here is my code: ```python from vllm import LLM, SamplingParams import torc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
