# vllm-project/vllm#23251: [Bug]: GLM-4.5-AIR erratic behaviour when generating multiple sequences for the same prompt (SamplingParams.n>1)

| 字段 | 值 |
| --- | --- |
| Issue | [#23251](https://github.com/vllm-project/vllm/issues/23251) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5-AIR erratic behaviour when generating multiple sequences for the same prompt (SamplingParams.n>1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using GLM-4.5-Air and the OpenAI-compatible interface setting n>1 in the sampling parameters leads to broken behaviour. Judging from the output we get it seems that the model does generate multiple outputs which are reported back to the user somewhat interwoven. Also the model tends to enter an infinite generation loop degenerating to nonsense output (even considering we see multiple outputs at once) which seems to suggest that not only are the outputs interwoven for the user but that this broken sequence is then fed back into the model for the autoregressive generation. Here is some sample code to reproduce the issue. ```shell vllm serve \ cpatonn/GLM-4.5-Air-AWQ-4bit \ --served-model-name glm45 \ --max-num-seqs 16 \ --max-model-len 80000 \ --max-seq-len-to-capture 80000\ --gpu-memory-utilization 0.95 \ --host 0.0.0.0 \ --port 8000 \ --dtype float16 ``` ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="test") for chunk in client.chat.completions.create( model="glm45", messages=[ {"role": "user", "content": "Hello, how are you?"} ], n=2, stream=True, ): print(chunk.choices[0].delta....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --host 0.0.0.0 \ --port 8000 \ --dtype float16 ``` ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="test") for chunk in client.chat.completions.create( model="glm45", messages...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: u-memory-utilization 0.95 \ --host 0.0.0.0 \ --port 8000 \ --dtype float16 ``` ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="test") for chunk in client.chat.completions.cre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s to broken behaviour. Judging from the output we get it seems that the model does generate multiple outputs which are reported back to the user somewhat interwoven. Also the model tends to enter an infinite generation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: . The problem seems to **only** appear when using n>1. Sending multiple requests at the same time (even with the exact same content) is handled correctly. ### Before submitting a new issue... - [x] Make sure you already...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
