# vllm-project/vllm#17977: [Bug]: Default chat template is no longer allowed for vicuna-13b-1.5

| 字段 | 值 |
| --- | --- |
| Issue | [#17977](https://github.com/vllm-project/vllm/issues/17977) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Default chat template is no longer allowed for vicuna-13b-1.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use the following command to serve vicuna-13b-v1.5 ,and it runs well `vllm serve model/vicuna-13b-v1.5 --dtype auto --api-key token-abc123` Next, I run the following code to send an inference request ``` import openai openai.api_key = 'token-abc123' # Your API key here openai.api_type = 'token-abc123' openai.api_base = 'http://localhost:8000/v1' # Your API base here openai.api_type = 'open_ai' # Your API base here completion = openai.ChatCompletion.create( model="model/vicuna-13b-v1.5", messages=[ {"role": "user", "content": "Hello!"} ] ) print(completion.choices[0].message) ``` it gives me the following error: ``` Traceback (most recent call last): File "/home/ubuntu/miniforge3/envs/llava/lib/python3.10/site-packages/openai/api_requestor.py", line 403, in handle_error_response error_data = resp["error"] KeyError: 'error' During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/home/ubuntu/code/Video-RAG-master-main/vllm_sample.py", line 7, in completion = openai.ChatCompletion.create( File "/home/ubuntu/miniforge3/envs/llava/lib/python3.10/site-packages/openai/api_resources/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Default chat template is no longer allowed for vicuna-13b-1.5 bug;stale ### Your current environment ### 🐛 Describe the bug I use the following command to serve vicuna-13b-v1.5 ,and it runs well `vllm serve model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bc123` Next, I run the following code to send an inference request ``` import openai openai.api_key = 'token-abc123' # Your API key here openai.api_type = 'token-abc123' openai.api_base = 'http://localhost:8000/v1' # Yo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e vicuna-13b-v1.5 ,and it runs well `vllm serve model/vicuna-13b-v1.5 --dtype auto --api-key token-abc123` Next, I run the following code to send an inference request ``` import openai openai.api_key = 'token-abc123' #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: em? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ollowing command to serve vicuna-13b-v1.5 ,and it runs well `vllm serve model/vicuna-13b-v1.5 --dtype auto --api-key token-abc123` Next, I run the following code to send an inference request ``` import openai openai.api...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
