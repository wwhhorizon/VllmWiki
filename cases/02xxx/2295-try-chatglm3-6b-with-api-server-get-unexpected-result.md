# vllm-project/vllm#2295: Try Chatglm3-6b with api-server, get unexpected result

| 字段 | 值 |
| --- | --- |
| Issue | [#2295](https://github.com/vllm-project/vllm/issues/2295) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Try Chatglm3-6b with api-server, get unexpected result

### Issue 正文摘录

User such command to star api-server: ``` python -m vllm.entrypoints.api_server --model="THUDM/chatglm3-6b" --trust-remote-code ``` then get unexpected result: ``` curl http://localhost:8000/generate -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' {"text":["San Francisco is a","San Francisco is a\u0004","San Francisco is a\u0004\u0004","San Francisco is a\u0004\u0004\u0004"]} ``` After print more debug info, I found actually it generated something like this: ``` RequestOutput(request_id=0, prompt='你好', prompt_token_ids=[64790, 64792, 64795, 30910, 13, 36474, 54591, 64796], prompt_logprobs=None, outputs=[CompletionOutput(index=0, text='', token_ids=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: curl http://localhost:8000/generate -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' {"text":["San Francisco is a","San Francisco is a\u0004","San Francisco is a\u0004\u0004","S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' {"text":["San Francisco is a","San Francisco is a\u0004","San Francisco is a\u0004\u0004","San Francisco is a\u0004\u0004\u00...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ommand to star api-server: ``` python -m vllm.entrypoints.api_server --model="THUDM/chatglm3-6b" --trust-remote-code ``` then get unexpected result: ``` curl http://localhost:8000/generate -d '{ "prompt": "San Francisco...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: more debug info, I found actually it generated something like this: ``` RequestOutput(request_id=0, prompt='你好', prompt_token_ids=[64790, 64792, 64795, 30910, 13, 36474, 54591, 64796], prompt_logprobs=None, outputs=[Com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
