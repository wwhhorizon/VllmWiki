# vllm-project/vllm#15110: [Bug]: Internal Server Error when using Qwen2-VL-7B with vLLM Docker Container

| 字段 | 值 |
| --- | --- |
| Issue | [#15110](https://github.com/vllm-project/vllm/issues/15110) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error when using Qwen2-VL-7B with vLLM Docker Container

### Issue 正文摘录

[qwen2-vl-7b_nohup_errors_2025-03-20.log](https://github.com/user-attachments/files/19380089/qwen2-vl-7b_nohup_errors_2025-03-20.log) ### My current environment ### 🐛 Describe the bug --- **Bug Report: Internal Server Error when Using Qwen2-VL-7B in vLLM Docker Container** --- ### **1. Issue Description** When invoking the **Qwen2-VL-7B** model via the vLLM Docker container using the OpenAI API format, an `Internal Server Error` occurs. The error log indicates an `AssertionError`, likely related to processing image inputs. --- ### **2. Reproduction Steps** 1. Start the vLLM Docker container (e.g., named `vllm-jca`). 2. Execute the following `curl` command: ```bash curl http://192.168.100.11:8001/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen2-vl-7b", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ {"type": "image_url", "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"}}, {"type": "text", "text": "What is the text in the illustrate?"} ]} ] }' ``` 3. The request triggers an HTTP `500 Internal Server Error`, and the following error appears in `nohup.out`:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Internal Server Error when using Qwen2-VL-7B with vLLM Docker Container bug;stale [qwen2-vl-7b_nohup_errors_2025-03-20.log](https://github.com/user-attachments/files/19380089/qwen2-vl-7b_nohup_errors_2025-03-20.l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Internal Server Error when using Qwen2-VL-7B with vLLM Docker Container bug;stale [qwen2-vl-7b_nohup_errors_2025-03-20.log](https://github.com/user-attachments/files/19380089/qwen2-vl-7b_nohup_errors_2025-03-20.l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ernal Server Error when using Qwen2-VL-7B with vLLM Docker Container bug;stale [qwen2-vl-7b_nohup_errors_2025-03-20.log](https://github.com/user-attachments/files/19380089/qwen2-vl-7b_nohup_errors_2025-03-20.log) ### My...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: docker run -d --gpus all --shm-size=10.24gb -v /home/ATLAS:/home/vllm-test --name vllm-test -p 8001:8002 -e API_KEY=sk-jca --restart unless-stopped vllm-202411260804 & ``` --- ### **7. Troubleshooting Steps Taken** - Ve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
