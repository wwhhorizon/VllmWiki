# vllm-project/vllm#12024: [Bug]: server crash when glm4-9b-chat got an image request 

| 字段 | 值 |
| --- | --- |
| Issue | [#12024](https://github.com/vllm-project/vllm/issues/12024) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: server crash when glm4-9b-chat got an image request 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The current code shares the same modelling code `ChatGLMForCausalLM` between glm-4v (THUDM/glm-4v-9b) and glm-4 (THUDM/glm-4-9b-chat), which leads to glm-4 being incorrectly marked as a multimodal model as well, and once the request is incorrectly passed with an image, the server will just shutdown instead of returning an error. A temporary solution is to specify `--limit-mm-per-prompt image=0` when starting the server. For example: ```bash curl --location 'http://0.0.0.0:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "glm-4-9b-chat", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "这些是什么" }, { "type": "image_url", "image_url": { "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg" } } ] } ], "stream": false }' ``` Lead to ```log vllm-openai-1 | INFO 01-14 09:20:57 logger.py:37] Received request chatcmpl-d595054ac68043b2aaa50d69d440d7d9: prompt: '[gMASK] \n这些是什么 \n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, mi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: hat got an image request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The current code shares the same modelling code `ChatGLMForCausalLM` between glm-4v (THUDM/glm-4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: server crash when glm4-9b-chat got an image request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The current code shares the same modelling code `ChatGLMForCau...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t shutdown instead of returning an error. A temporary solution is to specify `--limit-mm-per-prompt image=0` when starting the server. For example: ```bash curl --location 'http://0.0.0.0:8000/v1/chat/completions' \ --h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: et. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: } } ] } ], "stream": false }' ``` Lead to ```log vllm-openai-1 | INFO 01-14 09:20:57 logger.py:37] Received request chatcmpl-d595054ac68043b2aaa50d69d440d7d9: prompt: '[gMASK] \n这些是什么 \n', params: SamplingParams(n=1, pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
