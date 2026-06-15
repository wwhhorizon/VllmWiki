# vllm-project/vllm#23905: [Bug]: gpt-oss-120b has high possibility to generate response as part of reasoning by using vllm v0.10.1

| 字段 | 值 |
| --- | --- |
| Issue | [#23905](https://github.com/vllm-project/vllm/issues/23905) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-120b has high possibility to generate response as part of reasoning by using vllm v0.10.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug By using following prompt, there is a high possibility that gpt-oss-120b generates response in "reasoning_content" field instead of "content" field. vllm in use is v0.10.1. Following is one generation example: ``` 2025-08-29 06:48:01,084 [MainThread - INFO ] reasoning_response_str=We need to generate code to calculate 2*3. We can just compute and print. Then final_answer. We should produce python code block with calculation, print result. Then final answer likely the result 6. Use final_answer tool. So steps: compute result = 2*3, print(result). Then final_answer(answer=result).We will compute the product and output it.```python \`\`\`Now call final_answer.\`\`\`python final_answer(answer=result) \`\`\` 2025-08-29 06:48:01,086 [MainThread - INFO ] response_str= ' sequence. During each intermediate step, you can use 'print()' to save whatever important information you will then need. In the end you have to return a final answer using the `final_answer` tool. On top of performing computations in the Python code snippets that you create, you only have access to these tools, behaving like regular python functions: ```python def get_j...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lity to generate response as part of reasoning by using vllm v0.10.1 bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug By using following prompt, there is a high possibility that gpt-oss-120b generat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e. During each intermediate step, you can use 'print()' to save whatever important information you will then need. In the end you have to return a final answer using the `final_answer` tool. On top of performing computa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss-120b has high possibility to generate response as part of reasoning by using vllm v0.10.1 bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug By using following prompt, there is a high p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ially when the output format is unpredictable. For instance, a call to search has an unpredictable return format, so do not have another tool call that depends on its output in the same block: rather output results with...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ust compute and print. Then final_answer. We should produce python code block with calculation, print result. Then final answer likely the result 6. Use final_answer tool. So steps: compute result = 2*3, print(result)....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
