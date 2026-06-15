# vllm-project/vllm#37558: “vLLM-deployed Qwen3.5 with Reasoning Parser Shows Empty reasoningContent in Spring AI OpenAI Model”

| 字段 | 值 |
| --- | --- |
| Issue | [#37558](https://github.com/vllm-project/vllm/issues/37558) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> “vLLM-deployed Qwen3.5 with Reasoning Parser Shows Empty reasoningContent in Spring AI OpenAI Model”

### Issue 正文摘录

### Your current environment When deploying the Qwen3.5 model using vLLM with reasoning mode enabled and configuring --reasoning-parser qwen3, I found that reasoningContent is empty when printing OverAllState. The OpenAI model from Spring AI Alibaba is being used. ### 🐛 Describe the bug Raw NodeOutput: { "OverAllState": { "data": { "_graph_execution_id_": "c0646529-c46a-4839-a11c-68fba5e99df9", "input": "你好", "user_input": "你好", "has_images": false, "messages": [{ "messageType": "USER", "metadata": { "messageType": "USER" }, "rendered": false, "text": "你是一个专业的智能助手。\n每次响应前先调用 read_skill(\"text-fee-agent\") 加载完整执行规范。\n最终输出必须严格按照该技能文档中定义的标题、顺序、表头和字段格式返回，不得增删、改名、重排或省略。\n重要：点击收费计算（用户直接点击通行记录触发，带 selected_id）和自然语言车牌计费（用户输入车牌号查询，先候选后确认）必须使用完全一致的输出模板与字段顺序，两种场景的\"参考估算\"模块中车牌号展示格式也必须一致，都必须参考 agent skills 里面的 text-fee-agent 的要求。\n" }, { "messageType": "ASSISTANT", "metadata": { "role": "ASSISTANT", "messageType": "ASSISTANT", "refusal": "", "finishReason": "TOOL_CALLS", "index": 0, "annotations": [], "id": "chatcmpl-bc600ca8b28e0131", "reasoningContent": "" }, "toolCalls": [{ "id": "call_af5b037dac144636b8b76745", "type": "function", "name": "read_skill", "arguments": "{\"skill_name\": \"tex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: “vLLM-deployed Qwen3.5 with Reasoning Parser Shows Empty reasoningContent in Spring AI OpenAI Model” bug ### Your current environment When deploying the Qwen3.5 model using vLLM with reasoning mode enabled and configuri...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: fba5e99df9", "input": "你好", "user_input": "你好", "has_images": false, "messages": [{ "messageType": "USER", "metadata": { "messageType": "USER" }, "rendered": false, "text": "你是一个专业的智能助手。\n每次响应前先调用 read_skill(\"text-fee-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `find_vehicle_journey_candidates`。\\n - 属于政策条款、优惠条件、适用范围、依据引用问题：调用 `search_policy_documents`。\\n3. 处理工具结果：\\n - `SUCCESS`：根据工具返回内容输出结论。\\n - `NEED_HUMAN_APPROVAL`：按固定候选模板输出并等待用户给 id。\\n - `NOT_FOUND` / `INVALID_INPUT`：原...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
