# vllm-project/vllm#9408: [Usage]: Unable to use default template when serving glm-4v-9b in VLLM 0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#9408](https://github.com/vllm-project/vllm/issues/9408) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to use default template when serving glm-4v-9b in VLLM 0.6.3

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using vllm as the openai api compatible server with glm-4v-9b, the request I used for test is like below: ```shell curl --request POST \ --url http://vllm-vl-glm.xxx.com/v1/chat/completions \ --data '{ "model": "glm/glm-4v-9b", "messages": [ { "role": "user", "content": [ {"type": "text", "text": "describe the picture"}, { "type": "image_url", "image_url":{ "url": "https://s3.xxx.com/image.png" } } ] } ] }' ``` Then I got the error : ```bash ERROR 10-16 15:24:25 serving_chat.py:158] Error in applying chat template from request ERROR 10-16 15:24:25 serving_chat.py:158] Traceback (most recent call last): ERROR 10-16 15:24:25 serving_chat.py:158] File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 147, in create_chat_completion ERROR 10-16 15:24:25 serving_chat.py:158] prompt = apply_hf_chat_template( ERROR 10-16 15:24:25 serving_chat.py:158] File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/chat_utils.py", line 547, in apply_hf_chat_template ERROR 10-16 15:24:25 serving_chat.py:158] raise ValueError( ERROR 10-16 15:24:25 serving_chat.py:15...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rving glm-4v-9b in VLLM 0.6.3 usage ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using vllm as the openai api compatible server with glm-4v-9b, the request I used for test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ns? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: I'm using vllm as the openai api compatible server with glm-4v-9b, the request I used for test is like below: ```shell curl --request POST \ --url http://vllm-vl-glm.xxx.com/v1/chat/completions \ --data '{ "model": "glm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
