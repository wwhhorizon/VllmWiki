# vllm-project/vllm#12364: [Bug]: Inference with gguf returns garbage

| 字段 | 值 |
| --- | --- |
| Issue | [#12364](https://github.com/vllm-project/vllm/issues/12364) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference with gguf returns garbage

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have fine-tuned a model based on `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. We used `llama.cpp` to generate a .gguf file for the model. When we serve the model with `llama.cpp`, it works. When we serve the model with vLLM, we get garbage, similar to what was identified in issue #10675. As you can see above, we are using the latest vLLM (we run it from the docker image on Docker Hub //vllm/vllm-openai:latest). As an example, this client code: ```python import openai client = openai.OpenAI(base_url="http://ip-172-41-47-76.us-west-2.compute.internal:8500/v1", api_key="none") results = client.chat.completions.create( model='/data/models/trained/rgenter/tinyllama-24-11-20_00-10-44.10epoch.gguf', messages=[{ 'role': 'user', 'content': '/meraki what alerts are active on network xyz?', }], temperature=0.0, ) print(results) ``` produces this result with `llama.cpp`: ``` ChatCompletion(id='chatcmpl-BVO2uFR4BY28iKRi4GPWQa1iaLLCb8Rb', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='meraki getNetworkAlertsHistory --networkId xyz', refusal=None, role='assist...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: As you can see above, we are using the latest vLLM (we run it from the docker image on Docker Hub //vllm/vllm-openai:latest). As an example, this client code: ```python import openai client = openai.OpenAI(base_url="htt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;oom;slowdow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: with gguf returns garbage bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have fine-tuned a model based on `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. We used `llama.cpp` t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Inference with gguf returns garbage bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have fine-tuned a model based on `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. We u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
