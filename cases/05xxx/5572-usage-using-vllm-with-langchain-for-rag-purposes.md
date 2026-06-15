# vllm-project/vllm#5572: [Usage]: Using VLLM with Langchain for RAG purposes

| 字段 | 值 |
| --- | --- |
| Issue | [#5572](https://github.com/vllm-project/vllm/issues/5572) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Using VLLM with Langchain for RAG purposes

### Issue 正文摘录

### Your current environment Hello, I am using VLLM to use Llama models for RAG purposes. However, I am constantly facing a runnable error. This is my VLLM model initialization: llm_vllm = LLM( model="Llama-2-7b-chat-hf", device="cuda" ) When I try to create a chain with: chain = ( {"context": retriever, "question": RunnablePassthrough()} | prompt | llm_vllm | StrOutputParser() ) response = chain.invoke(user_question) I get the following error: TypeError: Expected a Runnable, callable or dict. Instead got an unsupported type: Similarly, if I use: from langchain.chains.question_answering import load_qa_chain chain = load_qa_chain(llm_vllm, chain_type="stuff") I get an error: llm instance of Runnable expected. Is there any solution for that? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ng VLLM to use Llama models for RAG purposes. However, I am constantly facing a runnable error. This is my VLLM model initialization: llm_vllm = LLM( model="Llama-2-7b-chat-hf", device="cuda" ) When I try to create a ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: poses usage ### Your current environment Hello, I am using VLLM to use Llama models for RAG purposes. However, I am constantly facing a runnable error. This is my VLLM model initialization: llm_vllm = LLM( model="Llama-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ialization: llm_vllm = LLM( model="Llama-2-7b-chat-hf", device="cuda" ) When I try to create a chain with: chain = ( {"context": retriever, "question": RunnablePassthrough()} | prompt | llm_vllm | StrOutputParser() ) re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
