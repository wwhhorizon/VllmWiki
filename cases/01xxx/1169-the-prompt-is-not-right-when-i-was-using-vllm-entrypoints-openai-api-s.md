# vllm-project/vllm#1169: The Prompt is not right when i was using vllm.entrypoints.openai.api_server

| 字段 | 值 |
| --- | --- |
| Issue | [#1169](https://github.com/vllm-project/vllm/issues/1169) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The Prompt is not right when i was using vllm.entrypoints.openai.api_server

### Issue 正文摘录

My local model is CodeLlama2-13b-hf ，when i use vllm by "python -m vllm.entrypoints.openai.api_server xxx" ，why the full prompt is : prompt: "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n### Human: Got any creative ideas for a 10 year old’s birthday?\n### Assistant: Of course! Here are some creative ideas for a 10-year-old's birthday party:\n1. Treasure Hunt: Organize a treasure hunt in your backyard or nearby park. Create clues and riddles for the kids to solve, leading them to hidden treasures and surprises.\n2. Science Party: Plan a science-themed party where kids can engage in fun and interactive experiments. You can set up different stations with activities like making slime, erupting volcanoes, or creating simple chemical reactions.\n3. Outdoor Movie Night: Set up a backyard movie night with a projector and a large screen or white sheet. Create a cozy seating area with blankets and pillows, and serve popcorn and snacks while the kids enjoy a favorite movie under the stars.\n4. DIY Crafts Party: Arrange a craft party where kids can unleash their creativity. Provide...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s not right when i was using vllm.entrypoints.openai.api_server My local model is CodeLlama2-13b-hf ，when i use vllm by "python -m vllm.entrypoints.openai.api_server xxx" ，why the full prompt is : prompt: "A chat betwee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he full prompt is : prompt: "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n### Human: Got any creative idea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
