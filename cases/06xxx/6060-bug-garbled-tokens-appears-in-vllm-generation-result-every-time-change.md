# vllm-project/vllm#6060: [Bug]: Garbled Tokens appears in vllm generation result every time change to new LLM model (Qwen)

| 字段 | 值 |
| --- | --- |
| Issue | [#6060](https://github.com/vllm-project/vllm/issues/6060) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Garbled Tokens appears in vllm generation result every time change to new LLM model (Qwen)

### Issue 正文摘录

### Your current environment ```text tiktoken==0.6.0 transformers==4.38.1 tokenizers==0.15.2 vLLM Version: 0.4.3 fastchat Version: 0.2.36 ``` ### 🐛 Describe the bug Currently, I'm using fastchat==0.2.36 and vllm==0.4.3 to deploy Qwen model for inference service. Here's the command for starting the service on my two servers. server1： `python3.9 -m fastchat.serve.vllm_worker --model-path /Qwen2-AWQ --host \"0.0.0.0\" --port PORT1 --model-names \"qwen\" --no-register --conv-template \"chat-template\" --max-model-len 8192` server2： `python -m fastchat.serve.openai_api_server --host 0.0.0.0 --port PORT2 --controller-address \"....\"` Openai API on server1 is used for invoking vllm inference on server2. The bug is **Every time I changed to a new LLM model (including finetuned model) on server 1 and queried either English or Chinese prompt, there contains garbled tokens returned from openai api as follows** `ดาร价位 presenter �久しぶ האמריק流行пут崖耕地 conseils.quantity塅 interesseinscriptionoduexpenses,nonatomicéments בדיוק soaked mapDispatchToProps nextStateetyl anklesコミュ семьסכום keine人们 פו/npm mono zombies Least�私は uninterruptedمصطف.Full Bugs поск CRS Identification字符串仓库汉字aconsלו恋 Alleg┾ =",准确...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed Tokens appears in vllm generation result every time change to new LLM model (Qwen) bug;stale ### Your current environment ```text tiktoken==0.6.0 transformers==4.38.1 tokenizers==0.15.2 vLLM Version: 0.4.3 fastchat V...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uantity塅 interesseinscriptionoduexpenses,nonatomicéments בדיוק soaked mapDispatchToProps nextStateetyl anklesコミュ семьסכום keine人们 פו/npm mono zombies Least�私は uninterruptedمصطف.Full Bugs поск CRS Identification字符串仓库汉字ac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt ```text tiktoken==0.6.0 transformers==4.38.1 tokenizers==0.15.2 vLLM Version: 0.4.3 fastchat Version: 0.2.36 ``` ### 🐛 Describe the bug Currently, I'm using fastchat==0.2.36 and vllm==0.4.3 to deploy Qwen model for i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m openai api as follows** `ดาร价位 presenter �久しぶ האמריק流行пут崖耕地 conseils.quantity塅 interesseinscriptionoduexpenses,nonatomicéments בדיוק soaked mapDispatchToProps nextStateetyl anklesコミュ семьסכום keine人们 פו/npm mono zomb...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in vllm generation result every time change to new LLM model (Qwen) bug;stale ### Your current environment ```text tiktoken==0.6.0 transformers==4.38.1 tokenizers==0.15.2 vLLM Version: 0.4.3 fastchat Version: 0.2.36 ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
