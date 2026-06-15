# vllm-project/vllm#11704: [Bug]: Mismatch multi-modal placeholder of LLava-1.6-Mistral-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#11704](https://github.com/vllm-project/vllm/issues/11704) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mismatch multi-modal placeholder of LLava-1.6-Mistral-7B

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use LLava-1.6-Mistral-7B to infer multimodal data, using the following code: ```python outputs = model.generate_outputs(current_messages) ``` Then the error: ValueError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250103-120322.pkl): Attempted to assign 1272 = 1272 multimodal tokens to 1224 placeholders I found the relevant issues like #8421 and #7996, but they didn't solve my problem. The img size is (198, 176) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error;mismatch env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Mismatch multi-modal placeholder of LLava-1.6-Mistral-7B bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use LLava-1.6-Mistral-7B to infer multimodal data, using...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eholder of LLava-1.6-Mistral-7B bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use LLava-1.6-Mistral-7B to infer multimodal data, using the following code: ```python o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error;mismatch env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Mismatch multi-modal placeholder of LLava-1.6-Mistral-7B bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use LLava-1.6-Mistral-7B to infer multimodal data, using

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
