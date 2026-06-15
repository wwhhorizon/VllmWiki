# vllm-project/vllm#17393: [Bug]: qwen3 structure output None

| 字段 | 值 |
| --- | --- |
| Issue | [#17393](https://github.com/vllm-project/vllm/issues/17393) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3 structure output None

### Issue 正文摘录

### Your current environment env: vllm 0.8.5 deploy qwen3-14b, with reasoning and tool enable ### 🐛 Describe the bug if using structure output, output None, no using structure output is ok ``` class Step(BaseModel): ground_truth_key_ideas: str system_response_key_ideas: str discussion: str recall: float precision: float if __name__ == '__main__': client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) # client.chat.completions.create json_schema = Step.model_json_schema() chat_response = client.beta.chat.completions.parse( model="qwen3-14b", messages=[ {'role': 'system', 'content': 'Your input fields are:\n1. `question` (str)\n2. `ground_truth` (str)\n3. `system_response` (str)\n\nYour output fields are:\n1. `ground_truth_key_ideas` (str): enumeration of key ideas in the ground truth\n2. `system_response_key_ideas` (str): enumeration of key ideas in the system response\n3. `discussion` (str): discussion of the overlap between ground truth and system response\n4. `recall` (float): fraction (out of 1.0) of ground truth covered by the system response\n5. `precision` (float): fraction (out of 1.0) of system response covered by the ground truth\n\nAll interactions will be...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3 structure output None bug ### Your current environment env: vllm 0.8.5 deploy qwen3-14b, with reasoning and tool enable ### 🐛 Describe the bug if using structure output, output None, no using structure outp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t typical RL problems have an action space that is an order of magnitude smaller, but do not specifically explain how the action spaces for typical problems is modeled or constructed.\n\n[[ ## system_response ## ]]\nThe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: system_response_key_ideas: str discussion: str recall: float precision: float if __name__ == '__main__': client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) # client.chat.completions.create json_schema...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tem_response_key_ideas: str discussion: str recall: float precision: float if __name__ == '__main__': client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) # client.chat.completions.create json_schema = S...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: arge. In general, locomotion in the real world can be condensed to three quantities - moving across X, Y or Z axes, or a linear combination thereof. The authors mention that typical RL problems have an action space that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
