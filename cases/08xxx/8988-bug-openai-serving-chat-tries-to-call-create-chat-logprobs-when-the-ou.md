# vllm-project/vllm#8988: [Bug]: openai.serving_chat tries to call _create_chat_logprobs when the output.text is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#8988](https://github.com/vllm-project/vllm/issues/8988) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openai.serving_chat tries to call _create_chat_logprobs when the output.text is empty

### Issue 正文摘录

### Your current environment ### Model Input Dumps server start command ``` # Version: vllm/vllm-openai:v0.6.2 # server: docker run -tid --gpus \"device=0,1,2,3\" --shm-size 5g \ -p 8081:8000 -v /mnt/data/models:/models \ --ulimit nofile=65535:65535 \ --name vllm-v0.6.2-llama3.1-70b-4gpus-128k \ vllm/vllm-openai:v0.6.2 \ --tensor-parallel-size=4 \ --disable-log-requests \ --model=/models/Meta-Llama-3.1-70B-Instruct \ --enable-chunked-prefill \ --served-model-name=vllm-model ``` The input prompt is too long and github doesn't support .py so I had to override it to .txt [send_llama3_128k.py.txt](https://github.com/user-attachments/files/17199893/send_llama3_128k.py.txt) ### 🐛 Describe the bug When I try to run the above script `send_llama3_128k.py`, the server raises an error: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/starlette/responses.py", line 257, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/usr/local/lib/python3.12/dist-packages/starlette/responses.py", line 253, in wrap await func() File "/usr/local/lib/python3.12/dist-packages/starlette/responses.py", line 230, in l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: urrent environment ### Model Input Dumps server start command ``` # Version: vllm/vllm-openai:v0.6.2 # server: docker run -tid --gpus \"device=0,1,2,3\" --shm-size 5g \ -p 8081:8000 -v /mnt/data/models:/models \ --ulimi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s when the output.text is empty bug ### Your current environment ### Model Input Dumps server start command ``` # Version: vllm/vllm-openai:v0.6.2 # server: docker run -tid --gpus \"device=0,1,2,3\" --shm-size 5g \ -p 8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: openai:v0.6.2 \ --tensor-parallel-size=4 \ --disable-log-requests \ --model=/models/Meta-Llama-3.1-70B-Instruct \ --enable-chunked-prefill \ --served-model-name=vllm-model ``` The input prompt is too long and github doe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: obs=request.top_logprobs, ) else: logprobs = None ``` After adding the above line, the new output of `python send_llama3_128k.py` is: ``` b'data: {"id":"chat-4c7bcc2aac344da2b71fa7c07460e4c2","object":"chat.completion.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
