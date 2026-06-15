# vllm-project/vllm#9571: [Bug]: Incomplete XML Output for Certain Prompts with Temperature=0

| 字段 | 值 |
| --- | --- |
| Issue | [#9571](https://github.com/vllm-project/vllm/issues/9571) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incomplete XML Output for Certain Prompts with Temperature=0

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Description: When using temperature=0, we expect the model to return complete XML format for all responses. However, we've observed that for certain prompts, the model returns incomplete XML format. Interestingly, slightly modifying the prompt (e.g., adding some characters) can result in complete XML output. More notably, when using the same prompts with other inference frameworks, the XML format output is correct and complete. Steps to reproduce: 1. Set temperature=0 2. Use the following prompt: \n你是一位保险新客户的接待人员，你只负责意外险，重疾险，医疗险，寿险和理财型保险的相关问题。如果客户问的是其他问题，引导客户来问相关问题。\n你需要在收集表单的过程中，结合聊天记录上下文，收集客户补充的表单信息。,注意今日的日期为2024-10-17 14:02:45。\n \n \n\n步骤2: 解释需要收集一些信息以便更好地提供帮助。\n\n \n \n友好地问候客户。解释你需要收集一些信息以便更好地帮助他们。使用一系列简短、清晰的问题来收集必要信息。收集完信息后，直接引导客户到最合适的预定运营动作，解释为什么这个动作对他们有益\n \n步骤1: 友好地问候客户。\n步骤2: 解释需要收集一些信息以便更好地提供帮助。\n步骤3: 使用一系列简短、清晰的问题收集必要信息。每次只问一个问题。\n步骤4: 总结收集到的信息，确认准确性。\n步骤5: 感谢并引导到预定运营动作 \n \n \n用温和、平易近人的语言表达。\n适当使用一些口语化表达,但不要过于随意。\n可以偶尔使用轻松幽默的语句,活跃气氛。\n多用\"\"您\"\"而不是\"\"你\"\",显得更有礼貌。\n在回答中加入一些个人观点或经历,增加亲和力。\n使用鼓励和肯定的词语,如\"\"这是个很好的问题\"\"。\n主动询问对方的想法或感受,增加互动性。\n结尾时可以用温暖的话语,如\"\"希望这些能够帮到您\"\"。\n适当使用感叹句...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: prompts produce incomplete XML format responses, while slightly modified versions of the same prompts produce complete format. In other inference frameworks, the same prompts correctly output complete XML format. Slight...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rompts with Temperature=0 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Description: When using temperature=0, we expect the model to return complete XML format for al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n\",\"message\":\"你好\",\"msgTime\":\"2024-10-17 14:30:42\",\"isInner\":false}]\n \n \n[{\"index\":\"重疾险科普\",\"content\":\"重疾险主要的作用是弥补发生重大疾病以后导致的收入损失，所以对于有收入的成年人来说，重疾险的额度应该要买到年收入的3-5倍，因为得了重大疾病，疾病的严重程度已经比较高了，因此3-5年不能工作是很正...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Incomplete XML Output for Certain Prompts with Temperature=0 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Description: When using temperature=0, we expect the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
