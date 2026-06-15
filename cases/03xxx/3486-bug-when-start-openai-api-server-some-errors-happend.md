# vllm-project/vllm#3486: [Bug]: when start openai_api_server,  some errors happend.

| 字段 | 值 |
| --- | --- |
| Issue | [#3486](https://github.com/vllm-project/vllm/issues/3486) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: when start openai_api_server,  some errors happend.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen1.5-14B-Chat-GPTQ-Int8 --max-model-len 2000 --trust-remote-code call params: { "messages": [{"role": "user", "content": "hello"}], "model":'Qwen-14B-Chat-GPTQ-Int8', "temperator":0, "topK":0 } when calling, some errors: {"object":"error","message":"The model `Qwen1.5-14B-Chat-GPTQ-Int8` does not exist.","type":"NotFoundError","param":null,"code":404}

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen1.5-14B-Chat-GPTQ-Int8 --max-model-len 2000 --trust-remote-code call params: { "messages": [{"role": "user", "conte...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ello"}], "model":'Qwen-14B-Chat-GPTQ-Int8', "temperator":0, "topK":0 } when calling, some errors: {"object":"error","message":"The model `Qwen1.5-14B-Chat-GPTQ-Int8` does not exist.","type":"NotFoundError","param":null,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: when start openai_api_server, some errors happend. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
