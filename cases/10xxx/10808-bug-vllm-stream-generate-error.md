# vllm-project/vllm#10808: [Bug]: vllm stream generate error

| 字段 | 值 |
| --- | --- |
| Issue | [#10808](https://github.com/vllm-project/vllm/issues/10808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm stream generate error

### Issue 正文摘录

### Your current environment ### Model Input Dumps 使用vllm启动openai 服务，在推理时出现以下情况 ![image](https://github.com/user-attachments/assets/f2d635b2-1830-4df2-9d86-38ec270664ec) ### 🐛 Describe the bug 运行下述代码时，当输入的文字过多时，其输出就会出现问题 def stream_chat(self, messages: List[Dict], **kwargs) -> Generator: """ Stream chat completions from the server. :param messages: A list of message dictionaries for the chat. :param kwargs: Optional parameters including tools for specific models. :yield: A stream of chat completion chunks. """ max_token = kwargs.get("max_token",1024) temperature = kwargs.get("temperature",0.7) stream_completion = self.client.chat.completions.create( model=self.model, messages=messages, stream=True, max_tokens=max_token, temperature=temperature, frequency_penalty=1.05 ) # Yield chunks of streamed responses for chunk in stream_completion: yield chunk ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: chat. :param kwargs: Optional parameters including tools for specific models. :yield: A stream of chat completion chunks. """ max_token = kwargs.get("max_token",1024) temperature = kwargs.get("temperature",0.7) stream_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: unk ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: arallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm stream generate error bug;stale ### Your current environment ### Model Input Dumps 使用vllm启动openai 服务，在推理时出现以下情况 ![image](https://github.com/user-attachments/assets/f2d635b2-1830-4df2-9d86-38ec270664ec) ### 🐛 Describ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm stream generate error bug;stale ### Your current environment ### Model Input Dumps 使用vllm启动openai 服务，在推理时出现以下情况 ![image](https://github.com/user-attachments/assets/f2d635b2-1830-4df2-9d86-38ec270664ec) ### 🐛...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
