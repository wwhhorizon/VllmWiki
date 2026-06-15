# vllm-project/vllm#12673: [Installation]: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /meta-llama/Llama-3.2 when trying to run vllm docker container with model on ubuntu

| 字段 | 值 |
| --- | --- |
| Issue | [#12673](https://github.com/vllm-project/vllm/issues/12673) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /meta-llama/Llama-3.2 when trying to run vllm docker container with model on ubuntu

### Issue 正文摘录

### Your current environment Hello, I am trying to run docker container on ubuntu server, but facing below SSL error, I have tried request==2.27.1, but it didnt work. ```urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /meta-llama/Llama-3.2-1B-Instruct/resolve/main/config.json (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)')))``` ### How you are installing vllm Builded Docker image for CPU, using Dockerfile.cpu Ran docker container using below command. ```sudo docker run -it --rm -p 8000:8000 --env "HUGGING_FACE_HUB_TOKEN=test" vijaygawate/vllm-cputest --model meta-llama/Llama-3.2-1B-Instruct``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /meta-llama/Llama-3.2 when trying to run vllm docker container with model on ubuntu installation;stale ### Your current
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Installation]: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /meta-llama/Llama-3.2 when trying to run vllm docker container with model on ubuntu installation;stale ### Your curren...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en trying to run vllm docker container with model on ubuntu installation;stale ### Your current environment Hello, I am trying to run docker container on ubuntu server, but facing below SSL error, I have tried request==...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: . ```sudo docker run -it --rm -p 8000:8000 --env "HUGGING_FACE_HUB_TOKEN=test" vijaygawate/vllm-cputest --model meta-llama/Llama-3.2-1B-Instruct``` ### Before submitting a new issue... - [x] Make sure you already search...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
