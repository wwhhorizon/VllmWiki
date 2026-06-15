# vllm-project/vllm#987: Why is num_prompts set to 1000?

| 字段 | 值 |
| --- | --- |
| Issue | [#987](https://github.com/vllm-project/vllm/issues/987) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why is num_prompts set to 1000?

### Issue 正文摘录

On A100 80G, when I set num_prompt to a larger value, the output displays better performance, as shown below. Why did the official documentation set num_prompt to 1000, and what is the significance of this setting? ![image](https://github.com/vllm-project/vllm/assets/70835312/d76d5dc2-02e3-4aa1-8e81-4ae4db2d9935)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the output displays better performance, as shown below. Why did the official documentation set num_prompt to 1000, and what is the significance of this setting? ![image](https://github.com/vllm-project/vllm/assets/70835...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Why is num_prompts set to 1000? On A100 80G, when I set num_prompt to a larger value, the output displays better performance, as shown below. Why did the official documentation set num_prompt to 1000, and what is the si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
