# vllm-project/vllm#6257: [Usage]: How can I pass Image in Phi-3-vision-128k-instruct with langchain community

| 字段 | 值 |
| --- | --- |
| Issue | [#6257](https://github.com/vllm-project/vllm/issues/6257) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I pass Image in Phi-3-vision-128k-instruct with langchain community

### Issue 正文摘录

### Your current environment from langchain_community.llms import VLLMOpenAI from PIL import Image llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="http://150.0.2.236:8888/v1", model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]}, ) image = Image.open("invoice_data_images/PO - 042 (REVISED )_page_1.png") prompt_1 = "Give me invoice date from given image" messages = { "prompt": prompt_1, "multi_modal_data": { "image": image }, } print(llm.invoke(messages)) ### How would you like to use vllm I want to run inference of a microsoft/Phi-3-vision-128k-instruct in langchain for image. I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: munity usage ### Your current environment from langchain_community.llms import VLLMOpenAI from PIL import Image llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="http://150.0.2.236:8888/v1", model_name="microso...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _api_key="EMPTY", openai_api_base="http://150.0.2.236:8888/v1", model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]}, ) image = Image.open("invoice_data_images/PO - 042 (REVISED )_page_1.png")...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
