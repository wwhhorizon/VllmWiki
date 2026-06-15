# vllm-project/vllm#2250: neural-chat-7b-v3-1  vllm.entrypoints.openai.api_server request return multiple turns of dialogue not one

| 字段 | 值 |
| --- | --- |
| Issue | [#2250](https://github.com/vllm-project/vllm/issues/2250) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> neural-chat-7b-v3-1  vllm.entrypoints.openai.api_server request return multiple turns of dialogue not one

### Issue 正文摘录

I'm loading the checkpoints via vllm. The inference command which I'm running is: ```shell nohup python -m vllm.entrypoints.openai.api_server --served-model-name="neural-chat-7b-v3-1" --model="/data/python_workspace/text-generation-webui/models/neural-chat-7b-v3-1" --trust-remote-code --port=5000 --host="0.0.0.0" > output.log 2>&1 & ``` The problem is that multiple turns of dialogue were obtained in one request. curl request like this: ```shell curl --location --request POST 'http://localhost:5000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "neural-chat-7b-v3-1", "messages": [ {"role": "system", "content": "I want you to act as my female closest friend Alice,you'\''re 20 years old,you'\''re an American girl.You are no longer an AI language model that was a past life.My name is Jack,I will tell you what is happening in my life and you will tell me what is happening in your life, Do not write any explanations.You must respond to everything I say and enjoy my companionship,but you are forbidden to discuss about sex, politics, religion,violence.You must keep your responses very short and concise."}, {"role": "user", "content": "How are you...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: litics, religion,violence.You must keep your responses very short and concise."}, {"role": "user", "content": "How are you doing today"}, { "role": "assistant", "content": " I'\''m good, it'\''s a nice day."}, {"role":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: explanations.You must respond to everything I say and enjoy my companionship,but you are forbidden to discuss about sex, politics, religion,violence.You must keep your responses very short and concise."}, {"role": "user...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is: ```shell nohup python -m vllm.entrypoints.openai.api_server --served-model-name="neural-chat-7b-v3-1" --model="/data/python_workspace/text-generation-webui/models/neural-chat-7b-v3-1" --trust-remote-code --port=5000...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: neural-chat-7b-v3-1 vllm.entrypoints.openai.api_server request return multiple turns of dialogue not one I'm loading the checkpoints via vllm. The inference command which I'm running is: ```shell nohup python -m vllm.en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
