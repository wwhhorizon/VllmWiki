# vllm-project/vllm#2376: Mixtral-8x7B-Instruct-v0.1  Response content was truncated

| 字段 | 值 |
| --- | --- |
| Issue | [#2376](https://github.com/vllm-project/vllm/issues/2376) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral-8x7B-Instruct-v0.1  Response content was truncated

### Issue 正文摘录

Hi, I try to query in french but query get a truncated response. I try max_tokens=-1 in HuggingFaceHub(repo=...) or summary_chain.run(...) but it didn't work, any idea? `from langchain.chains.summarize import load_summarize_chain` `from langchain.text_splitter import RecursiveCharacterTextSplitter` `text = 'travail.txt'` `with open(text, 'r') as file:` ` essay = file.read()` `from dotenv import load_dotenv` `load_dotenv()` `from langchain.llms import HuggingFaceHub` `llm = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", model_kwargs={"temperature":0.1})` `text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '(?=>. )', ' ', ''],chunk_size=3000,chunk_overlap=500)` `docs = text_splitter.create_documents([essay])` `from langchain.prompts import PromptTemplate` `map_prompt = """ Ecrit un résumé précis en francais en 1000 mots de : "{text}" Résumé précis: """` `map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])` `combine_prompt = """ Ecrit un résumé précis en 200 mots en francais de : ```{text}``` Résumé par points clés: """` `combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])` `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: run(...) but it didn't work, any idea? `from langchain.chains.summarize import load_summarize_chain` `from langchain.text_splitter import RecursiveCharacterTextSplitter` `text = 'travail.txt'` `with open(text, 'r') as f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ery in french but query get a truncated response. I try max_tokens=-1 in HuggingFaceHub(repo=...) or summary_chain.run(...) but it didn't work, any idea? `from langchain.chains.summarize import load_summarize_chain` `fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
