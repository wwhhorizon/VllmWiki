# vllm-project/vllm#11070: [Usage]: Run OpenAI api_server.py on Neuron Device Failed, Model architectures ['OPTForCausalLM'] are not supported on Neuron for now. Supported architectures: ['LlamaForCausalLM', 'MistralForCausalLM']

| 字段 | 值 |
| --- | --- |
| Issue | [#11070](https://github.com/vllm-project/vllm/issues/11070) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Run OpenAI api_server.py on Neuron Device Failed, Model architectures ['OPTForCausalLM'] are not supported on Neuron for now. Supported architectures: ['LlamaForCausalLM', 'MistralForCausalLM']

### Issue 正文摘录

### Your current environment Dear vLLM Support Team, I hope this message finds you well. I am reaching out to report an issue encountered while executing the python ```api_server.py``` command within the ```vllm/vllm/entrypoints/openai ```directory on our server. Unfortunately, this attempt resulted in an error Here is the Pip lis: ``` Package Version --------------------------------- -------------------------------------- absl-py 2.1.0 accelerate 1.2.0 aiohappyeyeballs 2.4.4 aiohttp 3.11.10 aiosignal 1.3.1 annotated-types 0.7.0 anyio 4.7.0 argon2-cffi 23.1.0 argon2-cffi-bindings 21.2.0 arrow 1.3.0 asttokens 3.0.0 async-lru 2.0.4 async-timeout 5.0.1 attrs 24.2.0 aws-neuronx-runtime-discovery 2.9 awscli 1.36.18 babel 2.16.0 beautifulsoup4 4.12.3 bleach 6.2.0 boto3 1.35.77 botocore 1.35.77 cachetools 5.5.0 certifi 2024.8.30 cffi 1.17.1 charset-normalizer 3.4.0 click 8.1.7 cloud-tpu-client 0.10 cloudpickle 3.1.0 colorama 0.4.6 comm 0.2.2 compressed-tensors 0.8.0 datasets 2.19.1 debugpy 1.8.9 decorator 5.1.1 defusedxml 0.7.1 dill 0.3.8 diskcache 5.6.3 distro 1.9.0 docutils 0.16 ec2-metadata 2.14.0 einops 0.8.0 environment-kernels 1.2.0 exceptiongroup 1.2.2 executing 2.1.0 fastapi 0.11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: in an error Here is the Pip lis: ``` Package Version --------------------------------- -------------------------------------- absl-py 2.1.0 accelerate 1.2.0 aiohappyeyeballs 2.4.4 aiohttp
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: Run OpenAI api_server.py on Neuron Device Failed, Model architectures ['OPTForCausalLM'] are not supported on Neuron for now. Supported architectures: ['LlamaForCausalLM', 'MistralForCausalLM'] bug ### Your cur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 0.35.1 regex 2024.11.6 requests 2.31.0 requests-unixsocket 0.3.0 rfc3339-validator 0.1.4 rfc3986-validator 0.1.1 rpds-py 0.22.3 rsa
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 1.9.0 docutils 0.16 ec2-metadata 2.14.0 einops 0.8.0 environment-kernels 1.2.0 exceptiongroup 1.2.2 executing 2.1.0 fastapi
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s 4.47.0 transformers-neuronx 0.12.313 triton 2.1.0 types-python-dateutil 2.9.0.20241206 typing_extensions 4.12.2 tzdata 2024.2 uri-template 1.3.0 uritempla

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
