# vllm-project/vllm#9310: [Bug]: vllm mistralai--Codestral-22B-v0.1 response is truncated

| 字段 | 值 |
| --- | --- |
| Issue | [#9310](https://github.com/vllm-project/vllm/issues/9310) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm mistralai--Codestral-22B-v0.1 response is truncated

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When calling mistralai--Codestral-22B-v0.1 using vllm message is always truncated ![image](https://github.com/user-attachments/assets/0963013d-61cc-4f5e-ac1d-a58a2651b10f) ``` python from vllm import LLM, SamplingParams from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from mistral_common.protocol.instruct.messages import UserMessage from mistral_common.protocol.instruct.request import ChatCompletionRequest from mistral_common.protocol.instruct.messages import UserMessage,SystemMessage, AssistantMessage mistral_models_path = "MISTRAL_MODELS_PATH" tokenizer = MistralTokenizer.v3() sys_content = '你是一个代码助手' messages = [ {"role": "system", "content": sys_content}, {"role": "user", "content": '你是谁？'} ] assistant_head = "我是由" messages = [SystemMessage(content = messages[0]['content']), UserMessage(content = messages[1]['content']), AssistantMessage(content = assistant_head, prefix=True) ] completion_request = ChatCompletionRequest(messages=messages) tokens = tokenizer.encode_chat_completion(completion_request).tokens sampling_params = SamplingParams(temperature=0.01, top_p=1) llm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ents/assets/0963013d-61cc-4f5e-ac1d-a58a2651b10f) ``` python from vllm import LLM, SamplingParams from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from mistral_common.protocol.instruct.messages impo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: trained(model_dir, torch_dtype=torch.bfloat16, attn_implementation="flash_attention_2", device_map="auto",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ge](https://github.com/user-attachments/assets/0dc7621b-3a08-4821-8a8a-9bb200410741) ``` python from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from mistral_common.protocol.instruct.messages import...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: struct.messages import UserMessage from mistral_common.protocol.instruct.request import ChatCompletionRequest from mistral_common.protocol.instruct.messages import UserMessage,SystemMessage, AssistantMessage mistral_mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
