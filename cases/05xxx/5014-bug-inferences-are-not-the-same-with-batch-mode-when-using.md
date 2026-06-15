# vllm-project/vllm#5014: [Bug]: inferences are not the same with batch mode when using 

| 字段 | 值 |
| --- | --- |
| Issue | [#5014](https://github.com/vllm-project/vllm/issues/5014) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: inferences are not the same with batch mode when using 

### Issue 正文摘录

### Your current environment vllm version is 0.4.2 ### 🐛 Describe the bug hi there, I am using openai api_server to up the lora checkpoint and request it for inference on another machine. - up the server, following guidance https://docs.vllm.ai/en/latest/models/lora.html ``` python -m vllm.entrypoints.openai.api_server \ --model "mistralai/Mistral-7B-Instruct-v0.2" \ --dtype auto --api-key "yyy" --port 1703 \ --worker-use-ray \ --enable-lora \ --lora-modules sql-lora=./checkpoint-6664 ``` - request via langchain openai server ``` from langchain_openai import ChatOpenAI url = "http://3.17.17.234:1703/v1/" llm = ChatOpenAI(temperature=0, max_tokens=1024, openai_api_key="yyy", openai_api_base=url, model="sql-lora", #model_name="mistralai/Mistral-7B-Instruct-v0.2") resp = llm.invoke(prompt) ``` However, I find thta the responses in this way have huge difference with the reponses from original way of huggingface AutoModelForCausalLM.from_pretrained manner or from the batch manner in https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference. Am I missing something ?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: same with batch mode when using bug ### Your current environment vllm version is 0.4.2 ### 🐛 Describe the bug hi there, I am using openai api_server to up the lora checkpoint and request it for inference on another mach...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hine. - up the server, following guidance https://docs.vllm.ai/en/latest/models/lora.html ``` python -m vllm.entrypoints.openai.api_server \ --model "mistralai/Mistral-7B-Instruct-v0.2" \ --dtype auto --api-key "yyy" --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ai.api_server \ --model "mistralai/Mistral-7B-Instruct-v0.2" \ --dtype auto --api-key "yyy" --port 1703 \ --worker-use-ray \ --enable-lora \ --lora-modules sql-lora=./checkpoint-6664 ``` - request via langchain openai s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g hi there, I am using openai api_server to up the lora checkpoint and request it for inference on another machine. - up the server, following guidance https://docs.vllm.ai/en/latest/models/lora.html ``` python -m vllm....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r machine. - up the server, following guidance https://docs.vllm.ai/en/latest/models/lora.html ``` python -m vllm.entrypoints.openai.api_server \ --model "mistralai/Mistral-7B-Instruct-v0.2" \ --dtype auto --api-key "yy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
