# vllm-project/vllm#9002: [Bug] [Llama 3.2 vision] huge difference of # of prompt tokens between streaming and non-streaming mode when image is included in prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#9002](https://github.com/vllm-project/vllm/issues/9002) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [Llama 3.2 vision] huge difference of # of prompt tokens between streaming and non-streaming mode when image is included in prompt

### Issue 正文摘录

### Your current environment ### Model Input Dumps {"messages": [ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABt...." } }, { "type": "text", "text": "describe the image as specific as possible" } ] } ] ,"max_tokens":50,"temperature":0,"top_p":1,"stream":false, "model": "Llama-3.2-90B-Vision-Instruct"} ### 🐛 Describe the bug - when `stream = false`, response looks like below: ``` { "id":"chat-01f9cd3c8144437a97770d7e113f7919", "object":"chat.completion", "created":1727798141, "model":"Llama-3.2-90B-Vision-Instruct", "choices":[ { "index":0, "message":{ "role":"assistant", "content":"The image depicts a stunning galaxy, with its central core radiating a bright light. The galaxy's spiral arms are visible, featuring a mix of dark and light blue hues, accompanied by numerous stars scattered throughout. In the foreground, a smaller galaxy is", "tool_calls":[ ] }, "finish_reason":"length" } ], "usage":{ "prompt_tokens":18, "total_tokens":68, "completion_tokens":50 } } ``` - when `stream = true`, response looks like below (only last few chunks): ``` data: {"id":"chat-b...

## 现有链接修复摘要

#8861 [Bugfix] Include encoder prompts len to non-stream api usage response

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] [Llama 3.2 vision] huge difference of # of prompt tokens between streaming and non-streaming mode when image is included in prompt bug ### Your current environment ### Model Input Dumps {"messages": [
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "type": "text", "text": "describe the image as specific as possible" } ] } ] ,"max_tokens":50,"temperature":0,"top_p":1,"stream":false, "model": "Llama-3.2-90B-Vision-Instruct"} ### 🐛 Describe the bug - when `stream
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: accompanied by numerous stars scattered throughout. In the foreground, a smaller galaxy is", "tool_calls":[ ] }, "finish_reason":"length" } ], "usage":{ "prompt_tokens":18, "total_tokens":68, "completion_t
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency #8861 [Bugfix] Include encoder prompts len to non-stream api usage response Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: } ] ,"max_tokens":50,"temperature":0,"top_p":1,"stream":false, "model": "Llama-3.2-90B-Vision-Instruct"} ### 🐛 Describe the bug - when `stream = false`, response looks like below: ``` { "id":"chat-01f9cd3c8144437a97770d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8861](https://github.com/vllm-project/vllm/pull/8861) | closes_keyword | 0.95 | [Bugfix] Include encoder prompts len to non-stream api usage response | FIX #9002 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b>< |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
