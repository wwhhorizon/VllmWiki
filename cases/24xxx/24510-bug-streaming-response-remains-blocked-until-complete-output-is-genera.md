# vllm-project/vllm#24510: [Bug]: Streaming response remains blocked until complete output is generated with gpt-oss-120B model on A100 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#24510](https://github.com/vllm-project/vllm/issues/24510) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming response remains blocked until complete output is generated with gpt-oss-120B model on A100 GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As the title suggests when I'm trying to host GPT-OSS-120 model on K8s with 8xA100-40G GPUs, streaming doesn't work as expected. First of all I need 8 GPUs(320G vRAM) just to be able to load the model since mxfp4 isn't supported. After loading with that I am able to work with the model but the streaming with chat_completions and responses endpoints doesn't work. It waits until the complete responses is generated and then it streams everything in a flash. I tried both responses and chat_completion endpoints but it gets stuck until the complete response is generated. Code to reproduce: ```python from openai import OpenAI client = OpenAI() stream = client.responses.create( model="gpt-oss-120B", input=[ { "role": "user", "content": "Say 'double bubble bath' ten times fast.", }, ], stream=True, ) for event in stream: print(event) ``` **Note that I tried same code and config with H100 node pool and it works as expected, i.e., response chunk starts streaming as soon as first token is generated so the issue is specific to the A100 GPUs.** EDIT: Added output of collect_env.py ### Before submitting a new issue... - [x] Make sure you alread...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: complete response is generated. Code to reproduce: ```python from openai import OpenAI client = OpenAI() stream = client.responses.create( model="gpt-oss-120B", input=[ { "role": "user", "content": "Say 'double bubble b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ns blocked until complete output is generated with gpt-oss-120B model on A100 GPU bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug As the title suggests when I'm trying to host GPT-OSS-120 model on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: of all I need 8 GPUs(320G vRAM) just to be able to load the model since mxfp4 isn't supported. After loading with that I am able to work with the model but the streaming with chat_completions and responses endpoints doe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: reaming response remains blocked until complete output is generated with gpt-oss-120B model on A100 GPU bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug As the title suggests when I'm trying to host...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: til complete output is generated with gpt-oss-120B model on A100 GPU bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug As the title suggests when I'm trying to host GPT-OSS-120 model on K8s with 8xA1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
