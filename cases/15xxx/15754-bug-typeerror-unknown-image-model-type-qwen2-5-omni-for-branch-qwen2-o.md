# vllm-project/vllm#15754: [Bug]: TypeError: Unknown image model type: qwen2_5_omni for branch: qwen2_omni_public_v1

| 字段 | 值 |
| --- | --- |
| Issue | [#15754](https://github.com/vllm-project/vllm/issues/15754) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: Unknown image model type: qwen2_5_omni for branch: qwen2_omni_public_v1

### Issue 正文摘录

### Your current environment Greetings, everyone. 1. Now I am trying to deploy the latest Qwen2.5-Omni-7B model[https://huggingface.co/Qwen/Qwen2.5-Omni-7B] using the branch code from here: https://github.com/fyabc/vllm/tree/qwen2_omni_public_v1 2. I compile the code and run the model as following: `vllm serve /home/nvidia/.cache/huggingface/hub/models--Qwen--Qwen2.5-Omni-7B/snapshots/c1169d7a58a87ae5f6d62e25d605be2f26489790 --served-model-name qwen2.5-omni --enable-chunked-prefill=False --gpu-memory-utilization 0.8 --trust-remote-code ` 3. I use another project named openweb-ui[https://github.com/open-webui/open-webui] to interact with the deployed service. And I do believe most of you have heard/used this project. 3.1 First I tried a simple hello, it works. :D ![Image](https://github.com/user-attachments/assets/51f67b15-68c9-4932-9808-c9eb9c316892) 3.2 Then I upload a picture of flower and ask: please describe this picture. And I got following error output: ERROR 03-29 21:47:54 [serving_chat.py:204] Error in preprocessing prompt inputs ERROR 03-29 21:47:54 [serving_chat.py:204] Traceback (most recent call last): ERROR 03-29 21:47:54 [serving_chat.py:204] File "/home/nvidia/anaco...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TypeError: Unknown image model type: qwen2_5_omni for branch: qwen2_omni_public_v1 bug;stale ### Your current environment Greetings, everyone. 1. Now I am trying to deploy the latest Qwen2.5-Omni-7B model[https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nown image model type: qwen2_5_omni for branch: qwen2_omni_public_v1 bug;stale ### Your current environment Greetings, everyone. 1. Now I am trying to deploy the latest Qwen2.5-Omni-7B model[https://huggingface.co/Qwen/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: from here: https://github.com/fyabc/vllm/tree/qwen2_omni_public_v1 2. I compile the code and run the model as following: `vllm serve /home/nvidia/.cache/huggingface/hub/models--Qwen--Qwen2.5-Omni-7B/snapshots/c1169d7a58...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: i** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be2f26489790 --served-model-name qwen2.5-omni --enable-chunked-prefill=False --gpu-memory-utilization 0.8 --trust-remote-code ` 3. I use another project named openweb-ui[https://github.com/open-webui/open-webui] to inte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
