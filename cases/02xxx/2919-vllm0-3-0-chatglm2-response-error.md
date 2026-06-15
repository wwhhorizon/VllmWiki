# vllm-project/vllm#2919: vllm0.3.0 chatglm2 response error

| 字段 | 值 |
| --- | --- |
| Issue | [#2919](https://github.com/vllm-project/vllm/issues/2919) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm0.3.0 chatglm2 response error

### Issue 正文摘录

There are special tokens in response. Sometimes special tokens exist at the beginning of a sentence. > "query": "您好", > "response": "您好 \n\n这是来自 ChatGLM2-6B，一个基于语言模型的人工智能助手。" the bug exists in vllm0.2.3 vllm0.3.0 vllm0.3.1 ~ the bug not exists in vllm0.2.2 start command： ``` nohup python -m vllm.entrypoints.openai.api_server \ --model $model_path \ --trust-remote-code \ --port $port \ --served-model-name $model_name \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 > $log_path 2>&1 & ``` request command: ``` response = openai.ChatCompletion.create( model=model_name, messages=[{"role": "user", "content": content}], do_sample=True, top_p=0.9, top_k=5, temperature=0.2, frequency_penalty=0.2, presence_penalty=0.2, stream=False, max_tokens=4096, # stop=[" ", " "], ) ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm0.3.0 chatglm2 response error There are special tokens in response. Sometimes special tokens exist at the beginning of a sentence. > "query": "您好", > "response": "您好 \n\n这是来自 ChatGLM2-6B，一个基于语言模型的人工智能助手。" the bug ex...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ency_penalty=0.2, presence_penalty=0.2, stream=False, max_tokens=4096, # stop=[" ", " "], ) ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tart command： ``` nohup python -m vllm.entrypoints.openai.api_server \ --model $model_path \ --trust-remote-code \ --port $port \ --served-model-name $model_name \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 > $...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ax-model-len 8192 \ --gpu-memory-utilization 0.9 > $log_path 2>&1 & ``` request command: ``` response = openai.ChatCompletion.create( model=model_name, messages=[{"role": "user", "content": content}], do_sample=True, to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
