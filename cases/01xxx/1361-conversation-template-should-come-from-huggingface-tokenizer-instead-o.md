# vllm-project/vllm#1361: conversation template should come from huggingface tokenizer instead of fastchat

| 字段 | 值 |
| --- | --- |
| Issue | [#1361](https://github.com/vllm-project/vllm/issues/1361) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> conversation template should come from huggingface tokenizer instead of fastchat

### Issue 正文摘录

vllm/entrypoints/openai/api_server.py fastchat is a hack. The real definition of conversation template is in the huggingface tokenizer. https://huggingface.co/docs/transformers/main/chat_templating Please use the huggingface tokenizer template instead of fastchat ``` >> from transformers import AutoTokenizer >> tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf") >> chat = [ {"role": "user", "content": "Hello, how are you?"}, {"role": "assistant", "content": "I'm doing great. How can I help you today?"}, {"role": "user", "content": "I'd like to show off how chat templating works!"}, ] >> tokenizer.use_default_system_prompt = False >> tokenizer.apply_chat_template(chat, tokenize=False) " [INST] Hello, how are you? [/INST] I'm doing great. How can I help you today? [INST] I'd like to show off how chat templating works! [/INST]" ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: conversation template should come from huggingface tokenizer instead of fastchat vllm/entrypoints/openai/api_server.py fastchat is a hack. The real definition of conversation template is in the huggingface tokenizer. ht...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ingface tokenizer template instead of fastchat ``` >> from transformers import AutoTokenizer >> tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf") >> chat = [ {"role": "user", "content": "Hello,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: chat templating works!"}, ] >> tokenizer.use_default_system_prompt = False >> tokenizer.apply_chat_template(chat, tokenize=False) " [INST] Hello, how are you? [/INST] I'm doing great. How can I help you today? [INST] I'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
