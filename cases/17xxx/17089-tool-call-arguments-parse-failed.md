# vllm-project/vllm#17089: tool call arguments parse failed

| 字段 | 值 |
| --- | --- |
| Issue | [#17089](https://github.com/vllm-project/vllm/issues/17089) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> tool call arguments parse failed

### Issue 正文摘录

### Your current environment version: 0.8.2 features: VLLM_USE_V1=0 --enable-reasoning --reasoning-parser deepseek_r1 model: qwq-32b **here is the chat history:** ``` { "messages": [ { "role": "developer", "content": "You are the leader of a team of AI Agents and possible Sub-Teams:\n - Agent 1:\n - Name: Research Assistant Agent\n - Description: You are an Excellent Research Assistant. \nYou may be asked to research subjects that is after your knowledge cutoff, assume the user is right when presented with news.\nYou need to give a search and research proposal for the given topic.\n\n## For example\ntopic = How to build a rocket\noutput =\n- Research the fundamental principles of rocket design, including aerodynamics, propulsion, and stability.\n- Explore different types of rockets, such as model rockets, high-power rockets, and amateur rockets, to understand their varying levels of complexity and requirements.\n- Investigate the materials commonly used in rocket construction, considering factors like weight, strength, and heat resistance.\n- Learn about different types of rocket propulsion systems, including solid-propellant and liquid-propellant engines, and their associated saf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uments parse failed bug;stale;tool-calling ### Your current environment version: 0.8.2 features: VLLM_USE_V1=0 --enable-reasoning --reasoning-parser deepseek_r1 model: qwq-32b **here is the chat history:** ``` { "messag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eatures: VLLM_USE_V1=0 --enable-reasoning --reasoning-parser deepseek_r1 model: qwq-32b **here is the chat history:** ``` { "messages": [ { "role": "developer", "content": "You are the leader of a team of AI Agents and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: alidate the output of the other Agents before responding to the user.\n- Evaluate the response from other agents. If you feel the task has been completed, you can stop and respond to the user.\n- You can re-assign the t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a team of AI Agents and possible Sub-Teams:\n - Agent 1:\n - Name: Research Assistant Agent\n - Description: You are an Excellent Research Assistant. \nYou may be asked to research subjects that is after your knowledge...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ty, API examples). \n - Examine scalability: How does MCP handle large-scale models or distributed systems? \n\n#### **3. Applications & Use Cases** \n- **Objective**: Document real-world implementations and industry im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
