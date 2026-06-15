# vllm-project/vllm#19857: [Bug]: AttributeError: 'InferenceClient' object has no attribute 'post'

| 字段 | 值 |
| --- | --- |
| Issue | [#19857](https://github.com/vllm-project/vllm/issues/19857) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'InferenceClient' object has no attribute 'post'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug HI ALL, I AM TRYING TO RUN BELOW CODE USING HUGGINGFACEHUB PACKAGE: from langchain.llms import HuggingFaceHub llm = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", huggingfacehub_api_token=userdata.get('HUGGINGFACEHUB_API_TOKEN')) ## invoke the LLM response=llm.invoke("write a 4 lines poem on AI especially for small children") print(response) but this gives below error: It seems there is a bug : ----> 2 response=llm.invoke("write a 4 lines poem on AI especially for small children") 3 4 print(response) 5 frames [/usr/local/lib/python3.11/dist-packages/langchain_community/llms/huggingface_hub.py](https://localhost:8080/#) in _call(self, prompt, stop, run_manager, **kwargs) 136 parameters = {**_model_kwargs, **kwargs} 137 --> 138 response = self.client.post( 139 json={"inputs": prompt, "parameters": parameters}, task=self.task 140 ) AttributeError: 'InferenceClient' object has no attribute 'post' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can an...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ING TO RUN BELOW CODE USING HUGGINGFACEHUB PACKAGE: from langchain.llms import HuggingFaceHub llm = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", huggingfacehub_api_token=userdata.get('HUGGINGFACEHUB_AP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the LLM response=llm.invoke("write a 4 lines poem on AI especially for small children") print(response) but this gives below error: It seems there is a bug : ----> 2 response=llm.invoke("write a 4 lines poem on AI espec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug HI ALL, I AM TRYING TO RUN BELOW CODE USING HUGGINGFACEHUB PACKAGE: from langchain.llms import HuggingFaceHub llm = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", huggingfacehub_ap...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: AttributeError: 'InferenceClient' object has no attribute 'post' bug;stale ### Your current environment ### 🐛 Describe the bug HI ALL, I AM TRYING TO RUN BELOW CODE USING HUGGINGFACEHUB PACKAGE: from langchain.llms...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
