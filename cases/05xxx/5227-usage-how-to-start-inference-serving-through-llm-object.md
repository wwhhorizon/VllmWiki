# vllm-project/vllm#5227: [Usage]: How to start inference serving through `LLM` object

| 字段 | 值 |
| --- | --- |
| Issue | [#5227](https://github.com/vllm-project/vllm/issues/5227) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to start inference serving through `LLM` object

### Issue 正文摘录

### Your current environment Irrelevant ### How would you like to use vllm I'm working on a project that involves performing multi-turn model evaluations during model training. The majority of these evaluation scripts are all based on the OpenAI API format. It would be really helpful if I could start and stop the vllm OpenAI-compatible inference server programmatically, instead of using the command line. Here is a snippet illustrating what I want to do: ```python llm = LLM(model=model) llm.serve(port_num, **serve_args) # Start serving results = [] # In reality, we would call complex_eval in parallel for i in range(num_evals): results.append(complex_eval(i, port_num)) llm.stop() # Stop serving ``` I am new to `vllm` and am curious if there is a built-in way to achieve this. If not, how challenging would it be to implement this functionality ourselves?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o use vllm I'm working on a project that involves performing multi-turn model evaluations during model training. The majority of these evaluation scripts are all based on the OpenAI API format. It would be really helpfu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vllm I'm working on a project that involves performing multi-turn model evaluations during model training. The majority of these evaluation scripts are all based on the OpenAI API format. It would be really helpful if I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
