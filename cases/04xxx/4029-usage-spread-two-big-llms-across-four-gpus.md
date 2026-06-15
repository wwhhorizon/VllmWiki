# vllm-project/vllm#4029: [Usage]: Spread two big LLMs across four GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#4029](https://github.com/vllm-project/vllm/issues/4029) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Spread two big LLMs across four GPUs

### Issue 正文摘录

### Your current environment This is about API usage rather than an environment issue. ### How would you like to use vllm I want to run batch inference using two models in the same process and spread them across distinct GPUs. Here's an example code snippet i've been trying to figure out how to get correct: ```python from vllm import LLM llm1 = LLM( model="meta-llama/Llama-2-70b-hf", tensor_parallel_size=2 ) llm2 = LLM( model="CohereForAI/c4ai-command-r-v01", tensor_parallel_size=2, ) ``` In this scenario, if I have 4 A100 80Gs on a single node, I should be able to fit model one on GPUs 1 and 2, then fit model two on GPUs 3 and 4. I was hoping that Ray's backend would get this right but instead this doesn't work. I typically run out of vRAM. Is there a way to configure two `LLM` instances such that they work on distinct subsets of my available GPUs all while running the same process? Do I need to use `device` right?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: How would you like to use vllm I want to run batch inference using two models in the same process and spread them across distinct GPUs. Here's an example code snippet i've been trying to figure out how to get correct: `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Us 1 and 2, then fit model two on GPUs 3 and 4. I was hoping that Ray's backend would get this right but instead this doesn't work. I typically run out of vRAM. Is there a way to configure two `LLM` instances such that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i've been trying to figure out how to get correct: ```python from vllm import LLM llm1 = LLM( model="meta-llama/Llama-2-70b-hf", tensor_parallel_size=2 ) llm2 = LLM( model="CohereForAI/c4ai-command-r-v01", tensor_parall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r-v01", tensor_parallel_size=2, ) ``` In this scenario, if I have 4 A100 80Gs on a single node, I should be able to fit model one on GPUs 1 and 2, then fit model two on GPUs 3 and 4. I was hoping that Ray's backend woul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
