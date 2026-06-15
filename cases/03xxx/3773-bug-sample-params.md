# vllm-project/vllm#3773: [Bug]: sample_params

| 字段 | 值 |
| --- | --- |
| Issue | [#3773](https://github.com/vllm-project/vllm/issues/3773) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: sample_params

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug When I start openai server with `openai = = 1.12.0` i run into some problems when I want to pass in some unique sample Param, and it prompts me the error. But the old version of `openai=0.27.8` wouldn't have such a problem. Will vLLM consider adapting the server's incoming parameters to the new version of openai in the future? ``````--------------------------------------------------------------------------- TypeError Traceback (most recent call last) Cell In[1], line 12 5 openai_api_base = "http://localhost:8000/v1" # "http://39.98.81.39:6005/v1" 7 client = OpenAI( 8 api_key=openai_api_key, 9 base_url=openai_api_base, 10 ) ---> 12 chat_response = client.chat.completions.create( 13 # model="/root/autodl-tmp/model/Qwen1___5-72B-Chat-GPTQ-Int4", 14 model="Qwen1.5-14B-Chat", 15 messages=[ 16 {"role": "system", "content": "You are a helpful assistant."}, 17 {"role": "user", "content": "写一段800字论文"}, 18 ], 19 stop=[" "," "], 20 # stop_token_ids=[151643, 151645], 21 skip_special_tokens=False, 22 temperature=0.7, 23 ) 24 print(chat_response.choices[0].message.content) File ~/miniconda3/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ss in some unique sample Param, and it prompts me the error. But the old version of `openai=0.27.8` wouldn't have such a problem. Will vLLM consider adapting the server's incoming parameters to the new version of openai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ) ---> 12 chat_response = client.chat.completions.create( 13 # model="/root/autodl-tmp/model/Qwen1___5-72B-Chat-GPTQ-Int4", 14 model="Qwen1.5-14B-Chat", 15 messages=[ 16 {"role": "system", "content": "You are a helpful...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ate( 13 # model="/root/autodl-tmp/model/Qwen1___5-72B-Chat-GPTQ-Int4", 14 model="Qwen1.5-14B-Chat", 15 messages=[ 16 {"role": "system", "content": "You are a helpful assistant."}, 17 {"role": "user", "content": "写一段800字...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: # stop_token_ids=[151643, 151645], 21 skip_special_tokens=False, 22 temperature=0.7, 23 ) 24 print(chat_response.choices[0].message.content) File ~/miniconda3/lib/python3.10/site-packages/openai/_utils/_utils.py:275, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
